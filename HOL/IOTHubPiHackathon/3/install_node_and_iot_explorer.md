# Installing node

We will leverage an open source application called "Node Version Manager" (NVM), which will allow you to install various versions of Node in differnt OS environments and be able to switch between Node versions.

1. Install node in your environment
  - go to https://github.com/creationix/nvm#installation and run the install script:
  - ```curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash```

1b. You may need to refresh your .bashrc file environment:
  - ```source ~/.bashrc```

2. Now you can install a specific version of Node at anytime.  At the time of writting this document, 8.9.4 is the latest stable LTS. For example, to install Node 8.9.4 run the following command:
  - ```nvm install 8.9.4```
  - This will install Node 8.9.4
  - If this is your first time running ```nvm install``` it will make ```8.9.4``` your default Node version
  - ```npm``` is automatically installed along with your desired version of ```node```

3. Now you can install ```iothub-explorer``` globally for your OS
  - ```npm install -g iothub-explorer```
  
You can now continue [Lab 3](README.md) and use iothub-explorer to view our incoming telemetry and send messages to our device via the IoT Hub.
