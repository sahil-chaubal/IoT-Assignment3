# CIS600 IoT Assignment 3

Welcome to the CIS600 IoT Assignment 3 repository!

- **Virtual Sensor Station (Publisher):** Simulates an environmental station by generating random sensor readings (temperature, humidity, CO₂) and publishing them as JSON messages.
- **Cloud-Based IoT Backend (Subscriber):** Securely connects to AWS IoT Core to receive the sensor data, stores it in memory, and provides functions to display:
  - The latest sensor data for a specified station.
  - Sensor data from the last five hours for a specified sensor type.

---

## Setup Instructions

### Prerequisites
Before you begin, please ensure you have the following:
- **Python 3.9:** Install the latest version of Python.
- **paho-mqtt Library:** Install via pip:
  ```bash
  pip install paho-mqtt
   
AWS Account: You’ll need an AWS account to configure AWS IoT Core.

AWS IoT Core Configuration

Follow these steps to set up AWS IoT Core for your project:

    Create a Thing:

        Log in to the AWS Management Console and navigate to AWS IoT Core.
        Under Manage → Things, click Create things and select Create a single thing.
        Give your thing a unique name (e.g., station001) and finish the setup.

    Generate and Download Certificates:
        After creating your thing, generate a device certificate.
        Download the following files:
            Device Certificate: (e.g., certificate.pem.crt)
            Private Key: (e.g., private.pem.key)
            Amazon Root CA: (e.g., AmazonRootCA1.pem)

    Attach a Policy:
        Create a policy that grants the following permissions:
            iot:Connect
            iot:Publish
            iot:Subscribe
            iot:Receive
        Attach this policy to your certificate.

    Obtain the AWS IoT Endpoint:
        In the AWS IoT Core console, go to Settings.
        Copy the Endpoint value (e.g., a1b2c3d4e5f6-ats.iot.us-west-2.amazonaws.com).

Local Environment Setup
    Clone this repository to your local machine.
    Place your AWS IoT certificate files (device certificate, private key, and CA) in a secure directory.
    Update the file paths and AWS IoT endpoint in both the publisher.py and subscriber.py scripts accordingly.

Running the Code
Publisher Script

The publisher script simulates your virtual sensor station.
    Generates random sensor data for:
        Temperature: -50°C to 50°C
        Humidity: 0% to 100%
        CO₂: 300ppm to 2000ppm
    Publishes the data to an MQTT topic over a secure TLS connection to AWS IoT Core.

To run the publisher, open your terminal and execute:
python3 publisher.py

The subscriber script:
    Connects securely to AWS IoT Core.
    Subscribes to the MQTT topic to receive sensor data.
    Stores incoming data in memory.
    Offers functions to display:
        The latest sensor data for a specified station.
        All sensor data from the last five hours for a specified sensor type.

To run the subscriber, open another terminal and execute:
python3 subscriberndisplay.py

Note: Both scripts need to run concurrently so that the subscriber can capture real-time data from the publisher.

Troubleshooting:

Connection Errors
    AWS IoT Endpoint: Double-check the endpoint value set in your scripts.
    Internet Connection: Confirm you have a stable connection.
    Policy Permissions: Ensure your AWS IoT policy includes all necessary permissions (iot:Connect, iot:Publish, iot:Subscribe, and iot:Receive).

Dependency Issues
    If you see errors related to missing packages, install them using:
    pip3 install paho-mqtt

Thank you!
