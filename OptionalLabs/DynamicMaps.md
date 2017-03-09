## Enabling Interactive Bing Maps in the Pre-configured Solution

1. Open up a new tab and login to the Azure Portal using your subscription credentials https://portal.azure.com/
1. On the Azure Portal, click the "+ New" Button.
      <p align="center">
         <img src="/images/AzureNewButton.jpg" width="30%" height="30%"/> 
      </p>
1. In the search bar, type in "Bing Maps". Click the "Bing Maps API for Enterprise" service when it appears.
 <p align="center">
         <img src="/images/BingMapsSearch.jpg" /> 
      </p>
1. Select the "Bing Maps API for Enterprise" service. In the "Bings Maps for Enterprise" blade, click the "Create" button. 
 
     <p align="center">
         <img src="/images/CreateBingMapsAPI.jpg" /> 
      </p>
  - Give your Bing Maps API for Enterprise Service a name. eg. StudentName-BingMaps
  - Choose your subscription from the *Subscription* drop down box. 
  - Use the existing *Resource Group* that was created for your remote monitoring pre-configured solution. 
  - Select the "Internal Website Transactions Level 1" plan. Click OK. 
  - Review the "Lgeal terms". Click the "I give Microsoft permissions to share ... and related products" check box. Click the "Purchase" button. 
  - On the *Bing maps API for Enterprise* blade, click "Create"
      <p align="center">
         <img src="/images/CreateBingMapsAPI2.jpg" width="50%" height="50%"/> 
      </p>
1. Once the Bing Maps API service is created, you'll need to retrieve the key. 
  - Click the resource groups icon -> click the resource group that was created for the remote monitoring solution eg. IoTHandsOnLab -> click the "BingMapsAPIFree" service
      <p align="center">
         <img src="/images/QueryKey1.jpg" /> 
      </p>
- Click "Key Management" -> copy the key value in the "QueryKey" field. You will need this key for the next step.
      <p align="center">
         <img src="/images/QueryKey2.jpg" /> 
      </p>
1. Navigate to the Application Settings for the remote monitoring solution that you previously created. 
  - Click the resource groups icon -> Click the resource group that was created for the remote monitoring solution
  - Click the App Service with the same name as the remote monitoring solution that you previously created eg. IoTHandsOnLab
      <p align="center">
         <img src="/images/AppService1.jpg" /> 
      </p>
  - Under *Settings* -> Click *Application Settings* -> Under *App Settings*, find the MapApiQueryKey variable and paste the previously obtained key into the value field. Hit "Save". 
      <p align="center">
         <img src="/images/AppService2.jpg" /> 
      </p>


[Back to Main HOL Instructions](/README.md)
