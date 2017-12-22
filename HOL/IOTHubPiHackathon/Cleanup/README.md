At the end of the Hands on Labs, you should clean up your Azure account so that the resources provisioned do not continue to consume funds from your account. There are two options that we suggest you follow:

### Option 1 - Delete the Pre-configured Solution Completely

If you did not create a preconfigured solution skip this step.

1. Remove any functions you created. <br>
    - Click on "Function Apps" in the Azure portal  https://ms.portal.azure.com/
    - Click on the function that you created
    - Click on "Manage"
    - Click on the "Delete" button

1. Delete the Remote Monitoring Pre-configured Solution completely if you are not planning to continue to work on the labs in your own time. <br />
  - Best way to remove all the resources is through the www.azureiotsuite.com microsite
    - Navigate to www.azureiotsuite.com
    - Click the tile for your pre-configured solution: 
    
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/SolutionReady.jpg" width="50%" height="50%"/> 
      </p> 
    - Once the blade that appears, click the "Delete solution" button
    
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/DeletePCS.jpg" width="40%" height="40%"/> 
      </p> 
      
### Option 2 - Delete the Resource Group

If you did not create the free IoT Hub skip this step.

1. Open the [Azure Portal](https://portal.azure.com/).
1. Select your resource group from the "Resource groups" blade.
1. Select your resource group.
1. Select "Delete resource group"
1. Enter the name of the resource group.  <b>Be sure not to delete any resource groups you did not create!</b>
1. Click "Delete".

### Option 3 - Reduce the size of the running Azure services
If you plan on using the PCS after this lab, you can leave it running but it's recommended that you reduce the size/scale of some of the resources so that the services consume less from your subscription. 
1. Change the IoT Hub from an S2 – Standard to an S1 – Standard.
  - Within the pre-configured solution resource group, click on the IoT Hub service. 
  - Navigate to Settings -> Pricing and Scale -> and change the pricing tier to S1 – Standard. Make sure to click "Save" in the top navigation.
    
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/reduceIoTHub.jpg" width="90%" height="90%"/> 
      </p> 

2. Change the Storage account from Standard – GRS to Standard – LRS.
  - Click on the pre-configured solution storage account
  - Navigate to Settings -> Configuration. Select Locally-redundant storage (LRS). Make sure to click Save in the top navigation.

      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/reduceStorage.jpg" width="90%" height="90%"/> 
      </p> 
      
3. Change the App Service plans from S1 - Standard to B1 – Basic. Note that there’s two app services to scale down. 
   - Click on the app service plans that were provisioned as part of the pre-configured solution
   - Under Settings -> Scale Up (App Service Plan), select the B1 - Basic plan and click "Select"
   - Do the same for the *-jobhost* service plan
     <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/reduceAppService.jpg" width="90%" height="90%"/> 
      </p>   
      
4. Pause the simulated devices. The simulated devices run in a web job. To completely halt generation of new data when not in use, you can stop the web job in which the simulated devices are running.
  - From within the jobhost service plan, select Settings -> Webjobs. 
  - Right-click the "DeviceSimulator-Webjob" webjob. Click "Stop". 

      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/pauseSimulatedDevices.jpg" width="90%" height="90%"/> 
      </p> 


