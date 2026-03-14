import cv2, numpy as np

# === SETTINGS ===
# This is the address of the drone's camera, like a website but for video
STREAM_URL = "http://192.168.x.x/stream"

# This is how big the blue light should look when the drone is at the perfect height (0.5m)
# You need to test this yourself! Hold the drone at 0.5m and check what number prints out
TARGET_AREA = 3000

# These are the colors the camera looks for (red light in HSV format)
# HSV is just a different way computers understand colors
# Note: red in HSV wraps around 0, so we use two ranges and combine them.
RED_L1 = np.array([0, 150,  70])      # darkest red near 0 degrees
RED_U1 = np.array([10, 255, 255])     # brightest red near 10 degrees
RED_L2 = np.array([170, 150,  70])    # darkest red near 170 degrees
RED_U2 = np.array([180, 255, 255])    # brightest red near 180 degrees

# Open the drone camera stream (like opening a YouTube video)
cap = cv2.VideoCapture(STREAM_URL)


# === FIND THE BLUE LIGHT ===
def get_blob(frame):
    # Step 1: convert the photo colors so the computer can find blue easier
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Step 2: create a black and white image where
    # WHITE = red light pixels
    # BLACK = everything else
    mask1 = cv2.inRange(hsv, RED_L1, RED_U1)
    mask2 = cv2.inRange(hsv, RED_L2, RED_U2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Step 3: erode = shrink white areas (removes tiny dots of noise)
    mask = cv2.erode(mask, None, iterations=2)

    # Step 4: dilate = grow white areas back (restores the real blob size)
    mask = cv2.dilate(mask, None, iterations=2)

    # Step 5: find the outlines of all white blobs in the image
    cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Step 6: ignore tiny blobs (smaller than 200 pixels, probably just noise)
    # and return only the biggest blob we found
    big_blobs = [c for c in cnts if cv2.contourArea(c) > 200]
    return max(big_blobs, key=cv2.contourArea, default=None)


# === MAIN LOOP (runs forever until you press Q) ===
while True:

    # Grab one photo from the drone camera
    ret, frame = cap.read()

    # If the camera stopped working, exit the loop
    if not ret:
        print("Camera stopped working!")
        break

    # Try to find the blue light in the photo
    blob = get_blob(frame)

    if blob:
        # Measure how big the blue light looks right now
        current_area = cv2.contourArea(blob)

        # Calculate the error: how far are we from the perfect size?
        # positive number = blob too big  = drone too low  = needs to go up
        # negative number = blob too small = drone too high = needs to go down
        err = current_area - TARGET_AREA

        # Decide what to do based on the error
        if abs(err) < 300:
            cmd = "HOLD"     # close enough, stay here
        elif err > 0:
            cmd = "DESCEND"  # blob too big = too low = go down
        else:
            cmd = "ASCEND"   # blob too small = too high = go up

        # --> plug err into YOUR PID here and send correction to motors
        # your_pid(err)

        # Print what the drone is thinking so you can see it
        print(f"{cmd} | error: {err:.0f}")

    else:
        # Blue light not found in the photo
        print("Cannot see the blue light!")

    # Wait 1ms and check if Q was pressed to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the camera when done
cap.release()