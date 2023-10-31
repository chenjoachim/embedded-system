# HW4_Mbed_ble
This folder contains the following program
* A program in RPi which communicates with a test device, and change some settings such as CCCD values.
* A program writen in MbedOS and run on STM32 which provides the Heartrate Service and the Magnetometer Service.

## 1. ble_scan_connect.py
1. It scans the nearby devices 
2. It connects to the device with the address or name matching that of the test device.
3. It changes the CCCD value of the Heartrate Service and the Magnetometer Service.
4. It receives the data from the device and prints it out.
## 2. BLE_GattServer_AddService
* It provides the Heartrate Service and the Magnetometer Service. 
* Both Heartrate Service and the Magnetometer Service are in notify mode.
## 3. How to use
1. Execute `ble_scan_connect.py`.
2. Select a device with an address or name matching that of the test device.
3. The program will receive the data from the device and print it out.
4. You can see the data from the device in the terminal.

## 4.Reference
* NTUEE embedded system week5 slides.
