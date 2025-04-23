# Spot Micro RC

Spot Micro RC is a Bluetooth-controlled robot dog built on the Spot Micro platform. It features six degrees of movement, including forward, backward, left, right, crouching, and roll rotation. Designed to run on a Raspberry Pi 4, it utilizes a PCA9685 servo driver for precise control of servo motors. This project combines robotics, Bluetooth communication, and embedded systems to create a versatile and interactive robotic companion.

## Features

- **Six Degrees of Movement**: Forward, backward, left, right, crouching, and roll rotation.
- **Bluetooth Control**: Seamless communication with a mobile device or controller.
- **Raspberry Pi 4**: Acts as the brain of the robot, running the control software.
- **PCA9685 Servo Drivers**: Ensures precise and smooth control of servo motors.
- **Customizable**: Open-source design allows for modifications and enhancements.

## Requirements

- Raspberry Pi 4 (or compatible)
- PCA9685 servo driver
- Servo motors (12x)
- Power supply
- 3D-printed parts for the Spot Micro frame [Thingiverse](https://www.thingiverse.com/thing:3445283).
- Python 3.x
- Required Python libraries (e.g., `Adafruit_PCA9685`, `pybluez`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Spot-Micro-RC.git
    cd Spot-Micro-RC
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Assemble the hardware components following the Spot Micro design.

4. Upload the control software to the Raspberry Pi.

## Usage

1. Power on the robot and ensure the Bluetooth module is active.
2. Pair your mobile device or controller with the robot.
3. Run the control script on the Raspberry Pi:
    ```bash
    python main.py
    ```
4. Use the paired device to control the robot's movements.

## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Inspired by the original Spot Micro design by Deok-yeon Kim [Thingiverse](https://www.thingiverse.com/thing:3445283).
- Thanks to the open-source community for providing tools and libraries.

