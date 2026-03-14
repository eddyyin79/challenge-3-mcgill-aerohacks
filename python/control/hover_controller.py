#LED debug (3 second blink) then motors on for 2 seconds then off
import time
from python.communication import esp_link as drone
import math
def __init__(self, motor_Pin):
    # Blink LED for 3 seconds
    print("Blinking LED for 3 seconds...")
    self.total_thrust = 1.0

def stabilize_drone(self, speed):
    if drone.get_pitch() > 0.5:
        drone.increment_thrusts(speed - 1, speed, speed - 1, speed)
    if drone.get_pitch() < -0.5:
        drone.increment_thrusts(speed + 1, speed , speed + 1, speed)
    if drone.get_roll() > 0.5:
        drone.increment_thrusts(speed, speed - 1, speed , speed - 1)
    if drone.get_roll() < -0.5:
        drone.increment_thrusts(speed, speed + 1, speed , speed + 1)

    #a front left, b front right, c back left, d back right
    #drone.manual_thrusts(a, b, c, d)
def PID_hover(self, target_pitch, target_roll, target_altitude):
        # Implement PID control logic here
        # Calculate errors
    pitch_error = target_pitch - drone.get_pitch()
    roll_error = target_roll - drone.get_roll()

        # Estimate vertical thrust component
        # total_thrust should be the sum of all motor thrusts (define as needed)
        # Example: total_thrust = a + b + c + d (or pass as argument)
        # For demonstration, set total_thrust = 1.0 (replace with real value)
    
    pitch_rad = math.radians(drone.get_pitch())
    roll_rad = math.radians(drone.get_roll())
    vertical_thrust = self.total_thrust * math.cos(pitch_rad) * math.cos(roll_rad)

        # If you know the drone's mass, you can estimate vertical acceleration:
        # mass = ... # in kg
        # g = 9.81
        # vertical_accel = (vertical_thrust / mass) - g

       # Placeholder, since true altitude is not available

        # Calculate control outputs (this is a simplified example)
    pitch_control = 1 * pitch_error  # P term only
    roll_control = 1 * roll_error    # P term only
    altitude_control = 1 * vertical_thrust  # P term only

        # Adjust motor speeds based on control outputs
    a = altitude_control + pitch_control + roll_control 
    b = altitude_control + pitch_control - roll_control 
    c = altitude_control - pitch_control + roll_control
    d = altitude_control - pitch_control - roll_control

    self.total_thrust = a + b + c + d  # Update total thrust based on control outputs
    drone.manual_thrusts(a, b, c, d)