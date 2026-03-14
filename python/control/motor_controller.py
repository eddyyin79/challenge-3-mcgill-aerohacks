from machine import Pin, PWM
import time
from python.communication import esp_link as drone

#LED debug (3 second blink) then motors on for 2 seconds then off

LED_BLUE = Pin(7, Pin.OUT)
class MotorController:
    def __init__(self):
        drone.manual_thrusts(0,0,0,0)

    # Motor On max speed 
    def motor_on_max(self):
        print("Motor ON...")
        drone.manual_thrusts(255,255,255,255)

    # Motors OFF  
    def motors_off(self):
        print("Motor OFF...")
        drone.manual_thrusts(0,0,0,0)
