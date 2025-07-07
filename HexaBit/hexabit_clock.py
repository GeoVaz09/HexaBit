from machine import Pin
import time

# LED setup
Gnd_1 = Pin(6, mode=Pin.OUT, value=0)
LED_1 = Pin(0, mode=Pin.OUT, value=0)
LED_2 = Pin(1, mode=Pin.OUT, value=0)
LED_3 = Pin(2, mode=Pin.OUT, value=0)
LED_4 = Pin(3, mode=Pin.OUT, value=0)
LED_5 = Pin(4, mode=Pin.OUT, value=0)
LED_6 = Pin(5, mode=Pin.OUT, value=0)

# Buttons setup
button_1 = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP)
Gnd_2 = Pin(26, mode=Pin.OUT, value=0)
button_2 = Pin(27, mode=Pin.IN, pull=Pin.PULL_UP)
Gnd_3 = Pin(29, mode=Pin.OUT, value=0)

# Mode pin setup
mode_pin = Pin(12, mode=Pin.IN, pull=Pin.PULL_UP)
Gnd_4 = Pin(13, mode=Pin.OUT, value=0)

def draw_bits(bits):
    LED_6.value(bits[0])
    LED_5.value(bits[1])
    LED_4.value(bits[2])
    LED_3.value(bits[3])
    LED_2.value(bits[4])
    LED_1.value(bits[5])

def draw_number(num):
    if num <= 63 and num >= 0 and isinstance(num, int):
        number = bin(num)[2:]
        binary = list(map(int, str(number)))
        while len(binary) != 6:
            binary.insert(0,0)
        draw_bits(binary)
    else:
        print("Error: The number in this function is not an int or is not between 0 and 63")

hours = 0
minutes = 0


while mode_pin.value() == 0:
    if button_1.value() == 0:
        if hours >= 24:
            hours = 0
        else:
            hours = hours + 1
            time.sleep(0.2)
        draw_number(hours)

    if button_2.value() == 0:
        if minutes >= 60:
            minutes = 0
        else:
            minutes = minutes + 1
            time.sleep(0.2)
        draw_number(minutes)

draw_number(0)

while True:
    for i in range(60):
        if button_1.value() == 0:
            draw_number(hours)
            time.sleep(0.5)
            draw_number(0)
            time.sleep(0.5)

        elif button_2.value() == 0:
            draw_number(minutes)
            time.sleep(0.5)
            draw_number(0)
            time.sleep(0.5)
        else:
            time.sleep(1)
    
    minutes = minutes + 1

    if minutes >= 60:
        minutes = 0
        hours += 1

    if hours >= 24:
        hours = 0
