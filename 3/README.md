## Connect Your Raspberry Pi to the Remote Monitoring Pre-configured Solution

In this lab, you will configure your Raspberry Pi to connect to the IoT solution that you created earlier. You will create a small application on your Raspberry Pi (python script) to send a D2C (Device to Cloud) message to the IoT Hub and also create another application to receive a C2D (Cloud to Device) message that will be displayed on the Sense HAT or the Sense HAT emulator. 

1. Configure the Raspberry Pi to send messages to the IoT Hub.
  1. Copy the [Python code](https://github.com/khilscher/IoTHubPiHackathon/blob/master/SenseHat_IoTHub_Http_Lab.py) from this HOL to a file. Save the file as ```SenseHat_IoTHub_Http_Lab.py``` and open it with a text editor such as Notepad.
  1. Alternatively you can download the file directly to your Raspberry Pi using: ```git clone https://github.com/khilscher/IoTHubPiHackathon.git``` and edit the ```SenseHat_IoTHub_Http_Lab.py``` using a text editor such as Nano.
  1. Next, you will provide the information required to connect the Raspberry Pi to the IoT pre-configured solution:
  - Update the file with the primary key connection string. Look for ```connectionString =``` and paste in the primary key connection string you copied earlier. 
  - Search for ```deviceId =``` and paste in the Device ID you created earlier.
  1. Copy ```SenseHat_IoTHub_Http_Lab.py``` to your Raspberry Pi using PuTTY. 
  - If you installed PuTTY using the default settings, the PuTTY environment variables should be set in your PATH already. Otherwise, the pscp executable will be in your PuTTY directory.<br/>
Open up a command prompt and enter the following command to copy the python script to your Raspberry Pi. If you didn't change the username/password, it should be pi/raspberry <br/>
`pscp SenseHat_IoTHub_Http_Lab.py userid@server_name:/path/SenseHat_IoTHub_Http_Lab.py`
  1. Log into the Raspberry Pi using PuTTY.
  1. Verify that the file was transfered by listing the directory: `ls -l`
  
  ![ls -l](/images/ListFiles.jpg)
  
  1. Start sending messages by invoking the script in Python
      ```
      pi@raspberrypi:~ $ python SenseHat_IoTHub_Http_Lab.py
      ```
  1. On your laptop, open Device Explorer, click the Data tab, select your device from the Device ID list, and click *Monitor*. If you see messages arriving then Congratulations, your Raspberry Pi is now sending data to Azure IoT Hub. 
  
  ![Device Explorer](/images/DeviceExplorer-ReceiveEvents.jpg)

***** ---- TERRY to fill out steps students should follow below -------- ********

1. Referring to the [Sense Hat API](https://pythonhosted.org/sense-hat/api/), update the code to send other telemetry to IoT Hub from the Sense HAT. 
  1. Update the ```SenseHat_IoTHub_Http_Lab.py``` code to send multiple telemetry data points (e.g. Yaw, Pitch, Roll, or Temperature, Pressure, Humidity) in a single JSON-formatted message to IoT Hub. See [sample_payload.json] (sample_payload.json). Solution source code - Authorized MSFT personnel only [SenseHat_IoTHub_Http_JSON.py](https://kevinhilscher.visualstudio.com/_git/IoT%20Hackathon?path=%2FSenseHat_IoTHub_Http_JSON.py&version=GBmaster&_a=contents).
  1. Update ```SenseHat_IoTHub_Http_Lab.py``` to display the HTTP response code from the IoT Hub message onto the Sense HAT LED display. Solution source code - Authorized MSFT personnel only [SenseHat_IoTHub_Http_JSON_LED.py](https://kevinhilscher.visualstudio.com/_git/IoT%20Hackathon?path=%2FSenseHat_IoTHub_Http_JSON%20_LED.py&version=GBmaster&_a=contents).
1. To send messages from IoT Hub back to your Raspberry Pi:
  1. Copy the ```SenseHat_IoTHub_Http_C2D_LED.py``` file to your Raspberry Pi using pscp or download it directly using git clone.
  1. Update the file with the primary key connection string. Look for ```connectionString =``` and paste in the primary key connection string you copied earlier. Then look for ```deviceId =``` and paste in the Device Name you created earlier. Save the file.
  1. Run the file using ```pi@raspberrypi:~ $ python SenseHat_IoTHub_Http_C2D_LED.py```
  
  ![Run C2D Python Script](/images/runC2D.jpg)
  
  1. On your laptop, open Device Explorer, click the Messages to Device tab, select your device from the Device ID list, type in a message into the Message textbox and click Send. 
  
  ![Send Message](/images/SendMsg-DvcExplorer.jpg) 
  
  1. On your Sense HAT, you should see the message appear on the display. (if you are using the Sense HAT emulator, you will need to VNC to your Raspberry Pi and open the Sense HAT Emulator application: Menu -> Programming -> Sense HAT Emulator)
  
  ![Sense HAT Message Display](/images/SenseMsgDisplay.jpg)

[Back to Main HOL Instructions](/README.md)
