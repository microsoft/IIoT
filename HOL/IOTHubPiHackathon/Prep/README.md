## Pre-workshop Setup (Must be completed in advance of the HOL)

Please perform the following steps in advance of the Hands-on-labs otherwise you will spend a significant time during the workshop performing these steps.

### Raspberry Pi Setup

You will need to walk through the following steps on your Raspberry Pi prior to the hands-on-lab. <BR>

1. Ensure your Raspberry Pi can boot [Raspian] (https://www.raspberrypi.org/downloads/) from the SD card. 
  - Follow the instructions to install the operating system: [NOOBS] (https://www.raspberrypi.org/downloads/noobs/) 
  - If you have a new microSD card that hasn't been formatted before, use [SDFormatter](https://www.sdcard.org/downloads/formatter_4/eula_windows/) to do a full format of the card.
  - Insert the microSD card into your Pi and connect the power supply. 
  - Click to install Raspbian
     <p align="center">
        <img src="/HOL/IOTHubPiHackathon/Prep/Images/NOOBS_Install.jpg" width="50%" height="50%"/>
      </p>
   - Confirm the deletion of content on the SD card and the installation of the OS. 
      <p align="center">
        <img src="/HOL/IOTHubPiHackathon/Prep/Images/ConfirmInstall.jpg" width="50%" height="50%"/>
      </p>
2. If you do not have the Sense HAT and will be using the Sense HAT Emulator, you will have to run through some extra steps to ensure that you access the Sense HAT Emulator graphically: 
  - First, run through the steps to ensure it's installed. Verify by checking under 'Programming' in the Raspian GUI.

      <p align="center">
        <img src="/HOL/IOTHubPiHackathon/Prep/Images/SenseHat.jpg"  width="50%" height="50%"/>
      </p>
      
   - Next, make sure that VNC is enabled. We will be using VNC so that a physical monitor will not be required for the labs. 
     - Select Menu -> Preferences -> Raspberry Pi Configuration -> Interfaces.
     
        <p align="center">
          <img src="/HOL/IOTHubPiHackathon/images/menu.jpg"  width="50%" height="50%"/>
        </p>
        
     - Ensure VNC is Enabled.
     
        <p align="center">
          <img src="/HOL/IOTHubPiHackathon/images/enableVNC.jpg"  width="50%" height="50%"/>
        </p>
         
3. Enable SSH on the Raspberry Pi. You will be SSH-ing to the Raspberry Pi to modify and execute scripts. 
  
  - In the menu, choose "Preferences", then "Raspberry Pi Configuration"
  - Enable SSH

### Laptop Setup (only required if using a laptop to emulate into the Raspberry Pi)

The following steps will walk you through the installation of tools that you need to run on your laptop for this lab: 

1. OPTIONAL if using a laptop to connect to the Raspberry Pi, download and install an SSH client like [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html). We will use PuTTY to SSH into the Raspberry Pi to perform various functions throughout the lab. 
1. OPTIONAL if using a laptop and the Sense HAT Emulator (vs the physical device), you'll need to install a VNC viewer client on your laptop so that you can remotely view your Raspbian desktop. Download and install RealVNC from (https://www.realvnc.com/download/viewer/)
1. Ensure your Azure subscription login is working and you have sufficient permissions to create resources.
1. Ensure you have access to Powerbi.com. If you are able to log in then you should be okay. 
1. Ensure that you can log into www.azureiotsolutions.com and can see the various Azure IoT solution Accelerators tiles as per below. If you get permission errors, you will need to ask your IT team to provide you with the right permissions or email your instructor for assistance. 
        <p align="center">
          <img src="/HOL/IOTHubPiHackathon/images/ValidAccelerators.jpg"  width="50%" height="50%"/>
        </p>
1. During the labs, you will install the Azure IoT CLI in your Azure cloud shell on the Azure Portal.  
  - Open the [Azure Portal](http://portal.azure.com) in your browser
  - click on the "Cloud Shell" button on the menu bar across the top

    ![Cloud Shell](../images/AzureToolBar.JPG)

  - install the azure iot cli extension with the following command

  ```bash
  az extension add --name azure-cli-iot-ext
  ```
  Alternatively, if you use Azure often, then you can actually install Azure CLI on your laptop and then install the IoT CLI extension mentioned above. Instructions to install the Azure CLI are [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)

[Back to Main HOL Instructions](/HOL/IOTHubPiHackathon/README.md)
