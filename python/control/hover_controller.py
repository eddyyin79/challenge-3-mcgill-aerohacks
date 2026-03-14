#LED debug (3 second blink) then motors on for 2 seconds then off
import time
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