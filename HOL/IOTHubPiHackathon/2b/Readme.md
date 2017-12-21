

## Obtain Your IoT Hub Primary Key and Connection String
1. Open the [Azure Portal](https://portal.azure.com/) tab and navigate to your IoT Hub service that you deployed as part of the remote monitoring solution
  - Click the *resource group* icon -> click the name of your remote monitoring solution -> click the IoT Hub service that was created when you provisioned the remote monitoring solution. 
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/IoTHubKeys1.jpg" /> 
      </p>
2. Obtain the "Connection string - primary key" for your IoT Hub. <BR>
This is the shared access key that you will use to connect your device to the IoT Hub. The key provides the device with all permissions - registryWrite, ServiceConnect and DeviceConnect. Details on the permissions are available [here](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-security#iot-hub-permissions)
  - Click on the "Shared access policies".
  - Click on the "iothubowner" policy.
  - Copy the primary key connection string. Take note of the primary key connection string for later. You can use the following template to capture all the required variables for this lab: [IoT HOL - Lab Parameters.xlsx](/HOL/IOTHubPiHackathon/IoTHOL-LabParameters.xlsx)
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/IoTHubKeys2.jpg" /> 
      </p>

## Create Consumer Groups
Consumer groups are a key element in Azure event ingestion services that allow consuming applications with a separate view of the event stream. Each consuming application can use the groups to read the streaming data independently at their own pace and with their own offet. These consumer groups will be created in advance but will be used later in this lab.
1. Under the "Messaging" subsection, select "Endpoints"
2. Click on the "Events" endpoint
3. In the blade that appears on the right, add the following consumer groups:
  - "deviceexplorer"
  - "asa"
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/consumerGroups.jpg" /> 
      </p>
