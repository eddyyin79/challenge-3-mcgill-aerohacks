#LED debug (3 second blink) then motors on for 2 seconds then off
import time
from python.communication import esp_link as drone

from machine import Pin, PWM
LED_BLUE = Pin(7, Pin.OUT)
def __init__(self, motor_Pin):
    # Blink LED for 3 seconds
    print("Blinking LED for 3 seconds...")
    for i in range(6):
        LED_BLUE.value(1)
        time.sleep_ms(250)
        LED_BLUE.value(0)
        time.sleep_ms(250)

    def stabilize_drone(self, speed):
        if self.get_pitch() > 0.5:
            drone.manual_thrusts(speed - 1, speed, speed - 1, speed)
        if self.get_pitch() < -0.5:
            drone.manual_thrusts(speed + 1, speed , speed + 1, speed)
        if self.get_roll() > 0.5:
            drone.manual_thrusts(speed, speed - 1, speed , speed - 1)
        if self.get_roll() < -0.5:
            drone.manual_thrusts(speed, speed + 1, speed , speed + 1)
        if self.get_yaw() > 0.5:
            drone.manual_thrusts(speed +1, speed - 1, speed +1, speed - 1)
        if self.get_yaw() < -0.5:
            drone.manual_thrusts(speed - 1, speed + 1, speed - 1, speed + 1)

        #a front left, b front right, c back left, d back right
        #drone.manual_thrusts(a, b, c, d)