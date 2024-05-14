import random
from game_assets import *


def randomBallData():
    goal = random.randint(1,6)
    return goal


with open('/Users/fabiolaalston/Desktop/rpi_data.txt', 'rb') as file:
    print(file.read())
