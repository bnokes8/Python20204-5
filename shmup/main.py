# SHMUP GAME BRADY NOKES

# IMPORTS
import pygame as pg
import random as r
import math as m
from os import *

# Game object classes---------------------------
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50,40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = (HEIGHT-(HEIGHT*.05))
        self.speedx = 0
        self.speedy = 0

    def toggle_pressed(self):
        self.key_pressed = False

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Basic Movement
        self.speedx = 0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.speedx = -5
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.speedx = 5
        if keystate[pg.K_DOWN] or keystate[pg.K_s]:
            self.speedy = 5
        if keystate[pg.K_UP] or keystate[pg.K_w]:
            self.speedy = -5
        if keystate[pg.K_KP5]:
            self.rect.center = (WIDTH/2,HEIGHT/2)

        # BIND PLAYER TO SCREEN
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT



class NPC(pg.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        self.image = pg.Surface((25,25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.top = (0)
        self.speedx = 0
        self.speedy = 0
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        self.speedy = 3.75


        
#-----------------------------------------------


# GAME CONSTANTS---------------------------------
title = "Shmup"
WIDTH = 600
HEIGHT = 900
FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)




# GAME SETUP------------------------------------
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()
#-----------------------------------------------
# Load Images
pass
#-----------------------------------------------

#-----------------------------------------------
# Create Sprite Groups
all_sprites = pg.sprite.Group()
players_group = pg.sprite.Group()
npc_group = pg.sprite.Group()
#-----------------------------------------------
# Create Game Objects
player = Player()
npc = NPC()
#-----------------------------------------------
#-----------------------------------------------
# Add Objects to Sprite Groups
players_group.add(player)
npc_group.add(npc)


for i in players_group:
    all_sprites.add(i)
for i in npc_group:
    all_sprites.add(i)

# GAME LOOP-------------------------------------

# Game Update Variables
playing = True
score = 0
level = 1
diff = 0
#-----------------------------------------------
# Play Loop
while playing:

    # TIMING
    clock.tick(FPS)
    #-------------------------------------------

    # GET INPUT
    # Quiting the game when we hit x or hits escape
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                playing = False

    #-------------------------------------------
    # UPDATE
    all_sprites.update()
    #-------------------------------------------

    # RENDER
    screen.fill(BLACK)
    all_sprites.draw(screen)


    pg.display.flip()
    #-------------------------------------------

    #-------------------------------------------

pg.QUIT
