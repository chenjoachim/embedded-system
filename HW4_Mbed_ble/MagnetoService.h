#warning "..."
#ifndef _MAGNETO_SERVICE_H_
#define _MAGNETO_SERVICE_H_

#include "ble/BLE.h"
#include "ble/Gap.h"
#include "ble/GattServer.h"

#if BLE_FEATURE_GATT_SERVER

class MagnetoService {
public:

    MagnetoService(BLE& _ble) :
        ble(_ble),
        magneto_x_Characteristic(GattCharacteristic::UUID_MAGNETO_X_CHAR, &magneto_x, GattCharacteristic::BLE_GATT_CHAR_PROPERTIES_NOTIFY),
        magneto_y_Characteristic(GattCharacteristic::UUID_MAGNETO_Y_CHAR, &magneto_y, GattCharacteristic::BLE_GATT_CHAR_PROPERTIES_NOTIFY),
        magneto_z_Characteristic(GattCharacteristic::UUID_MAGNETO_Z_CHAR, &magneto_z, GattCharacteristic::BLE_GATT_CHAR_PROPERTIES_NOTIFY)
    {
        static bool serviceAdded = false; /* We should only ever need to add the information service once. */
        if (serviceAdded) {
            return;
        }

        GattCharacteristic *charTable[] = { &magneto_x_Characteristic,
                                            &magneto_y_Characteristic,
                                            &magneto_z_Characteristic };

        GattService magnetoService(GattService::UUID_MAGNETO_SERVICE, charTable, sizeof(charTable) / sizeof(charTable[0]));

        ble.gattServer().addService(magnetoService);
        serviceAdded = true;
    }
    void updateMagneto(int16_t newMagneto_x, int16_t newMagneto_y, int16_t newMagneto_z)
    {
        magneto_x = (int16_t) (newMagneto_x);
        magneto_y = (int16_t) (newMagneto_y);
        magneto_z = (int16_t) (newMagneto_z);
        ble.gattServer().write(magneto_x_Characteristic.getValueHandle(), (uint8_t *) &magneto_x, sizeof(int16_t));
        ble.gattServer().write(magneto_y_Characteristic.getValueHandle(), (uint8_t *) &magneto_y, sizeof(int16_t));
        ble.gattServer().write(magneto_z_Characteristic.getValueHandle(), (uint8_t *) &magneto_z, sizeof(int16_t));
    }

    
private:
    BLE& ble;

    int16_t    magneto_x{};
    int16_t    magneto_y{};
    int16_t    magneto_z{};

    ReadOnlyGattCharacteristic<int16_t>    magneto_x_Characteristic;
    ReadOnlyGattCharacteristic<int16_t>    magneto_y_Characteristic;
    ReadOnlyGattCharacteristic<int16_t>    magneto_z_Characteristic;
};
#endif  /* BLE_FEATURE_GATT_SERVER */
#endif  /* #ifndef _MAGNETO_SERVICE_H_ */



