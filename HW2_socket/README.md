# HW2_socket
#### This folder contains following two programs.  
- A program in stm32 to read the sensor value, such as 3D Accelerator and 3D gyro and send the data.  
- A Linux/Windows/Mac host receive data send from stm32 and Visualize with some kind of GUI tools.
## 1. STM32 program(`mbedos_socket`)
### 1.1 socket
Run as socket client.
### 1.2 Sensor
Use 3D Accelerator to get the data.
## 2. Host program(`my_socket.py`)
### 2.1 socket
Run as socket server.
### 2.2 GUI
Use matplotlib to plot the data.  
**Blue line** is the data from x-axis of Accelerator.  
**Green line** is the data from y-axis of Accelerator.  
**Red line** is the data from z-axis of Accelerator.

## 3. How to use
### 3.1 STM32 program
1. Modify the IP address and AP’s SSID and password in `mbed-os-sockets/mbed_app.json`
```
"config": {
        "hostname": {
            "value": "\"Your IP address\""
        }
    }
```
```
"target_overrides": {
        "*": {
            "nsapi.default-wifi-security": "WPA_WPA2",
            "nsapi.default-wifi-ssid": "\"SSID\"",
            "nsapi.default-wifi-password": "\"PASSWORD\"",
```

2. Using MbedOS to compile the program.
3. Connect the stm32 to your computer with USB cable and run the program in stm32 and 
### 3.2 Host program
1. Modify the IP address in my_socket.py
```
HOST = 'Your IP address'
```
2. Running `my_socket.py` with python3 and you can see the GUI.


## 4. Reference
- NTUEE Embedded System Labs week3 silde