# from python.vision.open_cv import CameraSystem
# from python.control.hover_controller import HoverController
from python.communication import esp_link as drone
# from python.utils.config import *
import python.control.hover_controller as hc

import time

def main():
    drone.recalibrate()
    time.sleep(16)
    print("Done recalibration")
    print("For an emergency stop, press space!")

    # Setting drone to manual control (mode 1) and flying up to 0.5m (probably won't work)
    drone.set_mode(1)
    check_mode()
    drone.manual_thrusts(100,100,100,100)
    time.sleep(5)

    while True:
        stop = input()
        if stop == " ":
            print("Emergency stop activated!")
            drone.emergency_stop()
            break

        # Stabilize drone at 0.5m
        controller = hc.HoverController();
        check_mode() # should show mode 2
        controller.stabilize_drone()
        
        time.sleep(0.05) # avoiding constant comm with drone

def check_mode():
    mode = drone.get_mode()
    print("mode:", mode)

if __name__ == "__main__":
    main()