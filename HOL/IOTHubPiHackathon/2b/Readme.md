In the following section of the Hands on Lab, you will walk through provisioning an IoT Hub service from the Azure portal. 

## Create an IoT Hub
1. Open the [Azure Portal](https://portal.azure.com/).
1. Click "Create a resource" in the top left of the portal.
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/CreateAResource.JPG" /> 
      </p>
1. Type "IoT Hub" in the search, and choose "IoT Hub"
1. Click on the "Create" button.
1. Enter the details for your Hub:
   1. Name.  A globally unique name for your IoT Hub.  eg. my initials are "TM", so "TMIoTHub"
   1. Pricing and scale tier.  Choose the "F1" free tier.  This will give you 8,000 free messages per day.
   1. Subscription.  Choose a subscription you have permissions to create services in.
   1. Resource group.  Choose "Create new", then enter a globally unique name for your resource group.  eg. "TMResourceGroup"
   1. Location.  Choose a data center that is near your physical location.  eg. "West US"
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/IoTHubParams.JPG" /> 
      </p>   
   1. Click on "Create".
   1. Watch the notifications to see when your IoT Hub has been created.  (should be less than a minute)
      
## Obtain Your IoT Hub Primary Key and Connection String
1. Open the [Azure Portal](https://portal.azure.com/) tab and navigate to your IoT Hub service that you provisioned above
  - Click the *resource group* icon -> click the name of the resource group you created above -> click the IoT Hub service
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/ResourceGroupForIoTHub.JPG" /> 
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
3. Click "Save"

## Create A Device

Now we will configure a device in the IoT Hub for your Raspberry Pi.
1. Under "Explorers", choose "IoT Devices"
1. Click "+ Add"
1. Enter the parameters for your device:
   1. Device ID.  This is a name for your device.  It needs to be unique in the IoT Hub.  eg. TMDevice
   1. Authentication Type.  Choose "Symmetric Key"
   1. Check "Auto Generate Keys"
   1. Select "Enable" for "Connect Device to IoT Hub"
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/IoTHubParams.JPG" /> 
      </p>
   1. Click on Save
   
Congratulations! You have successfully spun up an IoT Hub and created a new custom device that you will configure in the next section of the labs! 

[Back to Main HOL Instructions](/HOL/IOTHubPiHackathon/README.md)
