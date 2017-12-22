## Hands on Lab - Initial Setup

These steps will be performed in the morning before the workshop starts. You will need to walk through each of the following steps to make sure that you can connect your Raspberry Pi to the local WiFi as well as ensure the requisite tools are installed and enabled. 

1. Turn on your Raspberry Pi and connect to Wifi.
  - Connect your Raspberry Pi to a monitor.
  - Click on the wifi icon in the top right.
      <p align="center">
        <img src="/HOL/IOTHubPiHackathon/images/wifi.JPG" />
      </p>
  - Enter the correct wifi credentials
2. Retrieve the IP address.
  - Click on the command prompt
      <p align="center">
        <img src="/HOL/IOTHubPiHackathon/images/CommandPrompt.jpg" /> 
      </p>
  - Retrieve the IP address with the following command: `ifconfig` <br>
     Take note of the IP address and use the following [template](/HOL/IOTHubPiHackathon/IoTHOL-LabParameters.xlsx) to track the configuration details that you will collect over the course of the lab. 
3. If you didn't enable SSH on your Raspberry Pi previously, follow the steps in the [Pre-lab Steps instructions](/HOL/IOTHubPiHackathon/Prep). <br><br>
4. If using a laptop, connect to your Raspberry Pi using your laptop to verify the connection. 
  - Open PuTTY. 
  - Enter the IP address of your Raspberry Pi into the *Host Name (or IP address)* field. 
      <p align="center">
        <img src="/HOL/IOTHubPiHackathon/images/PuTTY.jpg" />
      </p>
  - If you get prompted to accept a security certificate, click "Yes". 
5. Disconnect from the monitor.


[Back to Main HOL Instructions](/HOL/IOTHubPiHackathon/README.md)
