# Brady Nokes
# PYGAME STARTER TEMPLATE
import pygame as pg
import random

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.speedx = -8
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # if self.rect.left > WIDTH:
        #     self.rect.right = 0
        # if self.rect.right < 0:
        #     self.rect.left = WIDTH
        # if self.rect.top > HEIGHT:
        #     self.rect.bottom = 0
        # if self.rect.bottom < 0:
        #     self.rect.top = HEIGHT

        if self.rect.right < 0:
            self.rect.centery = -15
            self.rect.centerx = WIDTH/2
            self.speedx = 0
            self.speedy = 8

        if self.rect.top > HEIGHT:
            self.rect.centery = HEIGHT/2
            self.rect.centerx = WIDTH + 15
            self.speedy = 0
            self.speedx = -8

        if self.rect.right < 0:
            self.rect.bottom = HEIGHT
            self.speedx = 0
            self.speedy = -8






WIDTH = 360
HEIGHT = 480
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
DARK_ORANGE = (65,34,21)

# for i in range(5):
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     print(color)

pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()

# Create Sprite Groups
all_sprites = pg.sprite.Group()
players_group = pg.sprite.Group()

# Create Game Objects
player = Player()


# Add Objects To Sprite Groups
all_sprites.add(player)
players_group.add(player)

# Game Loop
running = True
while running:
    # Timing Of The Loop
    clock.tick(FPS)

    # Process Input
    # Getting a list of events
    for event in pg.event.get():
        # checking events to perform actions
        if event.type == pg.QUIT:
            running = False

    # Make Updates
    all_sprites.update()


    # Render (Draw)
    screen.fill(DARK_PURP)
    all_sprites.draw(screen)

    # LAST THING IN THE LOOP
    pg.display.flip()


# Exits the game when we break the loop
pg.quit()
