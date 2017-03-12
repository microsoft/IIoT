
var connectionString = 'HostName=Trak-IoT-Hub-Free.azure-devices.net;DeviceId=RaspberryPi;SharedAccessKey=Kj8PlWxtSYpeCCLfVcbLxaBgYHteCPRAi+9yrbn4Fo0=';
// Example: HostName=<IoT Hub Name>.azure-devices.net;DeviceId=<Device Name>;SharedAccessKey=<Device Key>


// use factory function from AMQP-specific package
var clientFromConnectionString = require('azure-iot-device-amqp').clientFromConnectionString;

// AMQP-specific factory function returns Client object from core package
var client = clientFromConnectionString(connectionString);

// use Message object from core package
var Message = require('azure-iot-device').Message;

var connectCallback = function (err) {
    if (err) {
        console.error('Could not connect: ' + err);
    } else {
        console.log('Client connected');
	i = 0;
	var msg = '';
		i = i + Math.random();
        	msg = new Message('{' + i + '}');
        	client.sendEvent(msg, function (err) {
            		if (err) {
                		console.log(err.toString());
            		} else {
                		console.log('Message sent');
            		};
        	});
    };
};


client.open(connectCallback);

console.log('Waiting for send');
setTimeout(exitProcessing, 30000)


function exitProcessing()
{
	console.log('Process complete');
	process.exit()
}