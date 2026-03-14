from python.control.hover_controller import HoverController

controller = HoverController()

# simulate drone slightly off center
position = (0.1, -0.05, 0.45)

roll, pitch, throttle = controller.update(position)

print("roll:", roll)
print("pitch:", pitch)
print("throttle:", throttle)