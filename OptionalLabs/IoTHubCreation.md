
-------- Steps using IoT Hub only -----
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
  1. Copy the primary key connection string. Save the primary key connection string for later.
      <p align="center">
        <img src="images/IoTHubConnectionString.jpg" /> 
      </p>
  1. Open Device Explorer
  1. In the "Connection information" tab paste the primary key connection string into the "IoT Hub Connection String" text box.
  1. Click on "Update".
  1. Click on the "Management" tab.
  1. In the "Actions" section, select "Create".
  1. Enter a name for your device. Save the device name for later.
      <p align="center">
        <img src="images/DeviceExplorer.JPG" /> 
      </p>
  1. Click "Create".
1. Configure the Raspberry Pi to send messages to the IoT Hub.
  1. Copy the [Python code](https://github.com/khilscher/IoTHubPiHackathon/blob/master/SenseHat_IoTHub_Http.py) from this HOL to a file. Save the file as ```SenseHat_IoTHub_Http.py``` and open it with a text editor such as Notepad.
    1. Alternatively you can download the file directly to your Raspberry Pi using: ```git clone https://github.com/khilscher/IoTHubPiHackathon.git``` and edit the ```SenseHat_IoTHub_Http.py``` using a text editor such as Nano.
  1. Update the file with the primary key connection string. Look for ```connectionString =``` and paste in the primary key connection string you copied earlier. Then look for ```deviceId =``` and paste in the Device Name you created earlier.
  1. Copy ```SenseHat_IoTHub_Http.py``` to your Raspberry Pi using PuTTY.  The pscp executable will be in your PuTTY directory.<br/>
`pscp SenseHat_IoTHub_Http.py userid@server_name:/path/SenseHat_IoTHub_Http.py`
  1. Log into the Raspberry Pi using PuTTY.
  1. Verify that the file was transfered by listing the directory: `ls -l`
  1. Start sending messages by invoking the script in Python
      ```
      pi@raspberrypi:~ $ python SenseHat_IoTHub_Http.py
      ```
  1. On your laptop, open Device Explorer, click the Data tab, select your device from the Device ID list, and click Monitor. If you see messages arriving then Congratulations, your Raspberry Pi is now sending data to Azure IoT Hub. 
1. Referring to the [Sense Hat API](https://pythonhosted.org/sense-hat/api/), update the code to send other telemetry to IoT Hub from the Sense HAT. 
  1. Update the ```SenseHat_IoTHub_Http.py``` code to send multiple telemetry data points (e.g. Yaw, Pitch, Roll, or Temperature, Pressure, Humidity) in a single JSON-formatted message to IoT Hub. See [sample_payload.json] (sample_payload.json). Solution source code - Authorized MSFT personnel only [SenseHat_IoTHub_Http_JSON.py](https://kevinhilscher.visualstudio.com/_git/IoT%20Hackathon?path=%2FSenseHat_IoTHub_Http_JSON.py&version=GBmaster&_a=contents).
  1. Update ```SenseHat_IoTHub_Http.py``` to display the HTTP response code from the IoT Hub message onto the Sense HAT LED display. Solution source code - Authorized MSFT personnel only [SenseHat_IoTHub_Http_JSON_LED.py](https://kevinhilscher.visualstudio.com/_git/IoT%20Hackathon?path=%2FSenseHat_IoTHub_Http_JSON%20_LED.py&version=GBmaster&_a=contents).
1. To send messages from IoT Hub back to your Raspberry Pi:
  1. Copy the ```SenseHat_IoTHub_Http_C2D_LED.py``` file to your Raspberry Pi using pscp or download it directly using git clone.
  1. Update the file with the primary key connection string. Look for ```connectionString =``` and paste in the primary key connection string you copied earlier. Then look for ```deviceId =``` and paste in the Device Name you created earlier. Save the file.
  1. Run the file using ```pi@raspberrypi:~ $ python SenseHat_IoTHub_Http_C2D_LED.py```
  1. On your laptop, open Device Explorer, click the Messages to Device tab, select your device from the Device ID list, type in a message into the Message textbox and click Send. You should see the message appear on the Sense HAT LED display.


[Back to Main HOL Instructions](/README.md)
