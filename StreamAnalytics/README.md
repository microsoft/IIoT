# Stream Analytics Lab - Send data to Power BI

Prerequisites: Power BI account

## Create Stream Analytics Job

1. Log into the [Azure portal](https://ms.portal.azure.com)
1. Go to the Stream Analytics blade
1. Add a Stream Analytics Job
  1. Click on "+ Add" to add a new Stream Analytics job
  1. Enter a name for your job.  eg. "HandsOnLab-PowerBI"
  1. Choose your subscription.
  1. Choose a Resource Group. 
  1. Choose a Location.  eg. West US
  1. Click "Create".
  1. Wait for the job to be created.  It will show under notifications in the portal
1. Add an Input for the Stream Analytics job
  1. Under "Job Topology" click on "Inputs"
  1. Click "+ Add" in the blade to the right
  1. Enter the properties:
    1. Alias: Free form text name for the input.  eg. "IoTHub"
    1. Source Type: Data Stream
    1. Source: IoT Hub
    1. Subscription: Use IoT Hub from current subscription
    1. IoT Hub: Choose the IoT Hub you have been using for the lab
    1. Endpoint: Messaging
    1. Shared Access Policy Name: iothubowner
    1. Consumer Group: $Default (or empty)
    1. Event Serialization Format: JSON
    1. Encoding: UTF-8
1. Add an Output for the Stream Analytics job
  1. Under "Job Topology" click on "Outputs"
  1. Click "+ Add" in the blade to the right
  1. Enter the properties
    1. Output alias: PowerBI
    1. Sink: Power BI
    1. Click "Authorize" and enter Power BI credentials
    1. Enter a Dataset name.  A dataset is a collection of data tables.  eg. Raspberry Pi Dataset
    1. Enter a Data table. eg. Raspberry Pi Data Table
    1. Click "Create"
1. Wait for the input and output to be created.  Check Notifications in the portal
1. Create a Query
  1. Under "Job Topology" click on "Query"
  1. Enter the following query
    SELECT <br>
      * <br>
    INTO  <br>
      [PowerBI] <br>
    FROM <br>
      ["IoTHub"] <br>
   1. Click "Save"
1. Start the Job
  1. Click on "Overview" 
  1. Click "Start"

## View Data in Power BI
1. Open Power BI in a web browser - https://powerbi.microsoft.com
1. Sign in
1. <TODO - Finish this off>
