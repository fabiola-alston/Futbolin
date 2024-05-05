from tkinter import *
from tkmacosx import *
from PIL import Image, ImageTk
import pygame

pygame.mixer.init()


# select sound function
def selectSound():
    sound = pygame.mixer.Sound("Sounds/select.wav")
    sound.set_volume(0.5)
    pygame.mixer.Sound.play(sound)


# fonts
font1 = ("retro gaming", 16)

# selected team variable
# 0 = samurai blue
# 1 = real madrid
# 2 = manchester united
SELECTED_TEAM = 0

# selected goalie
SELECTED_GOALIE = 0

# selected attacker
SELECTED_ATTACKER = 0