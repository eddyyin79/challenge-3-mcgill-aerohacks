#LED debug (3 second blink) for hover controller, 1 second 10% throttle


from machine import Pin, PWM   # machine is MicroPython's hardware control module
                                # Pin  → controls GPIO pins (on/off)
                                # PWM  → controls PWM signals (for motors)
import time                     # time → lets us pause the script (like sleep)


LED_BLUE = Pin(7, Pin.OUT)   # GPIO7  → Blue LED  

MOT_1    = PWM(Pin(5))       # GPIO5  → Motor 1
MOT_2    = PWM(Pin(6))       # GPIO6  → Motor 2
MOT_3    = PWM(Pin(3))       # GPIO3  → Motor 3
MOT_4    = PWM(Pin(4))       # GPIO4  → Motor 4


MOTOR_FREQ    = 50                    # 50 Hz
THROTTLE_10   = int(65535 * 0.10)     # 10% = 6553

for motor in [MOT_1, MOT_2, MOT_3, MOT_4]:
    motor.freq(MOTOR_FREQ)            # set frequency for each motor
    motor.duty_u16(0)                 # start with motors OFF (duty = 0)

print("Blinking LED for 3 seconds...")

for i in range(6):                    # 6 blinks × 500ms = 3 seconds
    LED_BLUE.value(1)                 # LED ON
    time.sleep_ms(250)                # wait 250ms
    LED_BLUE.value(0)                 # LED OFF
    time.sleep_ms(250)                # wait 250ms


print("Motors ON at 10% throttle...")

for motor in [MOT_1, MOT_2, MOT_3, MOT_4]:
    motor.duty_u16(THROTTLE_10)       # set each motor to 10%