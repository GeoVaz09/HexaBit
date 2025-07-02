from machine import Pin
import time

# Led module setup
Gnd_1 = Pin(6, mode=Pin.OUT, value=0)
LED_1 = Pin(0, mode=Pin.OUT, value=0)
LED_2 = Pin(1, mode=Pin.OUT, value=0)
LED_3 = Pin(2, mode=Pin.OUT, value=0)
LED_4 = Pin(3, mode=Pin.OUT, value=0)
LED_5 = Pin(4, mode=Pin.OUT, value=0)
LED_6 = Pin(5, mode=Pin.OUT, value=0)

# button input setup
button_1 = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP)
Gnd_2 = Pin(26, mode=Pin.OUT, value=0)
button_2 = Pin(27, mode=Pin.IN, pull=Pin.PULL_UP)
Gnd_3 = Pin(29, mode=Pin.OUT, value=0)



def draw_bits(bits):
    LED_6.value(bits[0])
    LED_5.value(bits[1])
    LED_4.value(bits[2])
    LED_3.value(bits[3])
    LED_2.value(bits[4])
    LED_1.value(bits[5])

#/////////////////////////////////////

# test draw_bits() function

# test = [0,0,0,1,0,1]
# draw_bits(test)

#/////////////////////////////////////

def draw_number(num):
    if num <= 63 and num >= 0 and isinstance(num, int):
        number = bin(num)[2:]
        binary = list(map(int, str(number)))
        while len(binary) != 6:
            binary.insert(0,0)
        draw_bits(binary)
    else:
        print("Error: The number in this function is not an int or is not between 0 and 63")

#/////////////////////////////////////

# test draw_number() function

# draw_number(7)

#/////////////////////////////////////



#/////////////////////////////////////
# Apps for HexaBit:
#/////////////////////////////////////

# 1) Stopwatch
# 2) Counter with buttons
# 3) Timer (1 minute)
# 4) Timer (1 hour)


#/////////////////////////////////////