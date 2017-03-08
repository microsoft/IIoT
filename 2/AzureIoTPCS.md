In the following section of the Hands on Lab, you will walk through the creation of a remote monitoring pre-configured solution from the Azure IoT Suite microsite. 

## Create a Remote Monitoring Pre-configured Solution
1. Setup your Azure IoT Suite remote monitoring pre-configured solution
  1. Go to the Microsoft IoT Suite microsite [https://www.azureiotsuite.com/](https://www.azureiotsuite.com/).
  1. Log in using your Azure subscription credentials. 
  1. Click the "Create a new solution" button. 
        <p align="center">
         <img src="/images/NewRMPCS.jpg" /> 
      </p>
  1. Select "Remote monitoring".
        <p align="center">
         <img src="/images/SelectRM.jpg" width="50%" height="50%" /> 
      </p>
  1. Fill out the form to create a Remote monitoring solution
    - Enter a name for your remote monitoring solution eg. IoTHandsOnLab-VinnyH. Note that the solution name needs to be globally unique. Once you provide a unique name, a green checkmark will appear to indicate that the solution name is valid. 
    - Choose the subscription that you will be using eg. Visual Studio Enterprise with MSDN
    - Click "I Accept" 
    - Select the closest region to deploy your remote monitoring solution eg. East US
    - Click "Create solution". The remote monitoring solution will get provisioned to your Azure subscription in approximately 5 minutes. 
       <p align="center">
         <img src="/images/RMPCS.jpg" width="50%" height="50%" /> 
      </p>
   1. While the remote monitoring solution is being provisioned, you can see the provisioning state and logging information by clicking on the solution 
      <p align="center">
         <img src="/images/ProvisioningState.jpg" /> 
      </p>
   1. Once the solution is fully created, it will appear in your list of provisioned solutions showing the "Ready" indicator with a green checkmark. It will take about 5 minutes to provision so while you wait for that, continue with the steps below. 
      <p align="center">
         <img src="/images/SolutionReady.jpg" width="30%" height="30%" /> 
      </p>

## (Optional) Enabling Interactive Bing Maps in the Pre-configured Solution 

The new version of the remote monitoring pre-configured solution comes with a static Bing map image configured by default. For this hands on lab, we won't be making use of the interactive maps but if interested, instructions on how to enable it is available [here](/OptionalLabs/DynamicMaps.md)


## Obtain Your IoT Hub Primary Key and Connection String
1. Open the [Azure Portal](https://portal.azure.com/) tab and navigate to your IoT Hub service that you deployed as part of the remote monitoring solution
  - Click the *resource group* icon -> click the name of your remote monitoring solution -> click the IoT Hub service that was created when you provisioned the remote monitoring solution. 
      <p align="center">
         <img src="/images/IoTHubKeys1.jpg" /> 
      </p>
1. Obtain the "Connection string - primary key" for your IoT Hub. 
  - Click on the "Shared access policies".
  - Click on the "iothubowner" policy.
  - Copy the primary key connection string. Take note of the primary key connection string for later.
      <p align="center">
         <img src="/images/IoTHubKeys2.jpg" /> 
      </p>

## Create Your Device in the Remote Monitoring Pre-configured Solution 
1. Go back to the Azure IoT Suite microsite tab. Your pre-configured solution should be provisioned now. Click the "Launch" button on the newly provisioned remote monitoring solution. This will open up a new browser tab to your remote monitoring solution dashboard.
      <p align="center">
         <img src="/images/SolutionReady.jpg" width="30%" height="30%" /> 
      </p>
1. Click the "Sign In" button.
      <p align="center">
         <img src="/images/RMSignIn.jpg" width="50%" height="50%"/> 
      </p>
1. If the following page requires you to accept the terms and conditions, click "I Agree". 
1. You will now have access to your created remote monitoring preconfigured solution. Feel free to browse around and review the features available in the pre-configured solution. 
      <p align="center">
         <img src="/images/RMDashboard.jpg"/> 
      </p>

1. Create a new custom device within the RM-PCS. 
  1. At the bottom left of the portal, click the "+ Add A Device" button. 
      <p align="center">
         <img src="/images/AddDevice.jpg"/> 
      </p>
  1. On the "Step 1 of 3" page, click "Add New" to add in a custom device. 
      <p align="center">
         <img src="/images/AddNewCustomDevice.jpg"/> 
      </p>
  1. On the "Step 2 of 3" page, click the "Let me define my own Device ID" radio button. Enter in a device ID eg. MyRaspberryPi. Click on the "Check ID" button to ensure that your device ID is unique. If the Device ID is unique, the text "Device ID is available" in green text will appear. Click the "Create" button. 
      <p align="center">
         <img src="/images/DefineDeviceID.jpg"/> 
      </p>
  1. The "Step 3 of 3" page provides you the *Device ID*, *IoT Hub Hostname* and *Device Key* that you will need to connect your Raspberry Pi to the remote monitoring solution. Copy and paste the value of these fields in a text document somewhere. 
      <p align="center">
         <img src="/images/CustomDeviceParams.jpg"/> 
      </p>

Congratulations! You have successfully spun up your Remote Monitoring Pre-configured (RM-PCS) solution and created a new custom device that you will configure in the next section of the labs! 

[Back to Main HOL Instructions](/README.md)
