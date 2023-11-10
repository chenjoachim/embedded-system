# Program 1
### (a)Modify trigger frequency
Set period from `2000 - 1` to `200000 - 1`.  
The period is 100 times longer than before.  
The frequency is 100 times lower than before.
### (b)Modify sampling time
Set sampling time from `ADC_SAMPLETIME_2CYCLES_5`(2.5 ADC clock cycles) to `ADC_SAMPLETIME_247CYCLES_5`(247.5 ADC clock cycles).  

# Program 2
DMA is implemented here. When the buffer is full or half-full, the program can print out half of the buffer on screen.
![image](https://github.com/chenjoachim/embedded-system/assets/101912090/8dd703dc-4efd-401d-841a-8cf1e5ec70a5)

# Program 3
When the buffer is half-full, pin1 will toggle; when the buffer is full, pin2 will toggle. 
The characteristic can be found using the logic analyzer, and there is (64/2)(buffer size)/16000 = 2ms between each toggle on each pin.
![image](https://github.com/chenjoachim/embedded-system/assets/101912090/4ea197b2-d505-4bbe-b345-ae3db36c0584)
