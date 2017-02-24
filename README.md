# IoT Hub Pi Hackathon

## Overview
This hackathon demonstrates connecting a Raspberry Pi running Raspian to [Azure IoT Hub] (https://azure.microsoft.com/en-us/services/iot-hub/) and sending telemetry to Azure IoT Hub from either:
- a physical [Sense HAT](https://www.raspberrypi.org/products/sense-hat/) connected to the Raspberry Pi; or
- a [Sense HAT Emulator](https://www.raspberrypi.org/blog/sense-hat-emulator/) installed on the Raspberry Pi.

Completing this hackathon will provide you with the basic skills needed to connect and securely send telemetry from a physical device (e.g. a field device or field gateway) to the Azure IoT Hub. This hackathon does not demonstrate what can be done with the data after it arrives at the Azure IoT Hub. Having said that, you can do almost anything including complex event processing, stream processing, saving telemetry to blob storage or databases, analytics, training of Machine Learning models etc.

### Why Sense HAT?
We didn't want you to mess around with breadboards, jumper cables, resistors etc. This just wastes time and adds nothing to the goal of connecting a sensor to Azure IoT Hub. The Sense HAT has all the necessary components installed on the circuit board, including a ready to use library, and a series of sensors to play with.

### Why HTTPS and REST?
For simplicity and to avoid downloading/compiling SDKs during the hackathon, we chose to send the Sense Hat telemetry to Azure IoT Hub using the [IoT Hub REST API](https://docs.microsoft.com/en-us/rest/api/iothub/) over HTTPS. Of course, you can use one of the many device SDKs available, which support sending messages over AMQP and MQTT. If you want to use the device SDKs, refer to the Using the .NET Device SDK section below.

## Requirements
- [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) (Pi 2 Model B with USB Wi-Fi dongle will probably work as well) with latest version of Raspian installed on the micro SD card. Using [NOOBS](https://www.raspberrypi.org/downloads/noobs/) works fine. 
- [Sense HAT Emulator](https://www.raspberrypi.org/blog/sense-hat-emulator/) (which comes with the Raspian O/S)
- [Sense HAT](https://www.raspberrypi.org/products/sense-hat/) (optional - for those that want to play with real hardware). You can order the Sense HAT from a variety of online sites such as adafruit.com, amazon.com etc. Please order yours 3-4 weeks in advance of the hackathon so it will arrive in time.
- Laptop (running whatever operating system you desire) but ideally running Windows so you can install/run [Device Explorer](https://github.com/Azure/azure-iot-sdks/releases/download/2016-11-17/SetupDeviceExplorer.msi). 
- An Azure subscription. You can create a [free trial](https://azure.microsoft.com/en-us/free/?b=17.01) Azure subscription, or you can use an MSDN Azure subscription or a subscription from your company. 
- A basic understanding of Python and Linux.
- TBD

## Advance Setup (Must be completed in advance of the hackathon)
Please perform the following steps in advance of the hackathon otherwise you will waste the entire hackathon performing these steps.
- Ensure your Raspberry Pi can boot [Raspian] (https://www.raspberrypi.org/downloads/) from the SD card.
- Ensure Sense HAT Emulator is installed (by default it is installed with Raspian). Verify by checking under 'Programming' in the Raspian GUI.
- Install [Device Explorer](https://github.com/Azure/azure-iot-sdks/releases/download/2016-11-17/SetupDeviceExplorer.msi) on your Winbdows laptop. Device Explorer is a great tool to see messages coming into the IoT Hub from your Raspberry Pi. 
- Ensure your Azure subscription login is working and you have sufficient permissions to create resources.
- Download and install [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).

## Steps (Performed by students during hackathon)
1. Connect to Wifi.
  1. Connect your Raspberry Pi to a monitor.
  1. Click on the wifi icon in the top right.
      <p align="center">
        <img src="images/wifi.JPG" />
      </p>
  1. Enter the correct wifi credentials
1. Retrieve the ip address.
  1. Click on the command prompt
      <p align="center">
        <img src="images/CommandPrompt.jpg" /> 
      </p>
  1. Retrieve the ip address with the following command: `arp -a` <br/>
1. Disconnect from the monitor.
1. Using your laptop, verify you connection by connecting to the Rasberry Pi using PuTTY.
1. Setup your Azure IoT Hub.  
  1. Go to the [Azure Portal](https://portal.azure.com).
  1. Select the [IoT Hub Service](https://ms.portal.azure.com/#blade/HubsExtension/Resources/resourceType/Microsoft.Devices%2FIotHubs). 
  1. Click on "Add".
  1. Enter the properties for your IoT Hub.
    1. Enter a name for your hub.  eg. TerrysFirstIoTHub
    1. Choose the "Free" pricing tier.  This will allow you up to 5,000 messages per day.
    1. For the Free tier, the "IoT Hub units" will default to 1.
    1. If you have more than 1 subscription, choose the one you wish to use.
    1. Create a new Resource group for your hub.  It can have the same name as the IoT Hub.
    1. Select the "West US" Location.
    1. Click the "Pin to dashboard" button.
    1. Click the "Create" button.
1. Wait for the hub to be created.  You will be notified in the "Notifications" section when it is complete.  
      <p align="center">
        <img src="images/Notifications.JPG" /> 
      </p>
1. Create (configure) your device in Azure IoT Hub.
  1. Click on your new IoT Hub in the [Azure Portal](https://portal.azure.com) Dashboard.
  1. Click on the "Shared access policies".
  1. Click on the "iothubowner" policy.
  1. Copy the primary key connection string.
      <p align="center">
        <img src="images/IoTHubConnectionString.jpg" /> 
      </p>
  1. Open Device Explorer
  1. In the "Connection information" tab paste the connection string into the "IoT Hub Connection String" text box.
  1. Click on "Update".
  1. Click on the "Management" tab.
  1. In the "Actions" section, select "Create".
  1. Enter a name for your device.
      <p align="center">
        <img src="images/DeviceExplorer.JPG" /> 
      </p>
  1. Save the new device key for later.
  1. Click "Create".
1. Configure the Raspberry Pi to send messages to the IoT Hub.
   1. Copy the [Python code](https://github.com/khilscher/IoTHubPiHackathon/blob/master/SenseHat_IoTHub_Http.py) from this hackathon to a file. Save the file as: SenseHat_IoTHub_Http.py.
   1. Update the file with your device key. <TODO>
   1. Copy the file to your Raspberry Pi using PuTTY.  The pscp executable will be in your PuTTY directory.<br/>
`pscp SenseHat_IoTHub_Http.py userid@server_name:/path/SenseHat_IoTHub_Http.py`
   1. Log into the Raspberry Pi using PuTTY.
   1. Verify that the file was transfered by listing the directory: `ls -l`
   1. Start sending messages by invoking the script in Python
      ```
      pi@raspberrypi:~ $ python SenseHat_IoTHub_Http.py
      ```
   1. Congratulations! Your Raspberry Pi should now be sending data to Azure IoT Hub. 
1. Referring to the [Sense Hat API](https://pythonhosted.org/sense-hat/api/), update the code to send other telemetry to IoT Hub from the Sense HAT. 
1. Update the code to send multiple telemetry data points (e.g. Yaw, Pitch, Roll, or Temperature, Pressure, Humidity) in a single JSON-formatted message to IoT Hub. See [sample_payload.json] (sample_payload.json). Solution source code - Authorized MSFT personnel only [SenseHat_IoTHub_JSON.py](https://microsoft-my.sharepoint.com/personal/kehilsch_microsoft_com/_layouts/15/guestaccess.aspx?guestaccesstoken=sdOEuDcq984383oB3iqDyt2y8wIhqAmXvKQb75V7LUA%3d&docid=2_1c28ea3292574419d932d16dacb6e4204&rev=1).
1. Display the HTTP response code from the IoT Hub message onto the Sense HAT LED display. Solution source code - Authorized MSFT personnel only [SenseHat_IoTHub_JSON_LED.py](https://microsoft-my.sharepoint.com/personal/kehilsch_microsoft_com/_layouts/15/guestaccess.aspx?guestaccesstoken=l%2bcljVkaJf6TEt7CWShh2FmMWnYquyVnnwivcnQ1s7I%3d&docid=2_1b7e74a4df92a4681b60b821fb38bf666&rev=1).

## Using the Python Device SDK
IoT Hub also supports MQTT and AMQP protocols. These are generally more efficient and scale better than using the HTTP REST API. In order to use MQTT or AMQP with Python, you will need to download and compile the Python Device SDK on your Raspian operating system.

The full instructions are [here] (https://github.com/Azure/azure-iot-sdk-python/blob/master/doc/python-devbox-setup.md) with some Python SDK examples [here] (https://github.com/Azure/azure-iot-sdk-python/tree/master/device/samples).

In summary:
- ```git clone --recursive https://github.com/Azure/azure-iot-sdk-python.git```
- ```cd azure-iot-sdk-python/build_all/linux```
- ```sudo ./setup.sh```
- ```sudo ./build.sh```

After a successful build, the ```iothub_client.so``` Python extension module is copied to the device/samples and service/samples folders. The iothub_client.so must be in the same folder as your IoT Hub client python script or in the common shared libraries folder such as ```/usr/local/lib``` or ```/usr/lib```.
