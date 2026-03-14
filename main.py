from python.vision.open_cv import CameraSystem
from python.control.hover_controller import HoverController
from python.communication import esp_link as drone
from python.utils.config import *

import time

def main():

    CONTROL_DT = 2000

    # camera = CameraSystem()       # idk if this works yet
    controller = HoverController()

    while True:

        # position = camera.get_position() 

        roll,pitch,throttle = controller.update(position)

        print("position:",position)
        print("roll:", roll)
        print("pitch:", pitch)
        print("throttle:", throttle)

        time.sleep(CONTROL_DT)


if __name__ == "__main__":
    main()