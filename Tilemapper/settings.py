# IMPORTS
import pygame as pg
import random as r
from os import *
# Colors (R,G,B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
DARK_GREY = (40,40,40)



game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'img')
snd_folder = path.join(game_folder, 'snd')

WIDTH = 1024
HEIGHT = 768
FPS = 60
BG_COLOR = DARK_GREY
title = "Tilemapper demo"
TILE_SIZE = 32
GRIDWIDTH = WIDTH / TILE_SIZE
GRIDHEIGHT = HEIGHT / TILE_SIZE
PLAYER_SPEED = 300



