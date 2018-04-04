## Connect Your Raspberry Pi to the IoT Hub

In this lab, you will configure your Raspberry Pi to connect to the IoT solution that you created earlier. You will create a small application on your Raspberry Pi (python script) to send a D2C (Device to Cloud) message to the IoT Hub and also modify that such that the application can be used to receive a C2D (Cloud to Device) message that will be displayed on the Sense HAT or the Sense HAT emulator. The python script is a sample that will interact with the Sense HAT to collect telemetry data (temperature, humidity, pitch, yaw, roll) from the device. It will also contain code that will securely connect the Raspberry Pi to Azure IoT Hub and allow bidirectional communication to it. 

1. Configure the Raspberry Pi to send messages to the IoT Hub.
  - Copy the [Python code](/HOL/IOTHubPiHackathon/SenseHat_IoTHub_Http_Lab_Key.py) from this HOL to a text editor (eg. Notepad) on your laptop. Save the file as ```SenseHat_IoTHub_Http_Lab_Key.py```.
  - Alternatively, you can download the file directly to your Raspberry Pi using: ```git clone https://github.com/Microsoft/IIoT.git``` and edit the ```SenseHat_IoTHub_Http_Lab_Key.py``` using a text editor (eg. Nano) on your Raspberry Pi.
  - Comment/uncomment the *import* statements that correspond to whether you are using a Sense HAT or the Sense Hat emulator. 
     Below the import statements, you will see:
     
     ``` from sense_hat import SenseHat #if using a physical SenseHat attached to Raspi``` <br/>
     ``` #from sense_emu import SenseHat #if using a Sense HAT Emulator (Linux only) ```
         
     - if you are using the physical Sense HAT, uncomment the *from sense_hat* statement and comment the *from sense_emu* statement. To comment a statement, use the '#' character in front of the text that you are trying to comment. To uncomment, remove the '#' character. 
     - if using the Sense HAT emulator, comment the *from sense_hat* and uncomment the *from sense_emu* statement

  - Next, you will provide the information required to connect your device - the Raspberry Pi to the IoT pre-configured solution:
    - Update the file with the primary key connection string. Look for ```connectionString = ''``` and paste in the IoT Hub "Connection string - primary key" you noted earlier. (Azure Portal -> IoT Hub -> Shared access policies -> iothubowner -> Connection string-primary key)
    - Search for ```deviceId = ''``` and paste in the Device ID you created earlier.
  - If you are editing the file on a laptop and not on the Raspberrry PI, copy ```SenseHat_IoTHub_Http_Lab_Key.py``` to your Raspberry Pi using pscp (or some other secure client to copy files). 
    - If you installed PuTTY using the default settings, the PuTTY environment variables should be set in your PATH already and you should be able to run psp from any path. Otherwise, the pscp executable will be in your PuTTY directory. <br/>
    
      Open up a command prompt on **your local machine/laptop** and enter the following command to copy the python script to your Raspberry Pi. If you didn't change the username/password, it should be ***pi/raspberry*** <br/>

      `pscp SenseHat_IoTHub_Http_Lab_Key.py <userid>@<server ip or server name>:/<$path>/SenseHat_IoTHub_Http_Lab_Key.py`

      (replace the \<userid\> text with your Raspberry Pi Username. The default username on Raspbian is "pi") <BR>
      (replace \<server ip or server name\> with the Raspbery Pi's IP address) <BR>
      (for the \<$path\>, use */home/pi*)  <BR>

      As an example, if your RaspberryPi has an IP of 192.168.1.1, the command you will run is: 
'pscp SenseHat_IoTHub_Http_Lab_Key.py pi@192.168.1.1:/home/pi'

    - Log into the Raspberry Pi using PuTTY.
    - Verify that the file was transfered by listing the directory: `ls -l`
  
     ![ls -l](/HOL/IOTHubPiHackathon/images/ListFiles.jpg)
  
  - If you are using the Sense HAT Emulator, start it now (Open a VNC session to the Raspberry Pi: Start -> Programming -> Sense HAT emulator)
  - Start sending messages by invoking the script in Python<br/>
      ```
      pi@raspberrypi:~ $ python SenseHat_IoTHub_Http_Lab_Key.py
      ```
  - Next we use iothub-explorer to view our incoming telemetry and send messages to our device via the IoT Hub.  To start, login using the following command:
      ```
      iothub-explorer login "<iothubowner connection-string>"
      ```
      
      (Make sure to replace the \<iothubowner connection-string\> text with the actual connection string that you obtained previously. <BR>
  The connection string should be in the format HostName=*URL*;SharedAccessKeyName=iothubowner;SharedAccessKey=*key*)
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/IoTHubExplorerLogin.JPG" width="100%" height="100%" /> 
      </p>
  - To view the IoT Hub attributes of your device, enter the following:
      ```
      iothub-explorer get <device name> --<iothubowner connection-string>
      ```
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/IoTHubExplorerGet.JPG" width="100%" height="100%" /> 
      </p>
  - To view telemetry coming in from your Raspberry Pi into the ioT Hub, enter the following. Use double quotes for Windows, and single quotes for Linux.
      ```
      iothub-explorer monitor-events <device name> --login "<iothubowner connection-string>" --consumer-group "deviceexplorer"
      ```
  <BR>
    (Note: the consumer group *deviceexplorer* was created in the previous lab. This consumer group provides you with the ability to consume from the event stream using multiple consumers, enabling those consumers to act independently)
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/IoTHubExplorerMonitor.JPG" width="100%" height="100%" /> 
      </p>
    
  - To send a message to your Raspberry PI via the IoT Hub, enter the following:
      ```
      iothub-explorer send <device name> Hello --ack=full
      ```
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/IoTHubExplorerSend.JPG" width="100%" height="100%" /> 
      </p>  
      
    - On your Sense HAT, you should see the message appear on the display. (if you are using the Sense HAT emulator, you will need to VNC to your Raspberry Pi and open the Sense HAT Emulator application: Menu -> Programming -> Sense HAT Emulator) <br />
    ![Sense HAT Message Display](/HOL/IOTHubPiHackathon/images/SenseMsgDisplay.jpg)
  

Congratulations! You just connected your Raspberry Pi to the IoT hub and created an application which demonstrated the two-way messaging capabilities. 
<!--
## Hands-On assignment.  

In this assignment, you will use your Python skills to alter the code to send the following additional sensor telemetry to the IoT Hub in JSON format:
  - Pitch
  - Yaw
  - Roll
  - Humidity
  - Temperature

### Tips: 
- You can refer to the [Sense Hat API](https://pythonhosted.org/sense-hat/api/) for information on how to update the code to send other telemetry to IoT Hub from the Sense HAT. 

- Update the ```SenseHat_IoTHub_Http_Lab_Key.py``` code to send multiple telemetry data points (e.g. Yaw, Pitch, Roll, or Temperature, Pressure, Humidity) in a single JSON-formatted message to IoT Hub. See [sample_payload.json] (/HOL/IoTHubPiHackathon/blob/master/sample_payload.json) for an example of the type of message to be sent. 
<p align="center">
  <img src="/HOL/IOTHubPiHackathon/images/DeviceExplorer-ReceiveEvents.jpg" width="50%" height="50%" /> 
</p>
   
- Once you have updated and run your code, go to the remote monitoring pre-configured solution dashboard and take a look at the new telemetry data points that are being plotted on the Telemetry History chart. 
-->
<!--
The finished script for this assignnment can be found [here](https://github.com/khilscher/IoTHubPiHackathon/blob/master/SenseHat_IoTHub_Http_Lab_Key.py).  If you use this script, remember to update the file with your IoT Hub connection string and the Device Id. 
-->

Finished early?  Try this [advanced tutorial](/HOL/IOTHubPiHackathon/3/Advanced.md)


[Next lab - 4a Route Telemetry to PowerBI](/HOL/IOTHubPiHackathon/StreamAnalytics)
OR
[Next lab - 4b Route Telemetry to Blob Storage](/HOL/IOTHubPiHackathon/BlobStorage)

[Back to Main HOL Instructions](/HOL/IOTHubPiHackathon/README.md)
