# IoT Hub Pi Hackathon Content

## Overview
This hackathon demonstrates connecting a Raspberry Pi running Raspian to [Azure IoT Hub] (https://azure.microsoft.com/en-us/services/iot-hub/). The Raspberry Pi will be sending telemetry to Azure IoT Hub from either:
- a physical [Sense Hat] (https://www.raspberrypi.org/products/sense-hat/) connected to the Raspberry Pi; or
- a Sense Hat simulator installed on the Raspberry Pi.

### Why Sense Hat?
We didn't want to mess around with breadboards, jumper cables, resistors etc. This just wastes time and adds nothing to the goal of connecting a sensor to Azure IoT Hub. 

### Why HTTPS and REST?
For simplicity and to avoid downloading/compiling SDKs during the hackathon, we chose to send the Sense Hat telemetry to Azure IoT Hub using the [IoT Hub REST API] (https://docs.microsoft.com/en-us/rest/api/iothub/) over HTTPS. Of course, you can use one of the many device SDKs available, which support sending messages over AMQP and MQTT. If you want to use the device SDKs, please visit [https://github.com/Azure/azure-iot-sdks] (https://github.com/Azure/azure-iot-sdks).

## Requirements
- Raspberry Pi 3 (Model 2+ will probably work as well) with latest version of Raspian installed on the micro SD card
- Sense Hat Simulator (which comes with the Raspian O/S)
- Sense Hat (optional - for those that want to play with real hardware)
- Laptop (running whatever operating system you desire) but ideally running Windows so you can install/run Device Explorer. 
- An Azure account (either a trial account, or a development subscription from your company). 
- TBD

## Advanced Setup (Must be completed in advanced of the hackathon)
Please perform the following steps in advance of the hackathon otherwise you will waste the entire hackathon performing these steps.
- Ensure your Raspberry Pi can boot Raspian from the SD card.
- Ensure Sense Hat Simulator is installed (by default it is installed with Raspian). Check under 'Programming' in the Raspian GUI.
- Install [Device Explorer] (https://github.com/Azure/azure-iot-sdks/releases/download/2016-11-17/SetupDeviceExplorer.msi) on your Winbdows laptop. Device Explorer is a great tool to see messages coming into the IoT Hub from your Raspberry Pi. 
- TBD

##//TODO
- Find out how to offer temp Azure subscriptions. I know there is a way...just need to find this.
- Order a real Sense Hat and test code sample.
