# IMPORTS
import pygame as pg
import random as r
from os import *

game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'img')
snd_folder = path.join(game_folder, 'snd')

WIDTH = 480
HEIGHT = 600
FPS = 60

# Player Properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12

title = "Jumpy!"


# Colors (R,G,B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
