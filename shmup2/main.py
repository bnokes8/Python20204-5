# ATTRIBUTIONS
# Kids Can Code Original Game Designer (kidscancode.org)
# Code Created by : Brady Nokes
# Art Created by : www.kenney.nl
#


import pygame as pg
import random as r
import math
from os import *


# Game object classes
####################################################################

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.shield = 100
        self.fuel = 100
        # self.image = pg.Surface((50, 40))
        # self.image.fill(GREEN)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(self.image, (75,55))
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * .75 / 2
        if debug:
            pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = (WIDTH / 2)
        self.rect.bottom = (HEIGHT - (HEIGHT * .05))
        self.speedx = 0
        self.shoot_delay = 250
        self.last_shot = pg.time.get_ticks()

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if (keystate[pg.K_LEFT] or keystate[pg.K_a]) and self.fuel > 0:
            self.speedx = -5
            self.fuel -= .025
        if (keystate[pg.K_RIGHT] or keystate[pg.K_d]) and self.fuel > 0:
            self.speedx = 5
            self.fuel -= .025
        if keystate[pg.K_SPACE]:
            player.shoot()
        # if keystate[pg.K_DOWN] or keystate[pg.K_s]:
        #     self.speedy = 5
        #     self.fuel -= 2
        # if keystate[pg.K_UP] or keystate[pg.K_w]:
        #     self.speedy = -5
        #     self.fuel -= 2
        # if keystate[pg.K_KP5]:
        #     self.rect.center = (WIDTH/2,HEIGHT/2)
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
        now = pg.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            b = Bullet(self.rect.centerx,self.rect.top - 1)
            all_sprites.add(b)
            bullet_group.add(b)
            #shoot_sound.play()

class Bullet(pg.sprite.Sprite):
    def __init__(self,x,y):
        super(Bullet, self).__init__()
        # self.image = pg.Surface((5,10))
        # self.image.fill(BLUE)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(self.image, (8,50))
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * .75 / 2
        if debug:
            pg.draw.circle(self.image, BLUE, self.rect.center, self.radius)
        self.rect.centerx = x
        self.rect.centery = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill bullet when it reaches top of screen
        if self.rect.bottom < 0:
            self.kill()



# EXPLOSIONS
class Explosions(pg.sprite.Sprite):

    def __init__(self, center, size):
        super(Explosions, self).__init__()
        self.size = size
        self.image = exp_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 50


    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame - len(exp_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = exp_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class NPC(pg.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        # self.image = pg.Surface((25, 30))
        # self.image.fill(RED)
        self.image = npc_img


        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(self.image,(75,75))
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * .75/2
        if debug:
            pg.draw.circle(self.image, RED, self.rect.center, self.radius)
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
font_name = pg.font.match_font('arial')

# Colors (R,G,B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

debug = False

title = "Shmup"
# FOLDER VARIABLES
game_folder = path.dirname(__file__)
imgs_folder = path.join(game_folder,"imgs")
snds_folder = path.join(game_folder,"snds")
scores_folder = path.join(game_folder,"scores")
background_folder = path.join(imgs_folder,"backgrounds")
player_folder = path.join(imgs_folder,"player")
enemy_img_folder = path.join(imgs_folder,"enemies")
animation_folder = path.join(imgs_folder, "animations")
#

####################################################################
# Game Functions
####################################################################
def spawn_npc():
    npc = NPC()
    npc_group.add(npc)
    all_sprites.add(npc)


def draw_bar(surf,x,y,pct,color):
    if pct < 0:
        pct = 0
    b_len = 180
    b_height = 40
    fill = (pct/100*b_len)
    outline = pg.Rect(x,y,b_len,b_height)
    fill_rect = pg.Rect(x,y,fill,b_height)
    pg.draw.rect(surf,color,fill_rect)
    pg.draw.rect(surf, WHITE, outline, 3)


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
background = pg.image.load(path.join(background_folder,"bgpurple.png")).convert()
bg_rect = background.get_rect()
npc_img = pg.image.load(path.join(enemy_img_folder,"meteormedium.png")).convert()
player_img = pg.image.load(path.join(player_folder,"playergreen.png")).convert()
bullet_img = pg.image.load(path.join(player_folder,"bulletred.png")).convert()



exp_anim = {}
exp_anim["lg"] = []
exp_anim["sm"] = []
for i in range(9):
    filename = "regularExplosion0{}.png".format(i)
    img = pg.image.load(path.join(animation_folder,filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pg.transform.scale(img, (100, 1000))
    exp_anim["lg"].append(img_lg)
    img_sm = pg.transform.scale(img, (75, 75))
    exp_anim["sm"].append(img_lg)




####################################################################
# Load Snds
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

            if event.key == pg.K_F12:
                debug = True

        if event.type == pg.QUIT:
            playing = False

    ##################################################
    # Update
    ##################################################0
    # checking for hit between player and npc

    hits = pg.sprite.spritecollide(player,npc_group,True,pg.sprite.collide_circle)
    if hits:
        exp = Explosions(hits[0].rect.center,"sm")
        all_sprites.add(exp)
        #r.choice(expl_snds).play()
        spawn_npc()
        player.shield -= hits[0].radius*2
        print(player.shield)
        if player.shield >= 0:
            exp = Explosions(player.rect.center,"lg")
            all_sprites.add(exp)
            player.kill()
            playing = False

        #playing = False
    # Bullet Hits NPC
    hits = pg.sprite.groupcollide(npc_group, bullet_group, True, True,pg.sprite.collide_circle)
    for hit in hits:
        exp = Explosions(hit.rect.center,"sm")
        all_sprites.add(exp)
        spawn_npc()

    all_sprites.update()
    ##################################################
    # Render
    ##################################################
    screen.fill(BLACK)
    screen.blit(background,bg_rect)
    all_sprites.draw(screen)
    # Draw HUD

    draw_bar(screen, 5, 15, player.shield, GREEN)

    draw_bar(screen, 5, 55, player.fuel, BLUE)

    pg.display.flip()
    ##################################################

pg.quit()
################################################################
#####################