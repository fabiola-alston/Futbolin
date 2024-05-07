from tkinter import *
from tkmacosx import *
from PIL import Image, ImageTk
import pygame
import random
import time
import serial

pygame.mixer.init()

# raspberry pi port id
rpi = serial.Serial(port="/dev/cu.usbmodem1301", baudrate=115200)

try:
    rpi.Open()
    print("connected 1")
except:
    if rpi.isOpen():
        print("connected 2")
    else:
        print("not connected")

while True:
    if rpi.isOpen():
        dt = rpi.readline()
        dt_str = dt.decode('UTF-8')
    print(dt_str)
    time.sleep(0.2)

# select sound function
def selectSound():
    sound = pygame.mixer.Sound("Sounds/select.wav")
    sound.set_volume(0.5)
    pygame.mixer.Sound.play(sound)

def shootSound():
    sound = pygame.mixer.Sound("Sounds/shoot.wav")
    sound.set_volume(0.5)
    pygame.mixer.Sound.play(sound)

def dullSound():
    sound = pygame.mixer.Sound("Sounds/err.wav")
    sound.set_volume(0.5)
    pygame.mixer.Sound.play(sound)

def cheerSound():
    sound = pygame.mixer.Sound("Sounds/cheer.mp3")
    sound.set_volume(0.5)
    pygame.mixer.Sound.play(sound)

def booSound():
    sound = pygame.mixer.Sound("Sounds/boo.mp3")
    sound.set_volume(0.5)
    pygame.mixer.Sound.play(sound)

# fonts
font1 = ("retro gaming", 16)
font2 = ("retro gaming", 14)
font3 = ("retro gaming", 24)

# selected team variable
# 0 = samurai blue
# 1 = real madrid
# 2 = manchester united
SELECTED_TEAM = 2

# selected goalie
SELECTED_GOALIE = 3

# selected attacker
SELECTED_ATTACKER = 2

# GAME MODE (MANUAL 1 - AUTOMATIC 2)
GAME_MODE = 1

# GOALIE MODE (AN1 - AN2 - AN3)
GOALIE_MODE = 2

# TEAM 2 (RANDOMLY GENERATED)
SELECTED_TEAM2 = 1
SELECTED_ATTACKER2 = 1
SELECTED_GOALIE2 = 1