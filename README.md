# Serial to socket.io proxy

## Download Python

Download Python from https://www.python.org/downloads/

## Python installation

🛑 Make sure to activate **add to PATH** on the first screen of installer

## Python modules

This Python code uses two Python modules:
**pyserial** allows reading data from serial port and **python-socketio** is for sending the same data to Node server.

Install modules with following commands:

```
pip install pyserial
pip install "python-socketio[client]"
```

> ### Note:
> If you want to run this code from WSL you migth need extra configuration for serial port.
> WSL 2 doesn't support serial port communcitaion out of the box. Following this [tutorial](https://devblogs.microsoft.com/commandline/connecting-usb-devices-to-wsl/) it is possible to solve this problem.

## Configuring

You have to figure out which port Arduino is connected to. First connect Arduino with USB cable. In Windows check device manager and ```Ports (COM & LPT)``` shows the port name.  
In Ubuntu use ```lsusb``` command.

If your server runs on differenet address or port change the ```URL``` variable accordingly.

Proxy reads lines from serial port. Line contains ```key``` defining type of the message and value. These two are separated by whitespace.  
In your virtual instrument aplication you have to define what happens if that type of message is received.

Proxy sends event called ```send-data``` to server. It also has data in JSON format.
