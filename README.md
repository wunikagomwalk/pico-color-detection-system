# Raspberry Pi Pico Color Detection System

An embedded color detection and classification system developed using a Raspberry Pi Pico, TCS3200 color sensor, and 16×2 LCD display. The system measures color sensor outputs, processes the readings using MicroPython, classifies the detected color, and displays the result in real time.

## Project Overview

The goal of this project was to design and implement a microcontroller-based system capable of detecting and distinguishing between different colors.

The TCS3200 color sensor measures the intensity of red, green, and blue components of an object. A Raspberry Pi Pico processes these measurements using MicroPython and determines the detected color based on the sensor readings. The resulting classification is displayed on a 16×2 LCD.

## Hardware

- Raspberry Pi Pico
- TCS3200/TCS230 color sensor
- 16×2 LCD display
- Breadboard
- Jumper wires
- Resistors
- External 5V supply for LCD

## Software & Technologies

- MicroPython
- Thonny IDE
- GPIO
- Embedded Systems
- Sensor Interfacing

## System Operation

1. The TCS3200 sensor measures RGB color information from the target object.
2. The Raspberry Pi Pico reads the sensor output.
3. MicroPython processes and compares the RGB measurements.
4. The program determines the closest color classification.
5. The detected color is displayed on the LCD.

## Engineering Challenges

### Sensor Calibration and Lighting

During testing, red initially appeared dominant across several objects. Sensor performance was highly dependent on illumination and the position of the object relative to the sensor.

Testing under more consistent lighting conditions and evaluating the RGB measurements helped improve color classification.

### LCD Power

The LCD initially displayed blocks instead of the expected text when powered directly from the Raspberry Pi Pico's 3.3V supply.

The display was later powered using a 5V supply, allowing it to operate correctly while interfacing with the Pico.

### Hardware Debugging

Several wiring and sensor-output issues were identified during prototyping. GPIO connections, sensor control pins, and power connections were systematically checked and corrected during testing.

## Testing

The completed prototype was tested using multiple colors, including:

- Red
- Blue
- Green
- Yellow
- Orange
- Grey

Sensor readings were monitored during testing and compared to observed colors to evaluate classification performance.

## What I Learned

This project strengthened my understanding of:

- Microcontroller programming
- GPIO configuration
- Sensor interfacing
- Hardware/software integration
- Breadboard prototyping
- Sensor calibration
- Hardware debugging and troubleshooting

The project also demonstrated how environmental conditions such as lighting can significantly affect real-world sensor performance.

## Future Improvements

Future development could include:

- Improved calibration using collected sensor data
- More robust classification algorithms
- Support for a larger range of colors
- A compact PCB implementation
- Improved enclosure and controlled illumination
