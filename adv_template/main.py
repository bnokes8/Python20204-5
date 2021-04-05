# BRADY NOKES
# ADVANCED TEMPLATE
# 4/5/2021

# IMPORTS
import pygame as pg
import random as r
from os import *
from settings import *
from sprites import *

class Game(object):

    def __init__(self):
        self.running = True
        # Initialize PyGame and Create Window
        pg.init()
        pg.mixer.init() # For Sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()


    def new(self):
        # Create The Sprite Groups
        self.all_sprites = pg.sprite.Group()
        self.player_group = pg.sprite.Group()

        # Create Game Objects
        player = Player()

        # Add Game Objects to Groups
        self.all_sprites.add(player)
        self.player_group.add(player)

        # Start Running Game Loop
        self.run()


    def run(self):
        #Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def events(self):
        for event in pg.event.get():
            # Check For Closing Window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)


        # After Drawing EVERYTHING
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_GO_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_GO_screen()


pg.quit()




