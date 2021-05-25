# Flappy Bird by Brady Nokes, adapted from Sai Anish Malla ( https://youtu.be/rO_UU_Uu8EQ )

# Imports
import pygame as pg
from settings import *
import random as r

pg.init()

screen = pg.display.set_mode((500, 750))

BG_IMAGE = pg.image.load('imgs/background.jpg')

# BIRD
BIRD_IMAGE = pg.image.load('imgs/bird1.png')
bird_x = 50
bird_y = 300
bird_y_change = 0

def display_bird(x,y):
    screen.blit(BIRD_IMAGE, (x, y))


# Obstacles
OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = r.randint(150, 450)
OBSTACLE_COLOR = (0, 255, 0)
OBSTACLE_X_CHANGE = -.3
obstacle_x = 500

def display_obstacle(height):
    pg.draw.rect(screen, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
    bottom_obstacle_height = 635 - height - 150
    pg.draw.rect(screen, OBSTACLE_COLOR, (obstacle_x, 635, OBSTACLE_WIDTH, -bottom_obstacle_height))

running = True
while running:

    screen.fill(BLACK)
    # Display the Background Image
    screen.blit(BG_IMAGE, (0,0))


    for event in pg.event.get():
        # Quit the game
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                bird_y_change = -1

        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                bird_y_change = .4
    bird_y += bird_y_change

    if bird_y <= 0:
        bird_y = 0
    if bird_y >= 571:
        bird_y = 571

    obstacle_x += OBSTACLE_X_CHANGE
    if obstacle_x <= -10:
        obstacle_x = 500
        OBSTACLE_HEIGHT = r.randint(200, 400)
    display_obstacle(OBSTACLE_HEIGHT)


    display_bird(bird_x, bird_y)


    pg.display.update()

pg.quit()
