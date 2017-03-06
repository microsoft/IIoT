## Advance Setup (Must be completed in advance of the HOL)

Please perform the following steps in advance of the HOL otherwise you will waste the entire HOL performing these steps.
- Ensure your Raspberry Pi can boot [Raspian] (https://www.raspberrypi.org/downloads/) from the SD card.
  1. Install the operating system installer [NOOBS] (https://www.raspberrypi.org/downloads/noobs/) 
  1. Format the microSD card that you will use for your Raspberry Pi. 
  1. Extract the files in the NOOBs zip file. 
  1. Copy the extracted files onto the formatted microSD card such that the files are at the root directory of the microSD card. 
  1. Insert the microSD card into your Pi and connect the power supply. 
  1. Click to install Raspbian
     <p align="center">
        <img src="images/NOOBS_Install.jpg" width="50%" height="50%"/>
      </p>
  1. Confirm the deletion of content on the SD card and the installation of the OS. 
      <p align="center">
        <img src="images/ConfirmInstall.jpg" width="50%" height="50%"/>
      </p>
- Ensure Sense HAT Emulator is installed (by default it is installed with Raspian). Verify by checking under 'Programming' in the Raspian GUI.
      <p align="center">
        <img src="images/SenseHat.jpg"  width="50%" height="50%"/>
      </p>
- Install [Device Explorer](https://github.com/Azure/azure-iot-sdks/releases/download/2016-11-17/SetupDeviceExplorer.msi) on your Windows laptop. Device Explorer is a great tool that can be used to perform operations such as manage the devices registered to an IoT hub, view device-to-cloud messages sent to an IoT hub, and send cloud-to-device messages from an IoT hub. 
- Ensure your Azure subscription login is working and you have sufficient permissions to create resources.
- Download and install [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).
