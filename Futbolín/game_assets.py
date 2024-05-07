from tkinter import *
from tkmacosx import *
from PIL import Image, ImageTk
import pygame
import random
import time

pygame.mixer.init()


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