from machine import Pin, PWM
import time
#LED debug (3 second blink) then motors on for 2 seconds then off

LED_BLUE = Pin(7, Pin.OUT)
class MotorController:
    def __init__(self, motor_Pin):
        self.MOT_0 = PWM(Pin(motor_Pin))

        self.MOT_0.freq(50)
        self.MOT_0.duty_u16(0)



    # Motor On max speed 
    def motor_on_max(self):
        print("Motor ON...")
        self.MOT_0.duty_u16(6553)
            
    # Set the porcentage Speed of the motor 
    def Set_speed_porcentage(self, speed):
        duty = int(65535 * (speed / 100))
        print(f"Setting motor speed to {speed}% (Duty: {duty})")
        self.MOT_0.duty_u16(duty)
        
        

    # Motors OFF  
    def motors_off(self):
        print("Motors OFF")
        self.MOT_0.duty_u16(0)
            #65535 max trotrle 