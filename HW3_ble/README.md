# HW3_BLE
This folder contains the following program
* A program in RPi which communicates with a test device, and change some settings such as CCCD values.

## 1. ble_scan_connect.py
### 1.1 scanner
* scans the nearby devices.

### 1.2 writer
* writes data into the test device.

## 2. How to use
1. Advertise test device for RPi sensing.
2. Execute ble_scan_connect.py.
3. Select a device with an address matching that of the test device.
4. Verify if the CCCD settings are successfully modified.

## 3.Reference
* NTUEE embedded system week4 slides.
