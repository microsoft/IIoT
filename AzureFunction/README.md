## Azure Functions Lab

In this part of the lab, you will create an Azure function that will be used to programmatically send data back to the Raspberry Pi. The Azure function that you will create will be triggered by events that arrive at the IoT Hub. If the status of the Raspberry Pi is normal and the newly reported temperature goes above the set threshold, the status of Sense HAT will be set to high. If the status is at high and the temperature goes below the threshold, the status will be reset to normal. These state changes will be sent back to the Raspberry Pi through a Cloud to Device (C2D) message and the status will be displayed on the Sense HAT LED display. 

### Obtain Values Required to Connect Function to the IoT Hub
1. Get the values associated with the Event Hub compatible endpoints as well as the IoT Hub Connection String:
  1. Open the Azure Portal [here](https://ms.portal.azure.com)
  1. Click on the IoT Hub that was created earlier. 
  1. Under the “Messaging” category click on “Endpoints”.
  1. In the list of "Built-in endpoints", click on “Events” to load the Events endpoint properties blade. 
  1. Take note of the values for the “Event Hub-compatible name” and “Event Hub-compatible endpoint" fields.  (EVENTHUB_CONFIG)<br />  
  ![Event Hub Endpoint](/images/EHendpointValues.jpg) <br />
  1. Create a new Shared Access Policy for the function that you will create. 
    1. Click on “Shared Access Policies”
    1. Click on “+ Add”
    1. Enter a name for your policy.  Eg. “Function”  
    1. Give the following permissions
      - Registry Read
      - Registry write
      - Service connect
    1. Click the "Create" button. 
    ![Create SAS](/images/CreateSAS.jpg)
    1. Once the new Shared Access Policy has been created, click the new policy. 
    1. Take note of the "Connection String-primary key".  This is the value for the new IoT Hub Functions connection string (IOT_HUB_CONNECTION_STRING) <br />
    ![Connection string](/images/ConnectionString.jpg) <br><br> 
    You should have three different values noted now: “Event Hub-compatible name", “Event Hub-compatible endpoint" and the IoT Hub Functions connection string. These values will be used to connect your function to the IoT Hub. 

### Create a Function

In the next part of this lab, you will be creating a C# Azure Function that will get triggered whenever the IoT hub service receives a new event. 
For ease of getting through the lab, we have provided the code that you will need to write the function. When triggered, the code in the function will compare the input to the set threshold (the tag parameter setting that you previously set to a value of 40). If the value is above or below, the function will send a cloud to device (C2D) message to the RaspberryPi. Note: To be technically correct, the function actually gets triggered when the event hub compatible endpoint within the IoT Hub service receives an event. IoT Hub service is built with the event hub service running under the covers.
1. Navigate to the Azure portal: https://portal.azure.com 
2. Click the ‘+’ sign and type in “function app” 
    <p align="center">
    <img src="/images/CreateFunction1.jpg" width="50%" height="50%" />
    </p> 
 3.	Click the “Create” button <br> 
    <p align="center">
    <img src="/images/CreateFunction2.jpg" width="50%" height="50%" />
    </p> 

4.	Fill out the required values to create a function <br>
  - Provide the function app a name (eg. functionC2DHoL)
  - Select your Azure subscription
  - Select your existing subscription that you are using for the hands on lab
  - For hosting plan, select “consumption plan”
  - For location, choose the closest data centre (eg. East US)
  - For storage, select “create new” and provide a name for the storage
  - You can leave Application Insights turned off
  - Click “Create” <br>
      <p align="center">
    <img src="/images/CreateFunction3.jpg" width="30%" height="30%" />
    </p> 
  
5. Once the Function app is created, click the function (the function icon is the one in the shape of a lightning bolt)
6. Click the ‘+’ sign beside the “Functions” node in the hierarchy tree
    <p align="center">
    <img src="/images/CreateFunction4.jpg" />
    </p> 
7. Click on “Custom Function”
    <p align="center">
    <img src="/images/CustomFunction.JPG" width="50%" height="50%" />
    </p> 
8. Choose the “EventHubTrigger – C#”
9. Enter a name for your new function in the “Name your function” field. eg. MessageTriggerFunction
10.	In the “Event Hub name” field, enter the Event hub-compatible name that was obtained above. eg. iothandsonlabc4f51. <br>
![Select Trigger](/images/EHTrigger.jpg)
11.	Next, you will create a new “Event Hub connection”. The next few steps will walk you through a simple wizard that will allow you to build out the required connection string. 
  - Click "new”.
  - Select “IoT Hub”
  - Under the *IoT Hub* drop down box, select your IoT Hub eg. Iothandsonlabs
  - Under the *Endpoint* drop down box, select “Events (built-in endpoint)
  - Click “Select”
  
    <p align="center">
    <img src="/images/Select.jpg" width="50%" height="50%" />
    </p>

  - Finally, click the “Create” button. The template for your new Event Hub trigger is now created! 
12.	You will now configure the required libraries that will be needed for the new function created. 
  - Expand the “Logs” view at the bottom of the page
  - Click on “View Files”	

![Expand Function views](/images/functionViews.jpg)

  - Click on “+ Add” under the "View files" tab. 
  - Enter “project.json” <br />
![Add project file](/images/addProject.jpg)

  - Copy the text from [project.json](/AzureFunction/project.json) file in the github repo to the new json file you created.
  - Click "Save". 
    <p align="center">
    <img src="/images/projectSave.jpg" width="50%" height="50%" />
    </p>    
13.	Now add the main source code that will used within the function
  - Copy the text from [Function.txt](/AzureFunction/AzureFunction.txt) in the github repo to the "run.csx" file. 
  - In the run.csx file, find the CONNECTION_STRING variable and set the value to the IoT Hub Primary Key Connection String obtained in an earlier lab.
  - Click “Save and run” to run the function

   <p align="center">
    <img src="/images/runFunction.jpg" />
    </p>

## Trying it out

You will now attempt to trigger the function and have the function send a message back to the Sense HAT. 
If you recall in lab 2, you created a tag parameter called tags.HighTemperatureLimit and set it to 40. This is the threshold that will determine when the status of the Sense HAT will change to Hot (if temperature is above the limit) or to Normal (when the temperature drops below the limit). When the status changes, the state (hot or normal) will appear on the Sense HAT display LEDs. 

1. If your python script is no longer running on the Raspberry Pi, start it back up using the command ```python SenseHat_IoTHub_Http_Lab_Key.py```
2. Try to get the temperature of the Sense HAT above the threshold value (if set to the instructed value, you should be trying to get the temperature above 40C)

If you are having difficulties getting the temperature on your physical Sense HAT over the threshold, you can do one of the following:
- Lower the threshold in the device twin for the RaspberryPi device. You can do this in the preconfigured solution portal (see steps in lab 2 to determine how to change the HighTemperatureLimit) 
- Update your Python script to use the Sense Hat emulator instead of the physical board. Using the Sense HAT emulator will allow you to virtually control the temperature (and other properties)

[Back to Main HOL Instructions](/README.md)
