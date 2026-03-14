from python.control.pid import PID
import matplotlib.pyplot as plt

pid = PID(1.0, 0.0, 0.1)

position = 1.0
target = 0.0

positions = []

for i in range(200):

    error = target - position
    control = pid.update(error, 0.02)

    position += control * 0.02

    positions.append(position)

print("final position:", position)