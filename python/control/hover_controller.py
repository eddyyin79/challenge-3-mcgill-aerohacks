#LED debug (3 second blink) then motors on for 2 seconds then off
import time
from python.communication import esp_link as drone
from machine import Pin, PWM

LED_BLUE = Pin(7, Pin.OUT)

class HoverController:
    
    def __init__(self):

        print("Starting hover controller")

        drone.set_mode(2)

        drone.manual_thrusts(120,120,120,120)

    def stabilize_drone(self):

        pitch = drone.get_pitch()
        roll = drone.get_roll()

        print("pitch:", pitch, "roll:", roll)

        pitch_correction = -0.5 * pitch
        roll_correction = -0.5 * roll

        drone.set_pitch(pitch_correction)
        drone.set_roll(roll_correction)