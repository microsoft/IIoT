In the following section of the Hands on Lab, you will walk through the creation of a remote monitoring pre-configured solution from the Azure IoT Suite microsite. 

## Create a Remote Monitoring Pre-configured Solution
1. Setup your Azure IoT Suite remote monitoring pre-configured solution. You will use this pre-configured solution for the duration of the labs to help with visualization of the data and other IoT functions. 
  - Go to the Microsoft IoT Suite microsite [https://www.azureiotsuite.com/](https://www.azureiotsuite.com/).
  - Log in using your Azure subscription credentials. 
  - Click the "Create a new solution" button. 
        <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/NewRMPCS.png" /> 
      </p>
  - Select "Remote monitoring".
        <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/SelectRM.jpg" width="50%" height="50%" /> 
      </p>
  - Fill out the form to create a Remote monitoring solution
    - Enter a name for your remote monitoring solution eg. IoTHandsOnLab-VinnyH. Note that the solution name needs to be globally unique. Once you provide a unique name, a green checkmark will appear to indicate that the solution name is valid. 
    - Choose the subscription that you will be using eg. Visual Studio Enterprise with MSDN
    - Click "I Accept" 
    - Select the closest region to deploy your remote monitoring solution eg. East US
    - Click "Create solution". The remote monitoring solution will get provisioned to your Azure subscription in approximately 5 minutes. 
       <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/RMPCS.jpg" width="50%" height="50%" /> 
      </p>
   - While the remote monitoring solution is being provisioned, you can see the provisioning state and logging information by clicking on the solution 
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/ProvisioningState.jpg" /> 
      </p>
   - Once the solution is fully created, it will appear in your list of provisioned solutions showing the "Ready" indicator with a green checkmark. It will take about 5 minutes to provision so while you wait for that, continue with the steps below. 
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/SolutionReady.jpg" width="30%" height="30%" /> 
      </p>

## (Optional) Enabling Interactive Bing Maps in the Pre-configured Solution 

The new version of the remote monitoring pre-configured solution comes with a static Bing map image configured by default. For this hands on lab, we won't be making use of the interactive maps but if interested, instructions on how to enable it is available [here](/HOL/IOTHubPiHackathon/OptionalLabs/DynamicMaps.md)


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
3. In the blade that appears on the right, add the following consumer groups.  If multiple people are connecting to the same IoT Hub, append your initials to each of the consumer group names so that each person gets their own groups.
  - "deviceexplorer"
  - "asa"
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/consumerGroups.jpg" /> 
      </p>

## Create Your Device in the Remote Monitoring Pre-configured Solution 
1. Go back to the Azure IoT Suite microsite tab. Your pre-configured solution should be provisioned now. Click the "Launch" button on the newly provisioned remote monitoring solution. This will open up a new browser tab to your remote monitoring solution dashboard.
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/SolutionReady.jpg" width="30%" height="30%" /> 
      </p>
2. Click the "Sign In" button.
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/RMSignIn.jpg" width="50%" height="50%"/> 
      </p>
3. If the following page requires you to accept the terms and conditions, click "I Agree". 
4. You will now have access to your created remote monitoring preconfigured solution. Feel free to browse around and review the features available in the pre-configured solution. 
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/RMDashboard.jpg"/> 
      </p>

5. Create a new custom device within the RM-PCS. 
  - At the bottom left of the portal, click the "+ Add A Device" button. 
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/AddDevice.jpg"/> 
      </p>
  - On the "Step 1 of 3" page, click "Add New" to add in a custom device. The custom device that you will add is the physical Raspberry Pi. 
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/AddNewCustomDevice.jpg"/> 
      </p>
  - On the "Step 2 of 3" page, click the "Let me define my own Device ID" radio button. Enter in a device ID eg. MyRaspberryPi. Click on the "Check ID" button to ensure that your device ID is unique. If the Device ID is unique, the text "Device ID is available" in green text will appear. Click the "Create" button. 
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/DefineDeviceID.jpg"/> 
      </p>
  - The "Step 3 of 3" page provides you the *Device ID*, *IoT Hub Hostname* and *Device Key* that you will need to connect your Raspberry Pi to the remote monitoring solution. Take note of the value of these fields. Feel free to use the parameters template provided earlier.  
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/CustomDeviceParams.jpg"/> 
      </p>
      
  - As a final step in this lab, add a high temperature limit to the device twin.  We will use this later in the lab.
    - Click on the device you created. 
    - Under "Device Twin", in the "Tags" category, click "Edit".
    <p align="center">
       <img src="/HOL/IOTHubPiHackathon/images/twinTag1.jpg" /> 
    </p>
    - Click "+ Add Tag".
    - Add a new parameter "tags.HighTemperatureLimit" under "TAGS".  Set it to 40 and make it of data type "Number".
    - Click "Save Changes to Device Twin".
    <p align="center">
      <img src="/HOL/IOTHubPiHackathon/images/twinTag2.jpg" width="70%" height="70%" /> 
    </p>

Congratulations! You have successfully spun up your Remote Monitoring Pre-configured (RM-PCS) solution and created a new custom device that you will configure in the next section of the labs! 

[Next lab - 3 Connect your Raspberry Pi to IoT Hub](/HOL/IOTHubPiHackathon/3)

[Back to Main HOL Instructions](/HOL/IOTHubPiHackathon/README.md)
