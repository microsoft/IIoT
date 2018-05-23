# Stream Analytics Lab - Send data to Power BI

Prerequisites: Power BI account

In this lab, we are going to create an Azure Stream Analytics job that will take the telemetry data from the Raspberry Pi and feed it to PowerBI as the output. From PowerBI, we will use the user friendly interface to drag and drop values onto a BI canvas and create some simple reports so that we can visualize the data coming into Azure from our device. 

## Optional: Stop the device simulators 

**This step is only relevant if you created the Remote Monitoring Solution Accelerator [(Lab 2a)](/HOL/IOTHubPiHackathon/2/README.md)** <BR>
Perform this part of the module if you wish to populate your PowerBI report with only data coming from your physical Raspberry Pi and not the simulated devices provisioned as part of the solution accelerator. The following steps will stop the telemetry data flowing from the simulated devices to your IoT Hub.

1. Go to the web app that was provisioned as part of the Remote Monitoring solution accelerator.
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
  
  - In the "Search the marketplace" box, type in "Stream Analytics". Click on the "Stream Analytics job" option that shows up. 
  
     <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/newASA.jpg" width="40%" height="40%" /> 
     </p>    
  
    1. Click on the "Stream Analytics job" that shows up in the results. Click "Create".
  
       <p align="center">
          <img src="/HOL/IOTHubPiHackathon/images/newASA1.jpg" width="50%" height="50%" /> 
       </p>    
      
    1. Enter a name for your job.  eg. "HandsOnLab-PowerBI" 
    1. Choose your subscription. Use the same subscription you used to provision everything else in this lab.
    1. Choose a Resource Group. Use the existing Resource Group that was created previously. This will make it easier to delete all the resources when you are done with the lab.
    1. Choose a Location.  Try and choose the same location as where the rest of your solution has been provisioned.
    1. Select "Cloud" for the Hosting Environment. With the IoT Edge gateway solution, you can now push ASA jobs down to the edge and have ASA jobs run locally on premise on your gateway solution. In these labs, we are going to use the cloud ASA job to filter out data streaming through IoT Hub and pass that data down to PowerBI. 
    1. Leave the Streaming Units at 1. Streaming Units are the pool of computation resources available for the Stream Analytics job.
    1. Click "Create". Feel free to click the "Pin to dashboard" check box. This will add the newly created ASA service to the main Azure portal dashboard. 
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/newASA4.jpg" width="30%" height="30%" /> 
      </p>   
  
  - Wait for the job to be created. You will see a notification banner that will pop up in the top right corner of the Azure portal to indicate the status of the job. This banner will disappear automatically. If you wish to see all the past notifications, click the bell icon. 
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/AzureNotification.jpg" width="50%" height="50%" /> 
      </p>   
  
- Next, you will add an Input for the Stream Analytics job.  
  - If you pinned the ASA service to the dashboard, you will see the ASA tile on the main Azure portal page. Click it. 
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/clickASA1.jpg" width="30%" height="30%" /> 
      </p>   
       
     If not, click "Resource Groups" -> Your *resource group name* -> Your *ASA name*
      
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/clickASA2.jpg" /> 
      </p>   
       
  - Under the "Job Topology" category, click on "Inputs".
  - Click "+ Add Stream input".
      
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
    - Click the "Authorize" button to make the connection to your PowerBI account. In the pop-up window that appears, enter in your PowerBI username and password.
 
    <p align="center">
       <img src="/HOL/IOTHubPiHackathon/images/powerBIOutput.jpg" width="30%" height="30%" /> 
    </p>      
    
    - A new window will open requiring credentials to authorize the connection to PowerBI. Enter your credentials and click "Sign in".
    <p align="center">
       <img src="/HOL/IOTHubPiHackathon/images/authorizePBI.jpg" width="50%" height="50%" /> 
    </p>      
    
    - Once you enter in the correct credentials, the "Group Workspace" drop down field should populate. Choose the workspace that you want the ASA streaming data to be stored. eg. "My workspace"
    - Enter a Dataset name.  A dataset is a collection of data tables.  eg. Raspberry Pi Dataset
    - Enter a Table Name. eg. Raspberry Pi Data Table
    - Click "Save"  
    <p align="center">
       <img src="/HOL/IOTHubPiHackathon/images/powerBIOutput2.jpg" width="30%" height="30%" /> 
    </p>

    - Wait for the input and output to be created.  Check the Notifications in the portal for a successful connection test.  
    
- Create an ASA Query.
   - Under the "Job Topology" category, click on "Query". The inline query editing tool will already have some stub code inserted. You will make some modifications to the query. 
    - Enter a query like the following: (Note, if you named your Input and Output bindings something different then you will have to update the query parameters to correspond correctly) 
  ```
    SELECT 
      * 
    INTO  
      [PowerBI] 
    FROM 
      [IoTHub] 
  ```  
    - Click "Save". 
    - If you wish to run a test on your newly generated query, you will need to upload some sample data that the ASA Query tool will use to run the query. To generate a sample file, you can either manually generate your own file or get a sampling of data from the IoT Hub input. Click the elipses (...) beside the IoTHub input and click "Sample data from input" to start collecting data. Click the "Upload sample data from file" option once you have created a sample file and then run the query test by clicking the "Test" button. 
   
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
          
## View Telemetry data in Power BI
1. Open Power BI in a web browser - https://powerbi.microsoft.com
2. Sign in.
3. Go to the bottom of the bar on the left.  Expand "My Workspace" and select "Datasets" to see the dataset you configured in Azure Stream Analytics (eg. Raspberry Pi Dataset). If you don't see the dataset that you created in the list, it's likely that no data has been streamed into your ASA job yet. Make sure that your ASA job has started and that there's input and output events showing up in your monitoring graph. Ask an instructor for assistance if you have any issues with this. 
   
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/PowerBILab.jpg" width="80%" height="80%" /> 
      </p>  
      
4.  Click the "Create Report" icon to create a new Power BI report using this dataset.
      
       <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/CreatePowerBIReport.jpg" width="80%" height="80%" /> 
      </p>  
      
4. In the "Fields" bar (far right), select EventEnqueuedUtcTime and Temperature
   
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/Fields.jpg" width="50%" height="50%" /> 
      </p>  
      
5. Select "Line Chart" from the visualizations.  You now see your Pi data in a line chart.
   
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/SelectLineChart.jpg" width="50%" height="50%" /> 
      </p>  
      
6. Save your report.
7. Click on the "Pin Visual" button on the chart
   
      <p align="center">
         <img src="/HOL/IOTHubPiHackathon/images/Pin.jpg" width="50%" height="50%" /> 
      </p>  
      
8. Click on "New Dashboard".
9. Type in a name for your dashboard.  eg. "Raspberry Dashboard"
10. Your trend is now viewable on a dashboard.  You may add more fields and visualizations if you like or view this dashboard from the Power BI mobile app.


[Next lab - 5 Azure Functions](/HOL/IOTHubPiHackathon/AzureFunction)

[Back to Main HOL Instructions](/HOL/IOTHubPiHackathon/README.md)
