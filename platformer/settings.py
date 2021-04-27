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
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# Player Properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = .8
PLAYER_JUMP = 22

# Game Properties
BOOST_POWER = 60
POW_SPAWN_PCT = 9
ENEMY_FREQ = 5000
PLAYER_LAYER = 2
PLAT_LAYER = 1
POW_LAYER = 1
ENEMY_LAYER = 2
CLOUD_LAYER = 0

TITLE = "Jumpy!"

# Starting Platforms
PLATFORM_LIST = [(0,HEIGHT - 60, ),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4 - 50),
                 (125, HEIGHT - 350),
                 (350, 200),
                 (175, 100)]


# Colors (R,G,B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE
