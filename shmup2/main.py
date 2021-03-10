import pygame as pg
import random as r
import math
from os import *


# Game object classes
####################################################################

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 2)
        self.rect.bottom = (HEIGHT - (HEIGHT * .05))
        self.speedx = 0

    def update(self):
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
        # Player Shooting
        # if keystate[pg.K_SPACE]:
        #     self.shoot()
        self.rect.x += self.speedx

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot(self):
        b = Bullet(self.rect.centerx,self.rect.top - 1)
        all_sprites.add(b)
        bullet_group.add(b)

class Bullet(pg.sprite.Sprite):
    def __init__(self,x,y):
        super(Bullet, self).__init__()
        self.image = pg.Surface((5,10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill bullet when it reaches top of screen
        if self.rect.bottom < 0:
            self.kill()




class NPC(pg.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        self.image = pg.Surface((25, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        # self.rect.centerx = (WIDTH / 2)
        # self.rect.top = (0)
        self.rect.x = r.randrange(WIDTH - self.rect.width)
        self.rect.y = r.randrange(-100,-40)
        self.speedy = r.randrange(3,10)
        self.speedx = r.randrange(-1, 1)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = r.randrange(WIDTH - self.rect.width)
            self.rect.y = r.randrange(-100, -40)
            self.speedy = r.randrange(4, 10)







####################################################################


# Game Constants
####################################################################
HEIGHT = 900
WIDTH = 600
FPS = 60

# Colors (R,G,B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

title = "Shmup"

####################################################################
# Game Functions
####################################################################
def spawn_npc():
    npc = NPC()
    npc_group.add(npc)
    all_sprites.add(npc)

# initialize pygame and create window
####################################################################
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()
####################################################################

# load imgs
####################################################################

####################################################################

# create Sprite groups
####################################################################
all_sprites = pg.sprite.Group()
players_group = pg.sprite.Group()
npc_group = pg.sprite.Group()
bullet_group = pg.sprite.Group()
####################################################################

# create Game Objects
####################################################################
player = Player()
for i in range(25):
    n = NPC()
    all_sprites.add(n)
    npc_group.add(n)
bullet = Bullet(WIDTH/2, HEIGHT/2)
npc = NPC()
####################################################################

# add objects to sprite groups
####################################################################
players_group.add(player)
npc_group.add(npc)
all_sprites.add(bullet)
bullet_group.add(bullet)


for i in players_group:
    all_sprites.add(i)
for i in npc_group:
    all_sprites.add(i)

####################################################################


# Game Loop
###################
# game update Variables
########################################
playing = True

########################################
################################################################
while playing:
    # timing
    ##################################################
    clock.tick(FPS)
    ##################################################

    # collecting Input
    ##################################################

    # Quiting the game when we hit the x
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                playing = False
            #Player Shooting
            if event.key == pg.K_SPACE:
                player.shoot()
        if event.type == pg.QUIT:
            playing = False

    ##################################################
    # Update
    ##################################################
    # checking for hit between player and npc

    hits = pg.sprite.spritecollide(player,npc_group,True)
    if hits:
        spawn_npc()
        #playing = False
    # Bullet Hits NPC
    hits = pg.sprite.groupcollide(npc_group, bullet_group, True, True)
    for hit in hits:
        spawn_npc()

    all_sprites.update()
    ##################################################
    # Render
    ##################################################

    screen.fill(BLACK)
    all_sprites.draw(screen)

    pg.display.flip()
    ##################################################

pg.quit()
################################################################
#####################