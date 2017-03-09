# Stream Analytics Lab - Send data to Power BI

Prerequisites: Power BI account

## Create Azure Stream Analytics (ASA) Job

1. Log into the [Azure portal](https://ms.portal.azure.com)
1. Add an Azure Stream Analytics (ASA) Job
  1. Click on "+ New"
  
     <p align="center">
         <img src="/images/AzureNewButton.jpg" width="50%" height="50%"/> 
      </p>    
  
  1. In the "Search the marketplace" file, type in "Stream Analytics". Click on the "Stream Analytics job" option that shows up. 
  
     <p align="center">
         <img src="/images/newASA.jpg" width="50%" height="50%" /> 
     </p>    
  
    1. Click on the "Stream Analytics job" that shows up in the results. Click "Create".
  
       <p align="center">
          <img src="/images/newASA1.jpg" width="50%" height="50%" /> 
       </p>    
      
    1. Enter a name for your job.  eg. "HandsOnLab-PowerBI" 
    1. Choose your subscription.
    1. Choose a Resource Group. Use the existing Resource Group that was created previously. This will make it easier to delete all the resources when you are done with the lab. 
  1. Choose a Location.  eg. West US
  1. Click "Create". Feel free to click the "Pin to dashboard" check box. This will add the newly created ASA service to the main Azure portal dashboard. 
      
      <p align="center">
         <img src="/images/newASA3.jpg" width="50%" height="50%" /> 
      </p>   
  
  1. Wait for the job to be created. You will see a notification banner that will pop up in the top right corner of the Azure portal to indicate the status of the job. This banner will disappear automatically. If you wish to see all the past notifications, click the bell icon. 
      
      <p align="center">
         <img src="/images/AzureNotification.jpg" width="50%" height="50%" /> 
      </p>   
  
1. Next, you will add an Input for the Stream Analytics job. 
  1. If you pinned the ASA service to the dashboard, you will see the ASA tile on the main Azure portal page. Click it. 
      
      <p align="center">
         <img src="/images/clickASA1.jpg" width="50%" height="50%" /> 
      </p>   
       
     If not, click "Resource Groups" -> Your *resource group name* -> Your *ASA name*
      
      <p align="center">
         <img src="/images/clickASA2.jpg" /> 
      </p>   
       
  1. Under the "Job Topology" category, click on "Inputs".
  1. Click "+ Add".
      
      <p align="center">
         <img src="/images/addInput1.jpg" width="50%" height="50%" /> 
      </p>   
    
  1. In the "New Input" blade that appears, fill in the fields:
    1. Alias: Free form text name for the input.  eg. "IoTHub"
    1. Source Type: Data Stream
    1. Source: IoT Hub
    1. Subscription: Use IoT Hub from current subscription
    1. IoT Hub: Choose the IoT Hub you have been using for the lab
    1. Endpoint: Messaging
    1. Shared Access Policy Name: iothubowner
    1. Consumer Group: asa (we created this earlier)
    1. Event Serialization Format: JSON
    1. Encoding: UTF-8
    1. Click "Create" and wait for the input to be created. 
              
      <p align="center">
         <img src="/images/ASANewInput.jpg" width="50%" height="50%" /> 
      </p>   
  
1. Next, add an Output for the Stream Analytics job.
  1. Under the "Job Topology" category, click on "Outputs". 
        
      <p align="center">
         <img src="/images/addOutput.jpg" width="50%" height="50%" /> 
      </p>   
  
  1. Click "+ Add" in the blade to the right
  1. Enter the properties
    1. Output alias: Free form text for the input. eg. "PowerBI"
    1. Sink: Power BI
    1. Click "Authorize". 
    
      <p align="center">
         <img src="/images/powerBIOutput.jpg" width="50%" height="50%" /> 
      </p>      
    
    1. A new window will open requiring credentials to authorize the connection to PowerBI.
   
      <p align="center">
         <img src="/images/authorizePBI.jpg" width="50%" height="50%" /> 
      </p>      
       
    1. Enter a Dataset name.  A dataset is a collection of data tables.  eg. Raspberry Pi Dataset
    1. Enter a Table Name. eg. Raspberry Pi Data Table
    1. Click "Create"
   
      <p align="center">
         <img src="/images/powerBIOutput2.jpg" width="50%" height="50%" /> 
      </p>      
       
    1. Wait for the input and output to be created.  Check the Notifications in the portal for a successful connection test. 
1. Create an ASA Query.
  1. Under the "Job Topology" category, click on "Query". The inline query editing tool will already have some stub code inserted. You will make some modifications to the query. 
  1. Enter the following query: 
  
    SELECT <br>
      * <br>
    INTO  <br>
      [PowerBI] <br>
    FROM <br>
      ["IoTHub"] <br>
      
   1. Click "Save". 
   1. Click "Test" 
   
      <p align="center">
         <img src="/images/ASAQuery.jpg" width="50%" height="50%" /> 
      </p>      
       
1. Start the ASA Job
  1. Click on "Overview" 
  1. Click "Start"
   
      <p align="center">
         <img src="/images/startASA.jpg" width="50%" height="50%" /> 
      </p>  
      
  1. For the "Job output start time", click "Now"
  1. Click "Start"
   
      <p align="center">
         <img src="/images/startASA2.jpg" width="50%" height="50%" /> 
      </p>  
          
## View Data in Power BI
1. Open Power BI in a web browser - https://powerbi.microsoft.com
1. Sign in
1. <TODO - Finish this off>


[Back to Main HOL Instructions](/README.md)
