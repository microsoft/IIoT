In the following section of the Hands on Lab, you will walk through the creation of a remote monitoring solution accelerator from the Azure IoT Solutions Accelerator microsite. 
The Remote Monitoring solution accelerator implements an end-to-end monitoring solution for multiple machines in remote locations. The solution combines key Azure services to provide a generic implementation of the business scenario. You can use the solution as a starting point for your own implementation and customize it to meet your own specific business requirements. It includes and by default will provision simulated devices such as trucks, chillers, elevators, engines and others. 

## Create a Remote Monitoring Solution Accelerator
1. Setup your Azure IoT Suite remote monitoring solution accelerator. You will use this solution accelerator for the duration of the labs to help with visualization of the data and other IoT functions. 
  - Go to the Microsoft IoT Solution Accelerators microsite [https://www.azureiotsolutions.com/](https://www.azureiotsolutions.com/).
  - Log in using your Azure subscription credentials. 
  - Click on the "Remote Monitoring Solution" Accelerator.
        ![remote monitoring](/HOL/IOTHubPiHackathon/images/selectRMS.png)
  - Click on "Try Now"
        ![remote monitoring try now](/HOL/IOTHubPiHackathon/images/RemoteMonitoringTryNow.PNG)
  - Fill out the form to create a Remote monitoring solution
    - Enter a name for your remote monitoring solution eg. IoTHandsOnLab-VinnyH. Note that the solution name needs to be globally unique. Once you provide a unique name, a green checkmark will appear to indicate that the solution name is valid. 
    - Choose the subscription that you will be using eg. Visual Studio Enterprise with MSDN
    - Select the closest region to deploy your remote monitoring solution eg. Canada Central
    - Choose the Deployment option you want - either C# or Java
    - Click "Create". The remote monitoring solution will get provisioned to your Azure subscription in approximately 25 minutes. 
       <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/RMPCS2.jpg" width="50%" height="50%" /> 
      </p>
    - Take note of the list of resources that get provisioned as part of the process. At the time of writing this document, the following Azure services get created in the Azure subscription that you specified (and therefore will incur some cost):
      - 1 Azure Active Directory application
      - 1 Virtual Machine (Standard D1 V2 (1 core, 3.5 GB memory))
      - 1 IoT Hub (S1 - Basic tier)
      - 1 Cosmos DB Account (Standard)
      - 1 Storage account (Standard-GRS)
      - 1 Web Application 
      - 1 Azure Maps account (Standard)
      - 1 Azure Stream Analytics (3 streaming units)

   - While the remote monitoring solution is being provisioned, you can see the provisioning state and logging information by clicking on the solution 
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/ProvisioningState2.jpg" /> 
      </p>
   - Once the solution is fully created, it will appear in your list of provisioned solutions showing the "Ready" indicator with a green checkmark or your provisiong status page will show a . It will take about 25 minutes to provision so while you wait for that, feel free to go for a coffee or click on the "Azure activity log" to see the logs that are written during the provisioning process. 
   
   When the provisioning is complete, you will see one of the two following screens:
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/SolutionReady.jpg" width="30%" height="30%" /> 
      </p>
      <BR>
      OR
      <BR>
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/SolutionReady2.jpg" width="50%" height="50%" /> 
      </p>

## Obtain Your IoT Hub Primary Key Connection String

1. Open the [Azure Portal](https://portal.azure.com/) tab and navigate to your IoT Hub service that you deployed as part of the remote monitoring solution
  - Click the *resource group* icon -> click the name of your remote monitoring solution -> click the IoT Hub service that was created when you provisioned the remote monitoring solution. 
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/IoTHubKeys1.jpg" /> 
      </p>
2. Obtain the "Connection string - primary key" for your IoT Hub. <BR>
This is the shared access key that you will use to connect your device to the IoT Hub. Note that since we are using the iothubowner policy, we will be using the policy that provides the device with all permissions - registryWrite, ServiceConnect and DeviceConnect. We do this to simplify the labs but in practice, you should only give your services access to the appropriate permissions. For example, if you are connecting a backend service that will be used to write to the IoT Hub register, you should only grant that particular service the "registryWrite" permission. Details on the permissions are available [here](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-security#iot-hub-permissions).
  Also, note that this is the primary key used by back end services to connect to the IoT Hub. Later in the labs, you will also be using a connection string that is used for individual devices to connect to IoT Hub. Make sure to note the difference. 
  - Click on the "Shared access policies".
  - Click on the "iothubowner" policy.
  - Copy the primary key connection string. Take note of the primary key connection string as you will use it later. To make things easier to capture, you can use the following template to capture all the required variables that you will use throughout this lab: [IoT HOL - Lab Parameters.xlsx](/HOL/IOTHubPiHackathon/IoTHOL-LabParameters.xlsx)
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/IoTHubKeys2.jpg" /> 
      </p>

## Create Consumer Groups
Consumer groups are a key element in Azure event ingestion services that allow consuming applications with a separate view of the event stream. Each consuming application can use the groups to read the streaming data independently at their own pace and with their own offet. For this section of the lab, you will create two new consumer groups that will be used by Azure Stream Analytics as well as the Azure CLI command tool to monitor IoT Hub events. You will create these in advance but won't use them until later in this lab.
1. Under the "Messaging" subsection, select "Endpoints"
2. Click on the "Events" endpoint
3. In the blade that appears on the right, add the following consumer groups.  If multiple people are connecting to the same IoT Hub, append your initials to each of the consumer group names so that each person gets their own consumer groups.
  - "monitor"
  - "asa"
  4. Click save in the top left hand corner of the blade.
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/consumerGroups.jpg" /> 
      </p>

## Create Your Device in the Remote Monitoring Solution Accelerator
1. Go back to the Azure IoT Solution Accelerators microsite tab. Click the "Launch" button on the newly provisioned remote monitoring solution. This will open up a new browser tab to your remote monitoring solution dashboard.
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/SolutionReady.jpg" width="30%" height="30%" /> 
      </p>
2. If the following permissions page showsup, click "Accept". 
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/permissions.jpg" width="50%" height="50%"/> 
      </p>
3. Click the "Sign In" button and provide your corporate credentials if it's requested. 
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/RMSignIn.jpg" width="50%" height="50%"/> 
      </p>
4. You will now have access to your created remote monitoring solution accelerator. Feel free to browse around and review the features available in the solution accelerator. More information on how to navigate and use the features of the remote monitoring solution accelerator are here: https://docs.microsoft.com/en-ca/azure/iot-accelerators/iot-accelerators-remote-monitoring-monitor
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/RMDashboard.jpg"/> 
      </p>

5. Create a new custom device within the IoT Solution Accelerator. 
  - At the top left of the portal in the navigation bar, click the "Devices" button. 
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/RMDashboardwArrow.jpg"/> 
      </p>
  - Click the '+ New Device' button in the top right corner
  - Under device type, select physical. The custom device that you will add is the physical Raspberry Pi. 
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/AddNewCustomDevice.jpg"/> 
      </p>
  - Under Device ID, create a custom Device ID. Enter in a device ID eg. MyRaspberryPi. 
  
  - Leave the Authentication Type as Symmetric Key.<BR>
  (Note: Communication between IoT devices and the IoT Hub can be secured using two methods. In these labs, we will use SAS based tokens but a higher level of security can be provided through the use of X.509 based certificates. See the following for best practices on securing your [IoT Architecture] (https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-security-deployment).
  
  - Select Auto Generate Keys under "Authentication Key".
  
  - Click "Apply".
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/CustomDeviceParams.jpg"/> 
      </p>
     
  - Take note of your Device ID and Connection String, as you will need these later. Feel free to use the parameters template provided earlier.
  - Click "Close"
      
  - As a final step in this part of the lab, you will add a tag that will be used by the app backend to define a property on the device. This tag will be a high temperature limit that will serve as a high temperature threshold that will trigger a message to be sent to your to your physical device later in the lab. 
    - Click the checkbox of the physical device you created. 
    - Click the "Jobs" button.
    <p align="center">
       <img src="/HOL/IOTHubPiHackathon/images/twinTag1.jpg" /> 
    </p>
    
    - Keep the "Tag" radio button selected under the "Select job" header.
    - Provide the job a name. eg. SetHighTemp
    - Click "+ Add Tag".
    
    - Add a new parameter "HighTemperatureLimit" under the "KEY" header.  Set the value to 40 and make it of data type "Number".
    
    - Click " Apply ".
    
    <p align="center">
      <img src="/HOL/IOTHubPiHackathon/images/twinTag2.jpg" width="70%" height="70%" /> 
    </p>
  -The job will be submitted and you should see a "job submitted successfully" message. This action will queue up a job in the IoT Hub job queue until the RaspberryPi device that you will setup later connects into the IoT Hub.  

Congratulations! You have successfully spun up your Solution Accelerator and created a new custom device that you will configure in the next section of the labs! 

[Next lab - 3 Connect your Raspberry Pi to IoT Hub](/HOL/IOTHubPiHackathon/3)

[Back to Main HOL Instructions](/HOL/IOTHubPiHackathon/README.md)
