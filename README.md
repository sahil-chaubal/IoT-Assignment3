# CIS600 IoT Assignment 3: Cloud-based IoT System using AWS IoT Core

Welcome to the CIS600 IoT Assignment 3 repository!

- **Virtual Sensor Station (Publisher):** Simulates an environmental station by generating random sensor readings (temperature, humidity, CO₂) and publishing them as JSON messages.
- **Cloud-Based IoT Backend (Subscriber):** Securely connects to AWS IoT Core to receive the sensor data, stores it in memory, and provides functions to display:
  - The latest sensor data for a specified station.
  - Sensor data from the last five hours for a specified sensor type.

---

## Setup Instructions

### Prerequisites
Before you begin, please ensure you have the following:
- **Python 3.x:** Install the latest version of Python.
- **paho-mqtt Library:** Install via pip:
  ```bash
  pip install paho-mqtt
