import board
import digitalio
import time
# import analogio
import _thread
import utime
from machine import Pin


#GLOBALS

A = False
B = False
C = False
D = False
E = False
F = False
G = False

# DATOS POR MANDAR


#PALETAS

paleta1 = digitalio.DigitalInOut(board.GP19)
paleta1.direction = digitalio.Direction.INPUT

paleta2 = digitalio.DigitalInOut(board.GP20)
paleta2.direction = digitalio.Direction.INPUT

paleta3 = digitalio.DigitalInOut(board.GP18)
paleta3.direction = digitalio.Direction.INPUT

paleta4 = digitalio.DigitalInOut(board.GP13)
paleta4.direction = digitalio.Direction.INPUT

paleta5 = digitalio.DigitalInOut(board.GP11)
paleta5.direction = digitalio.Direction.INPUT

paleta6 = digitalio.DigitalInOut(board.GP12)
paleta6.direction = digitalio.Direction.INPUT

#LEDS

LedLocal = digitalio.DigitalInOut(board.GP16)
LedLocal.direction = digitalio.Direction.OUTPUT

LedVisitor = digitalio.DigitalInOut(board.GP15)
LedVisitor.direction = digitalio.Direction.OUTPUT

Led1 = digitalio.DigitalInOut(board.GP17)
Led1.direction = digitalio.Direction.OUTPUT

Led2 = digitalio.DigitalInOut(board.GP21)
Led2.direction = digitalio.Direction.OUTPUT

Led3 = digitalio.DigitalInOut(board.GP22)
Led3.direction = digitalio.Direction.OUTPUT

Led4 = digitalio.DigitalInOut(board.GP14)
Led4.direction = digitalio.Direction.OUTPUT

Led5 = digitalio.DigitalInOut(board.GP10)
Led5.direction = digitalio.Direction.OUTPUT

Led6 = digitalio.DigitalInOut(board.GP9)
Led6.direction = digitalio.Direction.OUTPUT

#BOTON

boton = digitalio.DigitalInOut(board.GP3)
boton.switch_to_input(pull=digitalio.Pull.UP)

#POTENCIOMETRO

# potenciometro = analogio.AnalogIn(board.GP28)

#DEFINIR ACCIONES

while True:
    if paleta1.value == False:
        A = True
        Led1.value = True
        time.sleep(3)
        Led1.value = False
        A = False
    if paleta2.value == False:
        B = True
        Led2.value = True
        time.sleep(3)
        Led2.value = False
        B = False
    if paleta3.value == False:
        C = True
        Led3.value = True
        time.sleep(3)
        Led3.value = False
        C = False
    if paleta4.value == False:
        D = True
        Led4.value = True
        time.sleep(3)
        Led4.value = False
        D = False
    if paleta5.value == False:
        E = True
        Led5.value = True
        time.sleep(3)
        Led5.value = False
        E = False
    if paleta6.value == False:
        F = True
        Led6.value = True
        time.sleep(3)
        Led6.value = False
        F = False
        if boton.value == True:
            G = True

    time.sleep(0.5)

