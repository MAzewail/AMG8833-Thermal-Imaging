# AMG8833 Thermal Imaging Sensor with Arduino Uno

This repository contains the necessary code to interface with an AMG8833 thermal imaging sensor using an Arduino Uno board. The code enables you to capture temperature data from the sensor and visualize it as a live heatmap image.

![Thermal Image](https://github.com/MAzewail/AMG8833-Thermal-Imaging/blob/main/frame_39.png)

## Prerequisites

Before running the program, you need to ensure you have the following hardware components:

- Arduino Uno board
- AMG8833 thermal imaging sensor
- Jumper wires
- USB cable for connecting the Arduino to your computer

## Dependencies

The Arduino code relies on the following libraries:

- [Adafruit_AMG88xx](https://github.com/adafruit/Adafruit_AMG88xx): Library for interacting with the AMG8833 sensor.

The Python code requires the following libraries to be installed:

- [PySerial](https://pythonhosted.org/pyserial/): Library for serial communication with Arduino.
- [NumPy](https://numpy.org/): Fundamental package for scientific computing with Python.
- [Matplotlib](https://matplotlib.org/): Library for creating visualizations in Python.

You can install the Python dependencies using the following command:

```
pip install pyserial numpy matplotlib
```

## Circuit Diagram

To connect the AMG8833 sensor to the Arduino Uno, follow the circuit diagram below:

```
+---------+     +-----------------+
| AMG8833 |     |     Arduino     |
+---------+     +-----------------+
| Vin     |-----| 5V              |
| GND     |-----| GND             |
| SDA     |-----| A4 (SDA)        |
| SCL     |-----| A5 (SCL)        |
+---------+     +-----------------+
```

## Usage

1. Connect the AMG8833 sensor to the Arduino Uno following the circuit diagram provided.

2. Upload the Arduino code (`amg8833_arduino.ino`) to your Arduino board using the Arduino IDE.

3. Connect your Arduino Uno to your computer using the USB cable.

4. Open the Python script (`amg8833_python.py`) and update the `PORT` variable with the appropriate serial port on your system.

5. Run the Python script using the following command:

   ````
   python amg8833_python.py
   ```

   This will open a window displaying the live thermal heatmap image captured by the sensor.

## Customization

- You can modify the Python code (`amg8833_python.py`) to adjust the visualization settings, such as color mapping, minimum and maximum temperature thresholds, etc.

- Explore the [Adafruit_AMG88xx library documentation](https://github.com/adafruit/Adafruit_AMG88xx) to learn more about the available functions for interacting with the AMG8833 sensor.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The Adafruit_AMG88xx library for providing an easy-to-use interface for the AMG8833 sensor.

- The Arduino community for their support and contributions.

## Contact

If you have any questions or need further assistance, feel free to contact Mohamed Abdallah at mohammed.abdallah.salem@gmail.com.
