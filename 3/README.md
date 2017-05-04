## Connect Your Raspberry Pi to the Remote Monitoring Pre-configured Solution

In this lab, you will configure your Raspberry Pi to connect to the IoT solution that you created earlier. You will create a small application on your Raspberry Pi (python script) to send a D2C (Device to Cloud) message to the IoT Hub and also create another application to receive a C2D (Cloud to Device) message that will be displayed on the Sense HAT or the Sense HAT emulator. 

1. Configure the Raspberry Pi to send messages to the IoT Hub.
  1. Copy the [Python code](https://github.com/khilscher/IoTHubPiHackathon/blob/master/SenseHat_IoTHub_Http_Lab.py) from this HOL to a file. Save the file as ```SenseHat_IoTHub_Http_Lab.py``` and open it with a text editor such as Notepad.
  1. Alternatively you can download the file directly to your Raspberry Pi using: ```git clone https://github.com/khilscher/IoTHubPiHackathon.git``` and edit the ```SenseHat_IoTHub_Http_Lab.py``` using a text editor such as Nano.
  1. Comment/uncomment the *import* statements that correspond to whether you are using a Sense HAT or the Sense Hat emulator. 
     Below the import statements, you will see:
     
     ``` #from sense_hat import SenseHat #if using a physical SenseHat attached to Raspi``` <br/>
     ``` from sense_emu import SenseHat #if using a Sense HAT Emulator (Linux only) ```
         
     - if using the Sense HAT, uncomment the *from sense_hat* statement and comment the *from sense_emu* statement
     - if using the Sense HAT emulator, comment the *from sense_hat* and uncomment the *from sense_emu* statement

  1. Next, you will provide the information required to connect the Raspberry Pi to the IoT pre-configured solution:
    - Update the file with the primary key connection string. Look for ```connectionString =``` and paste in the IoT Hub "Connection string - primary key" you noted earlier. (Azure Portal -> IoT Hub -> iothubowner -> Connection string-primary key)
    - Search for ```deviceId =``` and paste in the Device ID you created earlier.
  1. Copy ```SenseHat_IoTHub_Http_Lab.py``` to your Raspberry Pi using PuTTY. 
    - If you installed PuTTY using the default settings, the PuTTY environment variables should be set in your PATH already. Otherwise, the pscp executable will be in your PuTTY directory.<br/>
    
Open up a command prompt on **your local machine** and enter the following command to copy the python script to your Raspberry Pi. If you didn't change the username/password, it should be pi/raspberry <br/>

`pscp SenseHat_IoTHub_Http_Lab.py <userid>@<server ip or server name>:/<$path>/SenseHat_IoTHub_Http_Lab.py`

(for the <$path>, use */home/pi*)

  1. Log into the Raspberry Pi using PuTTY.
  1. Verify that the file was transfered by listing the directory: `ls -l`
  
  ![ls -l](/images/ListFiles.jpg)
  
  1. Start sending messages by invoking the script in Python<br/> (if you are using the Sense HAT emulator, start the emulator in your VNC session: start -> programming -> Sense HAT emulator)
      ```
      pi@raspberrypi:~ $ python SenseHat_IoTHub_Http_Lab.py
      ```
  1. Connect your Device Explorer to the IoT Hub and check to see if messages are arriving at the IoT Hub:
    - On your laptop, open Device Explorer. Under the Configuration tab, copy and paste the IoT Hub Connection String obtained earlier and click "Update". This connects the Device Explorer app to the IoT Hub that you created. 
    
      <p align="center">
         <img src="/images/DeviceExplorer-Connect.jpg" width="50%" height="50%" /> 
      </p>
      
    - Click the Data tab, select your device from the Device ID list, click the "enable" checkbox beside the *Consumer Group* field, enter "deviceexplorer" in the "Consumer Group" text box, and click "Monitor". If you see messages arriving then Congratulations, your Raspberry Pi is now sending data to Azure IoT Hub. 
  
      <p align="center">
         <img src="/images/DeviceExplorer-ReceiveData.jpg" width="50%" height="50%" /> 
      </p>
  1. To send messages from IoT Hub back to your Raspberry Pi:
    1. On your laptop, open Device Explorer, click the Messages to Device tab, select your device from the Device ID list, type in a message into the Message textbox and click Send. <br />
    ![Send Message](/images/SendMsg-DvcExplorer.jpg) 
    1. On your Sense HAT, you should see the message appear on the display. (if you are using the Sense HAT emulator, you will need to VNC to your Raspberry Pi and open the Sense HAT Emulator application: Menu -> Programming -> Sense HAT Emulator) <br />
    ![Sense HAT Message Display](/images/SenseMsgDisplay.jpg)
  

Congratulations! You just connected your Raspberry Pi to the IoT hub and created an application which demonstrated the two-way messaging capabilities. 

## Hands-On assignment.  

In this assignment, you will use your Python skills to alter the code to send the following additional sensor telemetry to the IoT Hub in JSON format:
  - Pitch
  - Yaw
  - Roll
  - Humidity
  - Temperature

### Tips: 
- You can refer to the [Sense Hat API](https://pythonhosted.org/sense-hat/api/) for information on how to update the code to send other telemetry to IoT Hub from the Sense HAT. 

- Update the ```SenseHat_IoTHub_Http_Lab_Key.py``` code to send multiple telemetry data points (e.g. Yaw, Pitch, Roll, or Temperature, Pressure, Humidity) in a single JSON-formatted message to IoT Hub. See [sample_payload.json] (https://github.com/khilscher/IoTHubPiHackathon/blob/master/sample_payload.json) for an example of the type of message to be sent. 
<p align="center">
  <img src="/images/DeviceExplorer-ReceiveEvents.jpg" width="50%" height="50%" /> 
</p>
   
- Once you have updated and run your code, go to the remote monitoring pre-configured solution dashboard and take a look at the new telemetry data points that are being plotted on the Telemetry History chart. 

<!--
The finished script for this assignnment can be found [here](https://github.com/khilscher/IoTHubPiHackathon/blob/master/SenseHat_IoTHub_Http_Lab_Key.py).  If you use this script, remember to update the file with your IoT Hub connection string and the Device Id. 
-->

Finished early?  Try this [advanced tutorial](https://github.com/khilscher/IoTHubPiHackathon/blob/master/3/Advanced.md)

[Back to Main HOL Instructions](/README.md)
