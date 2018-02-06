# Stream Analytics Lab - Send data to Power BI

Prerequisites: Power BI account

In this lab, we are going to create an Azure Stream Analytics job that will take the telemetry data from the Raspberry Pi and feed it to PowerBI as the output. From PowerBI, we will use the user friendly interface to drag and drop values onto a BI canvas and create some simple reports so that we can visualize the data coming into Azure from our device. 

## Optional: Stop the device simulators 

** This step is only relevant if you created the Remote Monitoring preconfigured solution (Lab 2a)<BR>
Perform this part of the module if you wish to keep your PowerBI report clean with only data coming from your physical Raspberry Pi. The following steps will stop the web app that runs the simulators and therefore, the telemetry data from these simulators will not be sent to IoT hub. 

1. Log into the [Azure portal](https://ms.portal.azure.com)
2. Go to the "App Services" blade
3. Click on the App services associated with your preconfigured solution
4. Go To the "WebJobs" blade
5. Right click on the "DeviceSimulator-Webjob", and click "Stop"
  
     <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/StopDeviceSimulator.jpg" width="90%" height="90%"/> 
      </p>    <BR>
  
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
      
    1. Enter a name for your job.  eg. "HandsOnLab-PowerBI" 
    1. Choose your subscription.
    1. Choose a Resource Group. Use the existing Resource Group that was created previously. This will make it easier to delete all the resources when you are done with the lab. 
  - Choose a Location.  eg. East US
  - Select "Cloud" for the Hosting Environment. With the IoT Edge gateway solution, you can now push ASA jobs down to the edge and have ASA jobs run locally on premise on your gateway solution. In these labs, we are going to use the cloud ASA job to filter out data streaming through IoT Hub and pass that data down to PowerBI. 
  - Click "Create". Feel free to click the "Pin to dashboard" check box. This will add the newly created ASA service to the main Azure portal dashboard. 
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/newASA4.jpg" width="30%" height="30%" /> 
      </p>   
  
  - Wait for the job to be created. You will see a notification banner that will pop up in the top right corner of the Azure portal to indicate the status of the job. This banner will disappear automatically. If you wish to see all the past notifications, click the bell icon. 
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/AzureNotification.jpg" width="50%" height="50%" /> 
      </p>   
  
- Next, you will add an Input for the Stream Analytics job. 
  1. If you pinned the ASA service to the dashboard, you will see the ASA tile on the main Azure portal page. Click it. 
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/clickASA1.jpg" width="30%" height="30%" /> 
      </p>   
       
     If not, click "Resource Groups" -> Your *resource group name* -> Your *ASA name*
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/clickASA2.jpg" /> 
      </p>   
       
  - Under the "Job Topology" category, click on "Inputs".
  - Click "+ Add Stream Input".
  
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/addInput1.jpg" width="50%" height="50%" /> 
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
  1. Under the "Job Topology" category, click on "Outputs". 
        
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/addOutput.jpg" width="50%" height="50%" /> 
      </p>   
  
  1. Click "+ Add" in the blade to the right and select "PowerBI"
  1. Fill out the values in the "New Output" blade. 
    - Enter in any free form text for the "Output alias". eg. "PowerBI"
    - Click the "Authorize" button to make the connection to your PowerBI account. In the pop-up window that appears, enter in your PowerBI username and password. Once you enter in the correct credentials, the "Group Workspaces" drop down field should populate. 
    - Choose the workspace that you want the ASA streaming data to be stored. eg. "My workspace"
 
    <p align="center">
       <img src="/HOL/IOTHubPiHackathon/images/powerBIOutput.jpg" width="30%" height="30%" /> 
    </p>      
    
    - A new window will open requiring credentials to authorize the connection to PowerBI. Enter your credentials and click "Sign in".
    <p align="center">
       <img src="/HOL/IOTHubPiHackathon/images/authorizePBI.jpg" width="50%" height="50%" /> 
    </p>      
       
    - Enter a Dataset name.  A dataset is a collection of data tables.  eg. Raspberry Pi Dataset
    - Enter a Table Name. eg. Raspberry Pi Data Table
    - Click "Save"
    <p align="center">
       <img src="/HOL/IOTHubPiHackathon/images/powerBIOutput2.jpg" width="30%" height="30%" /> 
    </p>      
       
    1. Wait for the input and output to be created.  Check the Notifications in the portal for a successful connection test. 
- Create an ASA Query.
  1. Under the "Job Topology" category, click on "Query". The inline query editing tool will already have some stub code inserted. You will make some modifications to the query. 
  1. Enter the following query: 
 
    SELECT 
      * 
    INTO  
      [PowerBI] 
    FROM 
      [IoTHub] 
         
   1. Click "Save". 
   1. If you wish to run a test on your newly generated query, you will need to upload some sample data that the ASA Query tool will use to run the query. To generate a sample file, you can either manually generate your own file or get a sampling of data from the IoT Hub input. Click the elipses (...) beside the IoTHub input and click "Sample data from input" to start collecting data. Click the "Upload sample data from file" option once you have created a sample file and then run the query test by clicking the "Test" button. 
   
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/ASAQuery.jpg" width="50%" height="50%" /> 
      </p>      
       
- Start the ASA Job
  1. Click on "Overview" 
  1. Click the "Start" button
   
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/startASA.jpg" width="50%" height="50%" /> 
      </p>  
      
  1. For the "Job output start time", click "Now"
  1. Click "Start"
   
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/startASA2.jpg" width="50%" height="50%" /> 
      </p>  
          
## View Data in Power BI
1. Open Power BI in a web browser - https://powerbi.microsoft.com
2. Sign in
3. Go to the bottom of the bar on the left.  Expand "My Workspace" and select the dataset that you configured in Azure Stream Analytics (eg. Raspberry Pi Dataset). If you don't see the dataset that you created in the list, it's likely that no data has been streamed into your ASA job yet. Make sure that your ASA job has started and that there's input and output event showing up in your monitoring graph. Ask an instructor for assistance if you have any issues with this. 
   
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/PowerBILab.png" width="80%" height="80%" /> 
      </p>  
            
4. In the "Fields" bar (far right), select EventEnqueuedUtcTime and Temperature
   
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/Fields.jpg" width="50%" height="50%" /> 
      </p>  
      
5. Select "Line Chart" from the visualizations.  You now see your Pi data in a line chart
   
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/Visualizations.jpg" width="50%" height="50%" /> 
      </p>  
      
6. Save your report.
7. Click on the "Pin Visual" button on the chart
   
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/Pin.jpg" width="50%" height="50%" /> 
      </p>  
      
8. Click on "New Dashboard"
9. Type in a name for your dashboard.  eg. "Raspberry Dashboard"
10. Your trend is now viewable as a dashboard.  You can also view the dashboard from a mobile app


[Next lab - 5 Azure Functions](/HOL/IOTHubPiHackathon/AzureFunction)

[Back to Main HOL Instructions](/HOL/IOTHubPiHackathon/README.md)
