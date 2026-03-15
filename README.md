# ESP32 Drone Hover with PID Control

This project enables an ESP32-based drone to autonomously hover using PID (Proportional-Integral-Derivative) control. The system integrates onboard sensor data, motor control, and optional computer vision for stable flight.

## Features

- **ESP32 Firmware**: Controls motors and reads IMU data.
- **Python Control Suite**: Communicates with the ESP32, implements PID hover logic, and provides utilities for testing and vision.
- **PID Control**: Maintains stable hover by adjusting motor thrusts based on real-time feedback.
- **Computer Vision (Optional)**: Uses OpenCV to process camera input for advanced stabilization or height control.

## Project Structure

```
esp32/
  imu.cpp, imu.h, motor.cpp, motor.h, pid.cpp, main.ino   # ESP32 firmware (C++/Arduino)
python/
  communication/esp_link.py        # Handles WiFi communication with ESP32
  control/
    hover_controller.py            # Main hover logic and stabilization
    motor_controller.py            # Motor control interface
    pid.py                         # PID controller implementation
  utils/config.py                  # Configuration settings (currently empty)
  vision/open_cv.py                # (Optional) Computer vision for drone
tests/
  camera_test.py                   # Test for camera/vision
  controller_test.py               # Test for hover controller logic
  pid_test.py                      # Test for PID controller
main.py                            # Example entry point for running the system
requirements.txt                   # Python dependencies (currently empty)
```

## Getting Started

### 1. ESP32 Firmware

- Write your flight logic in the `esp32/` directory (C++/Arduino).
- Upload the code to your ESP32 using the Arduino IDE or PlatformIO.

### 2. Python Control Suite

- Install Python 3.8+.
- (Optional) Install dependencies:
  ```
  pip install -r requirements.txt
  ```
- Run the main control script:
  ```
  python main.py
  ```

### 3. Communication

- The ESP32 acts as a WiFi server (default: `192.168.4.1:8080`).
- Python scripts connect to the ESP32 to send commands and receive telemetry.

### 4. PID Tuning

- Adjust PID parameters in `python/control/pid.py` for optimal stability.
- Use `tests/pid_test.py` to simulate and visualize PID response.

### 5. Computer Vision (Optional)

- Edit `python/vision/open_cv.py` to configure camera stream and color detection.
- Use for advanced hover/height control.

## Testing

- Use scripts in the `tests/` directory to validate individual components.
- Example: `controller_test.py` simulates hover logic; `pid_test.py` simulates PID response.

## Notes

- Avoid high-bandwidth communication with the ESP32 to prevent sensor drift.
- Emergency stop and manual thrust controls are available in the Python interface.

## License

MIT License
