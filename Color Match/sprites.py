# IMPORTS
import pygame as pg
import random as r
from os import *
from settings import *


vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50,50))
        self.image.fill(YELLOW)
        # self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(40, HEIGHT - 100)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)



    def update (self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # Apply Friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # Equation of Motion
        self.vel += self.acc
        if abs(self.vel.x) < .5:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc

    def jump(self):
        # jump only if standing on platform
        self.rect.x += 3
        #hits = pg.sprite.spritecollide(self, self.game.platform_group, False)
        self.rect.x -= 3
        # if hits and not self.jumping:
        #     self.game.jump_sound.play()
        #     self.jumping = True
        #     self.vel.y = -PLAYER_JUMP