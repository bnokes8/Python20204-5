# IMPORTS
import pygame as pg
import random as r
from os import *

game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'img')
snd_folder = path.join(game_folder, 'snd')

WIDTH = 600
HEIGHT = 850
FPS = 60

title = "Template"

# Player Properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 15



# Colors (R,G,B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
C1 = r.randint(1, 256)
C2 = r.randint(1, 256)
C3 = r.randint(1, 256)
RAN_COLOR = (C1, C2, C3)
