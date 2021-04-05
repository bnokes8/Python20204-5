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
        self.platform_group = pg.sprite.Group()

        p1 = Platform(0,HEIGHT - 40, WIDTH, 40)
        self.all_sprites.add(p1)
        self.platform_group.add(p1)

        p2 = Platform(WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20)
        self.all_sprites.add(p2)
        self.platform_group.add(p2)

        # Create Game Objects
        self.player = Player()

        # Add Game Objects to Groups
        self.all_sprites.add(self.player)
        self.player_group.add(self.player)

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
        hits = pg.sprite.spritecollide(self.player, self.platform_group, False)
        if hits:
            self.player.pos.y = hits[0].rect.top
            self.player.vel.y = 0

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




