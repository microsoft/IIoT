## Azure Functions Lab

In this part of the lab, you will create an Azure function that will be used to programmatically send data back to the Raspberry Pi. 

### Steps
1. Get the values associated with the Event Hub compatible endpoints as well as the IoT Hub Connection String:
  1. Open the Azure Portal [here](https://ms.portal.azure.com)
  1. Click on the IoT Hub that was created earlier. 
  1. Under the “Messaging” category click on “Endpoints”.
  1. In the list of "Built-in endpoints", click on “Events” to load the Events endpoint properties blade. 
  1. Take note of the values for the “Event Hub-compatible name” and “Event Hub-compatible endpoint" fields.  (EVENTHUB_CONFIG)
     
  ![Event Hub Endpoint](/images/EHendpointValues.jpg)
  
  1. Create a new Shared Access Policy for the function that you will create. 
    1. Click on “Shared Access Policies”
    1. Click on “+ Add”
    1. Enter a name for your policy.  Eg. “Function”  
    1. Give the following permissions
      1. Registry Read
      1. Registry write
      1. Service connect
    1. Click the "Create" button. 
    
    ![Create SAS](/images/CreateSAS.jpg)
    
    1. Once the new Shared Access Policy has been created, click the new policy. 
    1. Take note of the "Connection String-primary key".  (IOT_HUB_CONNECTION_STRING)
    
    ![Connection string](/images/ConnectionString.jpg)
    
1.	Create an Azure Function. You will be creating a C# Azure Function that will be activated whenever the compatible event hub within the IoT hub service receives a new event. 
  1. Go to the Azure functions portal: [here](https://functions.azure.com/signin)
  1. Select your Subscription, enter a Name for your Function App, and select the Region you will deploy the function to. Click on "Create + get started"
  
  ![Create Function](/images/CreateFunction.jpg)
  
  1. Click on “+ New Function”
  
  ![New Function](/images/NewFunction.jpg)
  
  1. Choose the “EventHubTrigger-CSharp”
    1. Enter “Name your function”
    1. Enter “Event Hub name”.  Use the Event hub-compatible name obtained above. 
    
    ![Select EH Trigger](/images/EHTrigger.jpg)
    
    1. Create a new “Event Hub connection”.  This is the connection string for the event hub.
      - Click "new”.
      - Click "Add a connection string".
      - In the *Connection name* field, enter the IoT Hub Event Hub-compatible connection name that you obtained earlier
      - In the *Connection string* field, enter the IoT Event Hub compatible connection string. This connection string is a combination of the connection string for the Event Hub endpoint and the Shared Access key for the fuction's policy that you created above. <br>
Format: "Endpoint=" + *Event Hub-compatible endpoint* + ";" + *SharedAccessKey from the function policy*
        ex. Endpoint=sb://<eventHubName>.servicebus.windows.net/;SharedAccessKeyName=<SASPolicyName>;SharedAccessKey=<SASPolicyKey>
         Click "OK"
    
      <p align="center">
         <img src="/images/EHconnection.jpg" width="50%" height="50%" /> 
      </p>
      
  1. On the *New Function* page, click "Create". The template for your new Event Hub Trigger function is now created!
  1. Configure libraries for the new function created. 
    1. Expand the “Logs” view at the bottom of the page
    1. Click on “View Files”
    
    ![Expand Function views](/images/functionViews.jpg)
    
    1. Click on “+ Add” under the "View files" tab. 
    1. Enter “project.json”
    
    ![Add project file](/images/addProject.jpg)
    
    1. Copy the text from [project.json](/AzureFunction/project.json) file in the github repo to the new json file you created.
    1. Click "Save". 
    
      <p align="center">
         <img src="/images/projectSave.jpg" width="50%" height="50%" /> 
      </p>    
        
    1. Copy the text from [Function.txt](/AzureFunction/AzureFunction.txt) in the github repo to the "run.csx" file. 
    1. Update the CONNECTION_STRING variable to point to the IoT Hub Function Connection String that you obtained earlier.  See “(IOT_HUB_CONNECTION_STRING)” above.

      <p align="center">
         <img src="/images/runFunction.jpg" /> 
      </p>  
        
    1. Click “Run” to start the function

## Trying it out

You may have difficulties getting your Pi temperature over the threshold.  You can do one of the following:
- Lower the threshold in the device twin in the preconfigured solution website
- Update your Python script to use the Sense Hat emulator instead of the physical board.  

[Back to Main HOL Instructions](/README.md)
