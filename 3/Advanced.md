This tutorial will walk you through the steps to send messages via AMQP and MQTT. In the previous labs, we used HTTP/REST which is not ideal for IoT type scenarios as it will has high overhead, will have scale issues and generally isn't as fast.

1. Compiling requires more memory.  Increase the swap space to 500 MB.
   - Edit this file:  /etc/dphys-swapfile 
   - Change swap file sile to 500.  eg. CONF_SWAPSIZE=500
   - Stop the swapfile: /etc/init.d/dphys-swapfile stop
   - Start the swapfile: /etc/init.d/dphys-swapfile start
1. Clone the repository:  git clone --recursive https://github.com/Azure/azure-iot-sdk-python.git 
1. Compile by following these commands:

   - sudo apt-get update <br>
   - sudo apt-get install -y git cmake build-essential curl libcurl4-openssl-dev libssl-dev uuid-dev <br>
   - cmake --version <br>
   - cd <br>
   - cd azure-iot-sdk-python/build_all/linux <br>
   - ./setup.sh <br>
   - ./build.sh <br>
   
1. Add connection string to the simple sample:

   - cd ../../device/samples <br>
   - Edit iothub_client_sample.py, add connection string <br>
   - python iothub_client_sample.py <br> <br>

Reference: https://github.com/Azure/azure-iot-sdk-python
