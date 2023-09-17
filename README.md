# ESP8266-Network-Scanner
A MicroPython-based network scanner for ESP8266 chips.

![ESP8266](https://img.shields.io/badge/Platform-ESP8266-blue)
![MicroPython](https://img.shields.io/badge/Language-MicroPython-green)

## Description

The ESP8266 Network Scanner is a versatile and efficient tool for monitoring and scanning wireless Access Point (AP) networks using ESP8266 microcontroller-based chips. This project allows you to easily scan for available Wi-Fi AP networks in your vicinity and collect essential information such as SSID, signal strength (RSSI), encryption type, and channel. The collected data is stored in a JSON file for analysis and further use.

## Features

- Continuous scanning of nearby Wi-Fi networks.
- Data collection for SSID, RSSI, encryption type, and channel.
- JSON-based database for storing network information.
- Simple and intuitive MicroPython codebase.
- Easily adaptable for various IoT and network monitoring applications.

## Getting Started

To get started with the ESP8266 Network Scanner, follow these steps:

1. **Clone the Repository:**

2. **Upload Code to ESP8266:**
- Use your preferred method to upload the `main.py` and `db.py` files to your ESP8266 device.

3. **Run the Scanner:**
- Power up your ESP8266 and let it run the scanning script.
- The collected network data will be stored in a JSON file.

4. **View and Analyze Data:**
- Retrieve the JSON file from the ESP8266 or access it remotely, depending on your setup.
You can retrieve "networks.json" by with ampy
- Analyze the collected data to gain insights into nearby Wi-Fi networks.

## Contributing

Contributions are welcome! If you'd like to enhance this project or fix any issues, please submit a pull request. For major changes, please open an issue first to discuss the proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

