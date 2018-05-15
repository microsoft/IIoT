# Stream Analytics Lab - Send data to Blob Storage

In this lab, we are going to create an Azure Stream Analytics job that will take the telemetry data from the Raspberry Pi and store it in Blob Storage. 


## Stop the device simulators 

**This step is only relevant if you created the Remote Monitoring preconfigured solution [(Lab 2a)](/HOL/IOTHubPiHackathon/2/README.md)** <BR>
Perform this part of the module if you wish to populate Blob storage with only data coming from your physical Raspberry Pi and not the simluated devices provisioned as part of the preconfigured solution. The following steps will stop the telemetry data flowing from the simulated devices to your IoT Hub.

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
  - Click on "+ New"
  
     <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/AzureNewButton.jpg" width="30%" height="30%"/> 
      </p>    
  
  - In the "Search the marketplace" file, type in "Stream Analytics". Click on the "Stream Analytics job" option that shows up. 
  
     <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/newASA.jpg" width="40%" height="40%" /> 
     </p>    
  
    1. Click on the "Stream Analytics job" that shows up in the results. Click "Create".
  
       <p align="center">
          <img src="/HOL/IOTHubPiHackathon/images/newASA1.jpg" width="50%" height="50%" /> 
       </p>    
      
    1. Enter a name for your job.  eg. "HandsOnLab-BlobStorage" 
    1. Choose your subscription.
    1. Choose a Resource Group. Use the existing Resource Group that was created previously. This will make it easier to delete all the resources when you are done with the lab. 
  - Choose a Location.  eg. West US
  - Click "Create". Feel free to click the "Pin to dashboard" check box. This will add the newly created ASA service to the main Azure portal dashboard. 
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/StreamAnalyticsBlob.JPG" width="30%" height="30%" /> 
      </p>   
  
  - Wait for the job to be created. You will see a notification banner that will pop up in the top right corner of the Azure portal to indicate the status of the job. This banner will disappear automatically. If you wish to see all the past notifications, click the bell icon. 
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/AzureNotification.jpg" width="50%" height="50%" /> 
      </p>   
  
- Next, you will add an Input for the Stream Analytics job. 
  1. If you pinned the ASA service to the dashboard, you will see the ASA tile on the main Azure portal page. Click it. <br>
       
     If not, click "Resource Groups" -> Your *resource group name* -> Your *ASA name*
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/BlobStorage.JPG" /> 
      </p>   
       
  - Under the "Job Topology" category, click on "Inputs".
  - Click "+ Add".
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/addInput1.jpg" width="50%" height="50%" /> 
      </p>   
    
  - In the "New Input" blade that appears, fill in the fields:
    - Alias: Free form text name for the input.  eg. "IoTHub"
    - Source Type: Data Stream
    - Source: IoT Hub
    - Subscription: Use IoT Hub from current subscription
    - IoT Hub: Choose the IoT Hub you have been using for the lab
    - Endpoint: Messaging
    - Shared Access Policy Name: iothubowner
    - Consumer Group: asa (we created this earlier)
    - Event Serialization Format: JSON
    - Encoding: UTF-8
    - Click "Create" and wait for the input to be created. 
    <p align="center">
       <img src="/HOL/IOTHubPiHackathon/images/ASANewInput.jpg" width="30%" height="30%" /> 
    </p>   
  
- Next, add an Output for the Stream Analytics job.
  1. Under the "Job Topology" category, click on "Outputs". 
        
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/addOutput.jpg" width="50%" height="50%" /> 
      </p>   
  
  1. Click "+ Add" in the blade to the right
  1. Fill out the values in the "New Output" blade. 
    - Enter in any free form text for the "Output alias". eg. "BlobStorage"
    - For the Sink, select "Blob Storage".
    - In "Import option", select "Select blob storage from your subscription".
    - In "Storage Account", select "Create a new storage account"
    - In "Storage Account", enter a globally unique storage account name.  eg. handsonlabstorageaccount
    - In "Container", enter "iotdata"
    - In "Path pattern", enter "data/{date}/{time}"
    
    - Click "Create". 
    <p align="center">
       <img src="/HOL/IOTHubPiHackathon/images/SABlobOutput.JPG" width="30%" height="30%" /> 
    </p>      
           
    1. Wait for the input and output to be created.  Check the Notifications in the portal for a successful connection test. 
- Create an ASA Query.
  1. Under the "Job Topology" category, click on "Query". The inline query editing tool will already have some stub code inserted. You will make some modifications to the query. 
  1. Enter the following query: 
 
    SELECT 
      * 
    INTO  
      [BlobStorage] 
    FROM 
      [IoTHub] 
         
   1. Click "Save". 
   1. Click "Test" 
   
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/ASAQuery.jpg" width="50%" height="50%" /> 
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
