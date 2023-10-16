# HW3_BLE
This folder contains the following program
* A program in RPi which communicates with a test device, and change some settings such as CCCD values.

## 1. ble_scan_connect.py
* It scans the nearby devices and shows "Notification!" when receiving one.

## 2. How to use
1. Advertise test device for RPi sensing. NRF connect in Android can do this.
2. Execute ble_scan_connect.py.
3. Select a device with an address or name matching that of the test device.
4. Verify if the CCCD value on the device are successfully modified.
5. Modify the data using the "notification/indication" button in app. The command line should show up "Notification!"

## 3.Reference
* NTUEE embedded system week4 slides.
