# from python.vision.open_cv import CameraSystem
# from python.control.hover_controller import HoverController
from python.communication import esp_link as drone
# from python.utils.config import *

import time

def main():
    drone.recalibrate()
    time.sleep(16)
    print("Done recalibration")


    CONTROL_DT = 0.05

    # camera = CameraSystem()       # idk if this works yet
    # controller = HoverController()

    iterations = 0

    while iterations < 3:
        print("Testing connection...")

        print("Mode:", drone.get_mode())

        print("Pitch:", drone.get_pitch())

        print("Roll:", drone.get_roll())

        drone.set_mode(1)
       
        mode = drone.get_mode()
        print("mode:", mode)
        
        drone.manual_thrusts(250,250,250,250)

        time.sleep(5)

        drone.emergency_stop()

        iterations += 1


if __name__ == "__main__":
    main()