# IoT Hub Pi Hackathon

## Overview
This hackathon demonstrates connecting a Raspberry Pi running Raspian to [Azure IoT Hub] (https://azure.microsoft.com/en-us/services/iot-hub/) and sending telemetry to Azure IoT Hub from either:
- a physical [Sense HAT] (https://www.raspberrypi.org/products/sense-hat/) connected to the Raspberry Pi; or
- a [Sense HAT Emulator] (https://www.raspberrypi.org/blog/sense-hat-emulator/) installed on the Raspberry Pi.

Completing this hackathon will provide you with the basic skills needed to connect and securely send telemetry from a physical device (e.g. a field device or field gateway) to the Azure IoT Hub. This hackathon does not demonstrate what can be done with the data after it arrives at the Azure IoT Hub. Having said that, you can do almost anything including complex event processing, stream processing, saving telemetry to blob storage or databases, analytics, training of Machine Learning models etc.

### Why Sense HAT?
We didn't want you to mess around with breadboards, jumper cables, resistors etc. This just wastes time and adds nothing to the goal of connecting a sensor to Azure IoT Hub. The Sense HAT has all the necessary components installed on the circuit board, including a ready to use library, and a series of sensors to play with.

### Why HTTPS and REST?
For simplicity and to avoid downloading/compiling SDKs during the hackathon, we chose to send the Sense Hat telemetry to Azure IoT Hub using the [IoT Hub REST API] (https://docs.microsoft.com/en-us/rest/api/iothub/) over HTTPS. Of course, you can use one of the many device SDKs available, which support sending messages over AMQP and MQTT. If you want to use the device SDKs, please visit [https://github.com/Azure/azure-iot-sdks] (https://github.com/Azure/azure-iot-sdks).

## Requirements
- [Raspberry Pi 3 Model B] (https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) (Pi 2 Model B with USB Wi-Fi dongle will probably work as well) with latest version of Raspian installed on the micro SD card. Using [NOOBS] (https://www.raspberrypi.org/downloads/noobs/) works fine. 
- [Sense HAT Emulator] (https://www.raspberrypi.org/blog/sense-hat-emulator/) (which comes with the Raspian O/S)
- [Sense HAT] (https://www.raspberrypi.org/products/sense-hat/) (optional - for those that want to play with real hardware)
- Laptop (running whatever operating system you desire) but ideally running Windows so you can install/run [Device Explorer] (https://github.com/Azure/azure-iot-sdks/releases/download/2016-11-17/SetupDeviceExplorer.msi). 
- An Azure account. You can create a [free trial] (https://azure.microsoft.com/en-us/free/?b=17.01) Azure subscription, or you can use an MSDN Azure subscription or a subscription from your company. 
- A basic understanding of Python and Linux.
- TBD

## Advance Setup (Must be completed in advance of the hackathon)
Please perform the following steps in advance of the hackathon otherwise you will waste the entire hackathon performing these steps.
- Ensure your Raspberry Pi can boot [Raspian] (https://www.raspberrypi.org/downloads/) from the SD card.
- Ensure Sense HAT Emulator is installed (by default it is installed with Raspian). Verify by checking under 'Programming' in the Raspian GUI.
- Install [Device Explorer] (https://github.com/Azure/azure-iot-sdks/releases/download/2016-11-17/SetupDeviceExplorer.msi) on your Winbdows laptop. Device Explorer is a great tool to see messages coming into the IoT Hub from your Raspberry Pi. 
- TBD

## Steps (Performed by students during hackathon)
1. //TODO - Lots of steps to add here, including screen shots. These steps will include connecting their Raspi to Wi-Fi, logging into their trail Azure subscription, creating and configuring Azure IoT Hub, downloading SenseHat_IoTHub.py from this repo to their Raspi and updating the connection string to start sending Sense HAT data to IoT Hub, etc...
2. Referring to the [Sense Hat API] (https://pythonhosted.org/sense-hat/api/), update the code to send other telemetry to IoT Hub from the Sense HAT. 
3. Update the code to send multiple telemetry data points (e.g. Yaw, Pitch, Roll, or Temperature, Pressure, Humidity) in a single JSON-formatted message to IoT Hub. See [sample_payload.json] (sample_payload.json). Solution source code - Authorized MSFT personnel only [SenseHat_IoTHub_JSON.py] (https://microsoft-my.sharepoint.com/personal/kehilsch_microsoft_com/_layouts/15/guestaccess.aspx?guestaccesstoken=sdOEuDcq984383oB3iqDyt2y8wIhqAmXvKQb75V7LUA%3d&docid=2_1c28ea3292574419d932d16dacb6e4204&rev=1).
4. Display the HTTP response code from the IoT Hub message onto the Sense HAT LED display. Solution source code - Authorized MSFT personnel only [SenseHat_IoTHub_JSON_LED.py] (https://microsoft-my.sharepoint.com/personal/kehilsch_microsoft_com/_layouts/15/guestaccess.aspx?guestaccesstoken=l%2bcljVkaJf6TEt7CWShh2FmMWnYquyVnnwivcnQ1s7I%3d&docid=2_1b7e74a4df92a4681b60b821fb38bf666&rev=1).

##//TODO
- Determine number of temp Azure subscriptions needed for attendees
- Finish TBD/TODO sections above.
- Determine how to join Pi to local Wi-Fi network and to obtain IP of PI device. Bring HDMI monitor and cable?
- Terry to add additional steps to integrate Streaming Analytics, PowerBI.
