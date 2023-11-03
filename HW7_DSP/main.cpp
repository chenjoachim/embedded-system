#include "ThisThread.h"
#include "mbed.h"
#include "stm32l475e_iot01_accelero.h"
#include <cstdint>
#include "arm_fir.h"
static events::EventQueue event_queue(32 * EVENTS_EVENT_SIZE);
Thread t1;


#define SAMPLE_BUFFER_SIZE  128
int16_t sample_buffer[SAMPLE_BUFFER_SIZE];
float32_t FIRinput[SAMPLE_BUFFER_SIZE];
void PrintFIR(){
    for(int i = 0; i < SAMPLE_BUFFER_SIZE; i++){
        printf("%d.", i);
        printf("%d    ",sample_buffer[i]);
        printf("%f\n",FIRinput[i]);
    }
}
void readGYRO(){
    int16_t pDataXYZ[3] = {0};
    while(1){
        for (int i = 0;i < SAMPLE_BUFFER_SIZE; i++){
            BSP_ACCELERO_AccGetXYZ(pDataXYZ);
            sample_buffer[i] = pDataXYZ[0];
            FIRinput[i] = (float32_t)pDataXYZ[0];
            ThisThread::sleep_for(100);
            
        }
        event_queue.call(do_FIR,FIRinput);
        event_queue.call(PrintFIR);
    }

}
// main() runs in its own thread in the OS
int main()
{
    printf("Hello World!\n");
    t1.start(readGYRO);
    BSP_ACCELERO_Init();
    event_queue.event(&do_FIR);
    event_queue.event(&PrintFIR);
    event_queue.dispatch_forever();

    return 0;
}

