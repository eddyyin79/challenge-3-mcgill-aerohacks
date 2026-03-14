from vision.camera import CameraSystem
from control.hover_controller import HoverController
from communication.esp_link import ESPLink
from utils.config import *

import time

def main():

    camera = CameraSystem()
    controller = HoverController()

    drone = None  # replace later

    while True:

        position = camera.get_position()

        roll,pitch,throttle = controller.update(position)

        print("pos:",position)
        print("cmd:",roll,pitch,throttle)

        time.sleep(CONTROL_DT)


if __name__ == "__main__":
    main()