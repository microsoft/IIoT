# IoT Hub Pi Hackathon

## Overview
This hackathon demonstrates connecting a Raspberry Pi running Raspian to [Azure IoT Hub] (https://azure.microsoft.com/en-us/services/iot-hub/) and sending telemetry to Azure IoT Hub from either:
- a physical [Sense Hat] (https://www.raspberrypi.org/products/sense-hat/) connected to the Raspberry Pi; or
- a [Sense Hat Emulator] (https://www.raspberrypi.org/blog/sense-hat-emulator/) installed on the Raspberry Pi.

Completing this hackathon will provide you with the basic skills needed to connect and securely send telemetry from a physical device (e.g. a field device or field gateway) to the Azure IoT Hub. This hackathon does not demonstrate what can be done with the data after it arrives at the Azure IoT Hub. Having said that, you can do almost anything including complex event processing, stream processing, saving telemetry to blob storage or databases, analytics, training of Machine Learning models etc.

### Why Sense Hat?
We didn't want you to mess around with breadboards, jumper cables, resistors etc. This just wastes time and adds nothing to the goal of connecting a sensor to Azure IoT Hub. The Sense Hat has all this preinstalled on the circuit board, a ready to use library, and a series of sensors to play with.

### Why HTTPS and REST?
For simplicity and to avoid downloading/compiling SDKs during the hackathon, we chose to send the Sense Hat telemetry to Azure IoT Hub using the [IoT Hub REST API] (https://docs.microsoft.com/en-us/rest/api/iothub/) over HTTPS. Of course, you can use one of the many device SDKs available, which support sending messages over AMQP and MQTT. If you want to use the device SDKs, please visit [https://github.com/Azure/azure-iot-sdks] (https://github.com/Azure/azure-iot-sdks).

## Requirements
- [Raspberry Pi 3 Model B] (https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) (Pi 2 Model B with USB Wi-Fi dongle will probably work as well) with latest version of Raspian installed on the micro SD card. Using [NOOBS] (https://www.raspberrypi.org/downloads/noobs/) works fine. 
- [Sense Hat Emulator] (https://www.raspberrypi.org/blog/sense-hat-emulator/) (which comes with the Raspian O/S)
- [Sense Hat] (https://www.raspberrypi.org/products/sense-hat/) (optional - for those that want to play with real hardware)
- Laptop (running whatever operating system you desire) but ideally running Windows so you can install/run [Device Explorer] (https://github.com/Azure/azure-iot-sdks/releases/download/2016-11-17/SetupDeviceExplorer.msi). 
- An Azure account (either a trial account, or a development subscription from your company). 
- A basic understanding of Python and Raspian.
- TBD

## Advanced Setup (Must be completed in advanced of the hackathon)
Please perform the following steps in advance of the hackathon otherwise you will waste the entire hackathon performing these steps.
- Ensure your Raspberry Pi can boot Raspian from the SD card.
- Ensure Sense Hat Emulator is installed (by default it is installed with Raspian). Check under 'Programming' in the Raspian GUI.
- Install [Device Explorer] (https://github.com/Azure/azure-iot-sdks/releases/download/2016-11-17/SetupDeviceExplorer.msi) on your Winbdows laptop. Device Explorer is a great tool to see messages coming into the IoT Hub from your Raspberry Pi. 
- TBD

## Steps (Performed by students during hackathon)
1. TBD
2. Refer to the [SenseHat API] (https://pythonhosted.org/sense-hat/api/) and try sending other telemetry to IoT Hub from SenseHat. 
2. Change the python code to send multiple telemetry data points (e.g. Yaw, Pitch, Roll, or Temperature, Pressure, Humidity) in a single JSON-formatted message to IoT Hub.

##//TODO
- Find out how to offer temp Azure subscriptions. I know there is a way...just need to find this.
- Build JSON code to send multipe data points to IoT Hub.
- Print the IoT Hub return message to the LED display on the SenseHat.
- Determine how to join Pi to local Wi-Fi network and to obtain IP of PI device. Bring HDMI monitor and cable?
