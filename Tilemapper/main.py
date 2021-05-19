# BRADY NOKES
# ADVANCED TEMPLATE
# 4/5/2021

# IMPORTS
import pygame as pg
import random as r
from os import *
from settings import *
from sprites import *
import io


class Game(object):

    def __init__(self):
        self.running = True
        # Initialize PyGame and Create Window
        pg.init()
        pg.mixer.init() # For Sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.game_folder = path.dirname(__file__)
        self.map_data = []
        self.load_data()


    def load_data(self):

        with io.open(path.join(self.game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)



    def new(self):
        # Create The Sprite Groups
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)


        # Create Game Objects


        # Add Game Objects to Groups


        # Start Running Game Loop
        self.run()


    def run(self):
        #Game Loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
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

    def draw_grid(self):
        for x in range(0, WIDTH, TILE_SIZE):
            pg.draw.line(self.screen, GREEN, (x, 0), (x, HEIGHT))
        for y in range(0, WIDTH, TILE_SIZE):
            pg.draw.line(self.screen, GREEN, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.draw_grid()
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




