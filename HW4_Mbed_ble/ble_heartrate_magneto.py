# ble_scan_connect.py:
from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate
import binascii
import time

HANDLE_HEARTRATE = 13
HANDLE_MAGNETOX = 19
HANDLE_MAGNETOY = 22
HANDLE_MAGNETOZ = 25

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
        elif isNewData:
            print ("Received new data from", dev.addr)
    def handleNotification(self, cHandle, data):
        if(cHandle == HANDLE_HEARTRATE):
            print ("Heart rate:", int.from_bytes(data, byteorder='big'), "(bpm)")
        elif(cHandle == HANDLE_MAGNETOX):
            print ("MAGNETOX:", int.from_bytes(data, byteorder='little', signed=True), '(mgauss)')
        elif(cHandle == HANDLE_MAGNETOY):
            print ("MAGNETOY:", int.from_bytes(data, byteorder='little', signed=True), '(mgauss)')
        elif(cHandle == HANDLE_MAGNETOZ):
            print ("MAGNETOZ:", int.from_bytes(data, byteorder='little', signed=True), '(mgauss)')


scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)
n=0
addr = []
for dev in devices:
    print ("%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr,
    dev.addrType, dev.rssi))
    addr.append(dev.addr)
    n += 1
    for (adtype, desc, value) in dev.getScanData():
        print (" %s = %s" % (desc, value))
number = input('Enter your device number: ')
print ('Device', number)
num = int(number)
print (addr[num])
#
print ("Connecting...")
dev = Peripheral(addr[num], 'random')
dev.withDelegate(ScanDelegate())
#
print ("Services...")
for svc in dev.services:
    print (str(svc))
#
print("")
try:
    heartrate = dev.getCharacteristics(uuid=UUID(0x2a37))[0]
    descs = heartrate.getDescriptors()
    print(descs)
    for desc in descs:
        print(int.from_bytes(desc.read(), byteorder='little'))
        if(str(desc.uuid)[0:8] == "00002902"):
            print("Before writing:", int.from_bytes(desc.read(), byteorder='little'))
            desc.write(0x01.to_bytes(2,'little'))
            print("After writing:", int.from_bytes(desc.read(), byteorder='little'))
    testService = dev.getServiceByUUID(UUID(0x3a00))
    for ch in testService.getCharacteristics():
        print (str(ch))
    #
    print("")
    magneto = {}
    magneto['x'] = dev.getCharacteristics(uuid=UUID(0x3a01))[0]
    magneto['y'] = dev.getCharacteristics(uuid=UUID(0x3a03))[0]
    magneto['z'] = dev.getCharacteristics(uuid=UUID(0x3a05))[0]
    for axis in ['x', 'y', 'z']:
        # if (magneto[axis].supportsRead()):
        #     print ('MAGNETO' + axis + ' = ' + str(int.from_bytes(magneto[axis].read(), byteorder='little', signed=True))+' (mgauss)')
        descs = magneto[axis].getDescriptors()
        # print(descs)
        for desc in descs:
            print(int.from_bytes(desc.read(), byteorder='little'))
            if(str(desc.uuid)[0:8] == "00002902"):
                # print("Before writing:", int.from_bytes(desc.read(), byteorder='little'))
                desc.write(0x01.to_bytes(2,'little'))
                # print("After writing:", int.from_bytes(desc.read(), byteorder='little'))

            
    while True:
        # time.sleep(1)
        # for axis in ['x', 'y', 'z']:
        #     if (magneto[axis].supportsRead()):
        #         print ('MAGNETO' + axis + ' = ' + str(int.from_bytes(magneto[axis].read(), byteorder='little', signed=True))+' (mgauss)')
        if dev.waitForNotifications(10):
            continue
        # print("After writing:", int.from_bytes(real_desc.read(), byteorder='little'))
        # print(ch.read())
        # print("Waiting...")
    
#
finally:
    dev.disconnect()
