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
    print("Emergency stop, press space!")

    # camera = CameraSystem()       # idk if this works yet
    # controller = HoverController()


    while True:
        stop = input()
        if stop == " ":
            print("Emergency stop activated!")
            drone.emergency_stop()
            break
        # print("Testing connection...")

        # print("Mode:", drone.get_mode())

        # print("Pitch:", drone.get_pitch())

        # print("Roll:", drone.get_roll())

        drone.set_mode(1)
       
        mode = drone.get_mode()
        # print("mode:", mode)
        
        hc.stabilize_drone(0,0,0,0)
        time.sleep(5)

        drone.emergency_stop()



if __name__ == "__main__":
    main()