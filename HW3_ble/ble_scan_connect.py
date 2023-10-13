# ble_scan_connect.py:
from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate
import binascii
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print ("Discovered device", dev.addr)
        elif isNewData:
            print ("Received new data from", dev.addr)
    def handleNotification(self, cHandle, data):
        print(cHandle, data)
        print ("Notification:", cHandle, "sent data", binascii.b2a_hex(data))

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
#
print ("Services...")
for svc in dev.services:
    print (str(svc))
#
print("")
try:
    testService = dev.getServiceByUUID(UUID(0xaaa0))
    for ch in testService.getCharacteristics():
        print (str(ch))
    #
    print("")
    ch = dev.getCharacteristics(uuid=UUID(0xaaa2))[0]
    if (ch.supportsRead()):
        print (ch.read())
    print("")
    descs = ch.getDescriptors()
    print(str(descs))
    real_desc = None
    for desc in descs:
        print(int.from_bytes(desc.read(), byteorder='little'))
        print(desc.uuid)
        if(str(desc.uuid)[0:8] == "00002902"):
            real_desc = desc
            print("Before writing:", int.from_bytes(desc.read(), byteorder='little'))
            desc.write(0x02.to_bytes(2,'little'))
            print("After writing:", int.from_bytes(desc.read(), byteorder='little'))
                # print(desc.read())
    ch.write(0x66.to_bytes(1,'little'))
    # dev.withDelegate(ScanDelegate(ch.getHandle()))
    while True:
        if dev.waitForNotifications(100):
            # handleNotification() was called
            print("Notification!")
            continue
        # print("After writing:", int.from_bytes(real_desc.read(), byteorder='little'))
        # print(ch.read())
        # print("Waiting...")
    
#
finally:
    dev.disconnect()
