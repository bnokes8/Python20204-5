# Brady Nokes
# PYGAME STARTER TEMPLATE
import pygame as pg
import random
import math
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"imgs")
player_imgs = os.path.join(img_folder,"playerimgs")
sound_folder = os.path.join(game_folder,"snds")
textdata_folder = os.path.join(game_folder,"text_data")


class NPC(pg.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        self.image = pg.Surface((15, 15))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        #self.rect.center = (-25, -25)
        self.speedx = 6
        self.speedy = 6
        # The "center" the sprite will orbit
        self.center_x = self.rect.centerx
        self.center_y = self.rect.centery
        # Current Angle in radians
        self.angle = 1
        # How far away from the center to orbit
        self.radius = 75
        # How fast to orbit, radians per frame
        self.speed = .1

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        #Circle Movement
        # if self.angle <= 6.25:
        #     self.rect.centerx = self.radius * math.sin(self.angle)+self.center_x
        #     self.rect.centery = self.radius * math.cos(self.angle)+self.center_y
        #     self.angle += self.speed

        # Bouncing
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speedx *= -1

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speedy *= -1






        # if self.rect.left > WIDTH:
        #     self.rect.right = 0
        # if self.rect.right < 0:
        #     self.rect.left = WIDTH
        # if self.rect.top > HEIGHT:
        #     self.rect.bottom = 0
        # if self.rect.bottom < 0:
        #     self.rect.top = HEIGHT

        # if self.rect.right < 0:
        #     self.rect.centery = -15
        #     self.rect.centerx = WIDTH/2
        #     self.speedx = 0
        #     self.speedy = 8
        #
        # if self.rect.top > HEIGHT:
        #     self.rect.centery = HEIGHT/2
        #     self.rect.centerx = WIDTH + 15
        #     self.speedy = 0
        #     self.speedx = -8
        #
        # if self.rect.right < 0:
        #     self.rect.bottom = HEIGHT
        #     self.speedx = 0
        #     self.speedy = -8
        #
        # if self.rect.bottom < 0:
        #     self.rect.centery = HEIGHT / 2
        #     self.rect.centerx = 0
        #     self.speedx = 8
        #     self.speedy = 0
        # if self.rect.right > WIDTH:
        #     self.speedx = 0
        #     self.speedy = -10
        #     #print("test")
        #
        # if self.rect.top < 0:
        #     self.speedx = -10
        #     self.speedy = 0
        #
        # if self.rect.left < 0:
        #     self.speedx = 0
        #     self.speedy = 10
        #
        # if self.rect.bottom > HEIGHT and not self.rect.right > WIDTH:
        #     self.speedx = 10
        #     self.speedy = 0

        # if self.rect.centerx > WIDTH/2:
        #     self.speedy = 10
        #     self.speedx = -6
        #
        # if self.rect.top > HEIGHT:
        #     self.speedy = 0
        #     self.speedx = -6
        #     self.rect.center = (-25, -25)
        #
        # if self.rect.center == (-25, -25):
        #     self.speedy = 6
        #     self.speedx = 6

# class Player(pg.sprite.Sprite):
#     def __init__(self):
#         super(Player, self).__init__()
#         # self.image = pg.Surface((50, 50))
#         # self.image.fill(BLUE)
#         self.image = player_img
#         #self.image.set_colorkey(WHITE)
#         self.rect = self.image.get_rect()
#         self.rect.center = (WIDTH / 2, HEIGHT / 2)
#         # self.rect.center = (-25, -25)
#         self.speedx = 0
#         self.speedy = 0
#         self.key_pressed = False
#
#
#     def toggle_pressed(self):
#         self.key_pressed = False
#
#
#
#     def update(self):
#
#         # Mouse Movement
#         if mb_held == True:
#             self.rect.center = (mousex, mousey)
#         # self.rect.centerx = (mousex)
#         # self.rect.centery = (mousey)
#
#
#         # Grid Movement
#         keystate = pg.key.get_pressed()
#         # if keystate[pg.K_LEFT] and self.key_pressed == False:
#         #     self.key_pressed = True
#         #     self.rect.centerx += -50
#         # if keystate[pg.K_RIGHT] and self.key_pressed == False:
#         #     self.key_pressed = True
#         #     self.rect.centerx += 50
#         # if keystate[pg.K_DOWN] and self.key_pressed == False:
#         #     self.key_pressed = True
#         #     self.rect.centery += 50
#         # if keystate[pg.K_UP] and self.key_pressed == False:
#         #     self.key_pressed = True
#         #     self.rect.centery += -50
#         if keystate[pg.K_KP5]:
#             self.rect.center = (WIDTH/2,HEIGHT/2)
#
#
#
#         # Basic Movement
#         # self.speedx = 0
#         # self.speedy = 0
#         # keystate = pg.key.get_pressed()
#         # if keystate[pg.K_LEFT] or keystate[pg.K_a]:
#         #     self.speedx = -5
#         # if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
#         #     self.speedx = 5
#         # if keystate[pg.K_DOWN] or keystate[pg.K_s]:
#         #     self.speedy = 5
#         # if keystate[pg.K_UP] or keystate[pg.K_w]:
#         #     self.speedy = -5
#         # if keystate[pg.K_KP5]:
#         #     self.rect.center = (WIDTH/2,HEIGHT/2)
#         self.rect.x += self.speedx
#         self.rect.y += self.speedy
#
#         # BIND PLAYER TO SCREEN
#         if self.rect.left <= 0:
#             self.rect.left = 0
#         if self.rect.right >= WIDTH:
#             self.rect.right = WIDTH
#         if self.rect.top <= 0:
#             self.rect.top = 0
#         if self.rect.bottom >= HEIGHT:
#             self.rect.bottom = HEIGHT


def spawn_player(x,y):
    '''spawns a player'''
    newplayer = Player()
    newplayer.rect.center = (x, y)
    newplayer.speedy = random.randint(-10,10)
    newplayer.speedx = random.randint(-10,10)
    all_sprites.add(newplayer)
    players_group.add(newplayer)









WIDTH = 400
HEIGHT = 400
FPS = 30

title = "Template"

# Colors (R,G,B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (5,48,52)
DARK_PURP = (88,22,66)
SOFT_BLUE = (45,53,86)
DEEP_BLUE = (12,34,56)
DARK_ORANGE = (90,34,10)
mb_held = False



# for i in range(5):
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     print(color)

# pg.init()
# pg.mixer.init()
#
# screen = pg.display.set_mode((WIDTH, HEIGHT))
# pg.display.set_caption(title)
# clock = pg.time.Clock()

# Load In Images
player_img = pg.image.load(os.path.join(player_imgs,"player.png")).convert()


# Create Sprite Groups
# all_sprites = pg.sprite.Group()
# players_group = pg.sprite.Group()
npc_group = pg.sprite.Group()

# Create Game Objects
npc = NPC()
player = Player()


# Add Objects To Sprite Groups
all_sprites.add(npc)
players_group.add(npc)
npc_group.add(player)
all_sprites.add(player)

# Game Loop
running = True
while running:
    # Timing Of The Loop
    clock.tick(FPS)

    # Process Input
    # Getting a list of events

    mousex,mousey = pg.mouse.get_pos()

    # for event in pg.event.get():

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                player.toggle_pressed()
            if event.key == pg.K_UP or event.key == pg.K_DOWN:
                player.toggle_pressed()

        if event.type == pg.MOUSEBUTTONDOWN and player.rect.collidepoint(pg.mouse.get_pos()):
            x = pg.mouse.get_pressed()
            if x[0]:
                print("clicked left button")
                mb_held = True
            if x[1]:
                print("clicked mouse wheel")
            if x[2]:
                print("clicked right button")
                spawn_player(mousex, mousey)
        if event.type == pg.MOUSEBUTTONUP and mb_held == True:
            if x[0]:
                mb_held = False



        # Fluid Movement
        # if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_LEFT:
        #         player.speedx = -5
        #     if event.key == pg.K_RIGHT:
        #         player.speedx = 5
        #     if event.key == pg.K_UP:
        #         player.speedy = -5
        #     if event.key == pg.K_DOWN:
        #         player.speedy = 5
        #     if event.key == pg.K_KP5:
        #         player.rect.center = (WIDTH/2,HEIGHT/2)


            # Basic Grid Movement
            # if event.key == pg.K_KP1:
            #     player.rect.x -= 50
            #     player.rect.y += 50
            # if event.key == pg.K_KP3:
            #     player.rect.x += 50
            #     player.rect.y += 50
            # if event.key == pg.K_KP7:
            #     player.rect.x -= 50
            #     player.rect.y -= 50
            # if event.key == pg.K_KP9:
            #     player.rect.x += 50
            #     player.rect.y -= 50
            # if event.key == pg.K_KP5:
            #     player.rect.center = (WIDTH/2,HEIGHT/2)
            #
            # if event.key == pg.K_LEFT or event.key == pg.K_a or event.key == pg.K_KP4:
            #     player.rect.x -= 50
            # if event.key == pg.K_RIGHT or event.key == pg.K_d or event.key == pg.K_KP6:
            #     player.rect.x += 50
            # if event.key == pg.K_UP or event.key == pg.K_w or event.key == pg.K_KP8:
            #     player.rect.y -= 50
            # if event.key == pg.K_DOWN or event.key == pg.K_s or event.key == pg.K_KP2:
            #     player.rect.y += 50

        # Fluid Movement
        # if event.type == pg.KEYUP:
        #     if event.key == pg.K_LEFT:
        #         player.speedx = 0
        #     if event.key == pg.K_RIGHT:
        #         player.speedx = 0
        #     if event.key == pg.K_UP:
        #         player.speedy = 0
        #     if event.key == pg.K_DOWN:
        #         player.speedy = 0


        # checking events to perform actions
        if event.type == pg.QUIT:
            running = False

    # Make Updates
    all_sprites.update()


    # Render (Draw)
    screen.fill(DARK_PURP)
    all_sprites.draw(screen)

    # LAST THING IN THE LOOP
    #pg.display.flip()


# Exits the game when we break the loop
pg.quit()
