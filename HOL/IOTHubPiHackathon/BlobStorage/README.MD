# Stream Analytics Lab - Send data to Blob Storage

In this lab, we are going to create an Azure Stream Analytics job that will take the telemetry data from the Raspberry Pi and store it in Blob Storage. 


## Stop the device simulators 

**This step is only relevant if you created the Remote Monitoring preconfigured solution [(Lab 2a)](/HOL/IOTHubPiHackathon/2/README.md)** <BR>
Perform this part of the module to populate Blob storage with only data coming from your physical Raspberry Pi and not the simluated devices provisioned as part of the preconfigured solution. The following steps will stop the telemetry data flowing from the simulated devices to your IoT Hub.

1. Go to the web app that was provisioned as part of the Remote Monitoring preconfigured solution.
  - Navigate to the [Azure portal](https://ms.portal.azure.com)  
  - Click the resource group icon -> click the name of the group of your Remote Monitoring solution -> click the App Service that was created when you provisioned the solution.
  
   <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/OpenWebApp.jpg" width="80%" height="80%"/> 
      </p> 
      
  - Click 'Browse' to navigate to the web app. 
  
     <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/BrowseToWebApp.jpg" width="80%" height="80%"/> 
      </p> 

2. You should be at the same device dashboard as when you initially launched the preconfigured solution.
  - Click the 'Gear' icon in the upper right corner
  
    <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/OpenSettingsInWebApp.jpg" width="80%" height="80%"/> 
      </p> 

3. Toggle the 'Simulation data' slider so that it reads 'Stopped'. This will stop all telemetry data and associated alerts from the simulated devices.

    <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/StopSimulatedDeviceData.jpg" width="60%" height="60%"/> 
      </p>  
  
## Create Azure Stream Analytics (ASA) Job

1. Log into the [Azure portal](https://ms.portal.azure.com)
2. Add an Azure Stream Analytics (ASA) Job
  - Click on "+ Create a resource"
  
     <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/CreateAResource.jpg" width="30%" height="30%"/> 
      </p>    
  
  - In the "Search the marketplace" blade, type in "Stream Analytics". Click on the "Stream Analytics job" option that shows up. 
  
     <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/newASA.jpg" width="40%" height="40%" /> 
     </p>    
  
    1. Click "Create" on this blade.
  
       <p align="center">
          <img src="/HOL/IOTHubPiHackathon/images/newASA1.jpg" width="50%" height="50%" /> 
       </p>    
      
    1. Enter a name for your job.  eg. "HandsOnLab-BlobStorage" 
    1. Choose your subscription. Use the same subscription you used to provision everything else in this lab.
    1. Choose a Resource Group. Use the existing Resource Group that was created previously. This will make it easier to delete all the resources when you are done with the lab. 
    1. Choose a Location. Try and choose the same location as where the rest of your solution has been provisioned.
    1. Select "Cloud" for the Hosting Environment. With the IoT Edge gateway solution, you can now push ASA jobs down to the edge and have ASA jobs run locally on premise on your gateway solution. In these labs, we are going to use the cloud ASA job to filter out data streaming through IoT Hub and pass that data down to Blob Storage. 
    1. Leave the Streaming Units at 1. Streaming Units are the pool of computation resources available for the Stream Analytics job.
    1. Click "Create". Feel free to click the "Pin to dashboard" check box. This will add the newly created ASA service to the main Azure portal dashboard. 
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/StreamAnalyticsBlob.JPG" width="30%" height="30%" /> 
      </p>   
  
  - Wait for the job to be created. You will see a notification banner that will pop up in the top right corner of the Azure portal to indicate the status of the job. This banner will disappear automatically. If you wish to see all the past notifications, click the bell icon. 
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/AzureNotification.jpg" width="50%" height="50%" /> 
      </p>   
  
- Next, you will add an Input for the Stream Analytics job. 
  - If you pinned the ASA service to the dashboard, you will see the ASA tile on the main Azure portal page. Click it. 
  
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/clickASABlob.jpg" width="20%" height="20%" /> 
      </p> 
      
     If not, click "Resource Groups" -> Your *resource group name* -> Your *ASA name*
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/BlobStorage.JPG" width="60%" height="60%" /> 
      </p>   
       
  - Under the "Job Topology" category, click on "Inputs".
  - Click "+ Add stream input".
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/addInput1.jpg" width="60%" height="60%" /> 
      </p>   
      
  - In the pop up menu that appears, select "IoT Hub" 
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/selectIoTHub.jpg" width="30%" height="30%" /> 
      </p>   
    
  - In the "New Input" blade that appears, fill in the fields:
    - Input Alias: This is a free form text name for the input to the ASA job. eg. "IoTHub"
    - Choose "Select IoT Hub from your subscriptions". We will be connecting the ASA job to the IoT Hub you created and collecting streaming data from that existing IoT Hub
    - Subscription: Choose the name of your IoT Hub from your current subscription
    - IoT Hub: Choose the IoT Hub you have been using for the lab
    - Endpoint: Messaging
    - Shared Access Policy Name: iothubowner
    - Consumer Group: asa (we created this earlier)
    - Event Serialization Format: JSON
    - Encoding: UTF-8
    - Event Compression Type: None
    - Click "Save" and wait for the input to be created. 
    
    <p align="center">
       <img src="/HOL/IOTHubPiHackathon/images/ASANewInput.jpg" width="30%" height="30%" /> 
    </p>   
  
- Next, add an Output for the Stream Analytics job.
  1. First we need to create a new Storage account for the data to be streamed to.
    - Click on "+ Create a resource"
  
     <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/CreateAResource.jpg" width="30%" height="30%"/> 
      </p> 
      
    - In the "Search the marketplace" blade, type in "storage account". Click on the "Storage account - blob, file, table, queue" option that shows up. Click "Create".
  
     <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/NewStorageAccount.jpg" width="40%" height="40%" /> 
     </p> 
     
    - In the "Create storage account" blade enter the following. 
      - Enter a name for your atorage account. this name must be unique across all existing storage account names in Azure. eg. "<your-initials>iotholstorageaccount" 
      - Leave "Resource manager" as the Deployment model. 
      - Leave "Storage (general purpose v1)" as the Account Kind.
      - Choose a Location. Try and choose the same location as where the rest of your IoT Hub has been provisioned.
      - Leave "Locally Redundant storage (LRS)" as the Replication. LRS still ensures that three copies of your data is stored in Azure.
      - Leave the default settings selected for Performance and Secure transfer required options.
      - Choose your subscription. Use the same subscription you used to provision your IoT Hub resource.
      - Choose an existing Resource Group. Use the one that contains your IoT Hub resource.
      - Leave "Virtual Networks" disabled. Enabling this will grant access to the storage account from only a specified virtual network and subnets.
      - Click "Create".
      
     <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/NewStorageAccount1.jpg" width="30%" height="40%" /> 
     </p>
  
  
  2. Navigate back to the Stream Analytics Job you created ("Resource Groups" -> *Your resource group name* -> *Your ASA name*). 
  
    - In the Stream Analytics blade under the "Job Topology" category, click on "Outputs". 
        
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/addOutput.jpg" width="50%" height="50%" /> 
      </p>   
  
  3. Click "+ Add" in the blade to the right. In the pop up menu that appears select "Blob storage".
    
    <p align="center">
       <img src="/HOL/IOTHubPiHackathon/images/SelectASAOutputBlob.jpg" width="30%" height="30%" /> 
    </p>      
    
  4. Fill out the values in the "Blob storage" blade. 
    - Enter in any free form text for the "Output alias". eg. "BlobStorage"
    - Choose "Select Blob storage from your subscriptions". We will be connecting the ASA job to the Blob Storage account that you just created.
    - Choose the subscription that you created your storage account in.
    - Choose the Storage account that you just created in the previous steps.
    - For "Container", select "Create new" and enter "iotdata"
    - In "Path pattern", enter "data/{date}/{time}"
    - Keep all the remaining options set to their default values.
    - Click "Save". 
    
    <p align="center">
       <img src="/HOL/IOTHubPiHackathon/images/SABlobOutput.jpg" width="30%" height="30%" /> 
    </p>      
           
- Next lets create an ASA Query.
  1. In the Stream Analytics job blade, under the "Job Topology" category, click on "Query". The inline query editing tool will already have some stub code inserted. You will make some modifications to the query. 
  2. Enter the following query: (Note, if you named your Input and Output bindings something different then you will have to update the query parameters so that they correspond correctly)  
  
  
```
    SELECT 
      * 
    INTO  
      [BlobStorage] 
    FROM 
      [IoTHub] 
```  

  1. Click "Save". 
  1. If you wish to run a test on your newly generated query, you will need to upload some sample data that the ASA Query tool will use to run the query. To generate a sample file, you can either manually generate your own file or get a sampling of data from the IoT Hub input. Click the elipses (...) beside the IoTHub input and click "Sample data from input" to start collecting data. Click the "Upload sample data from file" option once you have created a sample file and then run the query test by clicking the "Test" button.
   
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/ASAQueryBlob.jpg" width="50%" height="50%" /> 
      </p>      
       
- Start the ASA Job
  1. Click on "Overview" 
  1. Click "Start"
   
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/startASA.jpg" width="50%" height="50%" /> 
      </p>  
      
  1. For the "Job output start time", click "Now"
  1. Click "Start"
   
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/startASA2.jpg" width="50%" height="50%" /> 
      </p>  
          
## View IoT blob data in the Azure Portal

  1. Click "Resource Groups" -> Your *resource group name* -> Your *blob storage account name* (eg. "handsonlabstorageaccount")
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/BlobStorage.JPG" /> 
      </p> 

  1. Select "Browse blobs"
  1. Select the container.  eg. "iotdata"
  1. Click down through the folder hierarchy.  eg. "data" -> <year> -> <month> -> <day> -> <UTC hour>
  1. Click on a file.
  1. Select "Download".
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/BlobIoTDataDownload.JPG" /> 
      </p> 

  1. Open the file with your favorite editor to view the IoT data
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/BlobIoTData.JPG" /> 
      </p> 

Congratulations, you have streamed your data into blob storage! 

[Next lab - 5 Azure Functions](/HOL/IOTHubPiHackathon/AzureFunction)

[Back to Main HOL Instructions](/HOL/IOTHubPiHackathon/README.md)
