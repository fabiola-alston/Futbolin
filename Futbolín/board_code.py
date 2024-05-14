from machine import *
import utime

paleta1 = Pin(19, Pin.IN, Pin.PULL_UP)
paleta2 = Pin(20, Pin.IN, Pin.PULL_UP)
paleta3 = Pin(18, Pin.IN, Pin.PULL_UP)
paleta4 = Pin(13, Pin.IN, Pin.PULL_UP)
paleta5 = Pin(11, Pin.IN, Pin.PULL_UP)
paleta6 = Pin(12, Pin.IN, Pin.PULL_UP)

led1 = Pin(17, Pin.OUT)
led2 = Pin(21, Pin.OUT)
led3 = Pin(22, Pin.OUT)
led4 = Pin(14, Pin.OUT)
led5 = Pin(10, Pin.OUT)
led6 = Pin(9, Pin.OUT)

PALETTE = 0

def updatePalVal(val):
    print("yes")
    with open('rpi_data.txt', 'wb') as file:
        file.write(str(val))

while True:
    if paleta1.value() == 0:
        PALETTE = 1
        led1.value(1)
        print(PALETTE)
        updatePalVal(PALETTE)
        utime.sleep(1)
    else:
        led1.value(0)

    if paleta2.value() == 0:
        PALETTE = 2
        led2.value(1)
        print(PALETTE)
        updatePalVal(PALETTE)
        utime.sleep(1)
    else:
        led2.value(0)

    if paleta3.value() == 0:
        PALETTE = 3
        led3.value(1)
        print(PALETTE)
        updatePalVal(PALETTE)
        utime.sleep(1)
    else:
        led3.value(0)

    if paleta4.value() == 0:
        PALETTE = 4
        led4.value(1)
        print(PALETTE)
        updatePalVal(PALETTE)
        utime.sleep(1)
    else:
        led4.value(0)

    if paleta5.value() == 0:
        PALETTE = 5
        led5.value(1)
        print(PALETTE)
        updatePalVal(PALETTE)
        utime.sleep(1)
    else:
        led5.value(0)

    if paleta6.value() == 0:
        PALETTE = 6
        led6.value(1)
        print(PALETTE)
        updatePalVal(PALETTE)
        utime.sleep(1)
    else:
        led6.value(0)

    utime.sleep(0.5)


