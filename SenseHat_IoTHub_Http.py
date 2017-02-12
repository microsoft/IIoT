"""
Sample code demonstrating Sense Hat running on Raspian and Raspberry Pi 3 sending temperature data to Azure IoT Hub using Azure IoT Hub REST API.

Test with Python 2.7 and 3.5
"""

import base64
import hmac
import hashlib
import time
import requests
import urllib
import time
import sys

#If using emulator, uncomment 'from sense_emu import SenseHat ' and comment out 'from sense_hat import SenseHat'
#from sense_hat import SenseHat #if using a physical SenseHat attached to Raspi
from sense_emu import SenseHat #if using a SenseHat Emulator

class D2CMsgSender:
    
    API_VERSION = '2016-02-03'
    TOKEN_VALID_SECS = 10
    TOKEN_FORMAT = 'SharedAccessSignature sig=%s&se=%s&skn=%s&sr=%s'
    
    def __init__(self, connectionString=None):
        if connectionString != None:
            iotHost, keyName, keyValue = [sub[sub.index('=') + 1:] for sub in connectionString.split(";")]
            self.iotHost = iotHost
            self.keyName = keyName
            self.keyValue = keyValue
            
    def _buildExpiryOn(self):
        return '%d' % (time.time() + self.TOKEN_VALID_SECS)
    
    def _buildIoTHubSasToken(self, deviceId):
        resourceUri = '%s/devices/%s' % (self.iotHost, deviceId)
        targetUri = resourceUri.lower()
        expiryTime = self._buildExpiryOn()
        toSign = '%s\n%s' % (targetUri, expiryTime)
        key = base64.b64decode(self.keyValue.encode('utf-8'))

        if sys.version_info[0] < 3:
            signature = urllib.quote(
                base64.b64encode(
                    hmac.HMAC(key, toSign.encode('utf-8'), hashlib.sha256).digest()
                )
            ).replace('/', '%2F')
        else:
            signature = urllib.parse.quote(
                base64.b64encode(
                    hmac.HMAC(key, toSign.encode('utf-8'), hashlib.sha256).digest()
                )
            ).replace('/', '%2F')

        return self.TOKEN_FORMAT % (signature, expiryTime, self.keyName, targetUri)
    
    def sendD2CMsg(self, deviceId, message):
        sasToken = self._buildIoTHubSasToken(deviceId)
        url = 'https://%s/devices/%s/messages/events?api-version=%s' % (self.iotHost, deviceId, self.API_VERSION)
        r = requests.post(url, headers={'Authorization': sasToken}, data=message)
        return r.text, r.status_code
    
if __name__ == '__main__':

    #Replace <iot_hub_name> and <sas_key> with values obtained from Azure Portal or Device Explorer
    #Ensure you use IoT Hub owner connection string, not a device connection string here.
    connectionString = 'HostName=KHIoTHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=PUbIrbAmPvgcc1kIAW5bDlNQG6/Y7zJSoi6qSiNpcio='
    
    #Replace with deviceId registered with your IoT Hub.
    deviceId = 'Device1'
    
    d2cMsgSender = D2CMsgSender(connectionString)
    sense = SenseHat()
    
    while True:
        #Send temperature from the Sense HAT
        #Refer to Sense HAT API to send other Sense HAT sensor data https://pythonhosted.org/sense-hat/api/
        message = str(sense.temp) 
        print('Sending message... ' + message)
        print(d2cMsgSender.sendD2CMsg(deviceId, message))
        time.sleep(5) # 5 second delay
