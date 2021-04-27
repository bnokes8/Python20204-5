# BRADY NOKES
# ADVANCED TEMPLATE
# 4/5/2021
# Art from Kenney.nl
# Happy Tune by http://opengameart.org/users/synocopika
# Yippee by https://opengameart.org/users/snabisch




# IMPORTS
import pygame as pg
import random as r
from settings import *
from sprites import *
from os import path
import io



class Game:

    def __init__(self):
        self.running = True
        # Initialize PyGame and Create Window
        pg.init()
        pg.mixer.init()  # For Sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()

    def load_data(self):
        # load spritesheet image
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, 'img')
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))
        # cloud images
        self.cloud_images = []
        for i in range(1, 4):
            self.cloud_images.append(pg.image.load(path.join(img_dir, 'cloud{}.png'.format(i))).convert())


         #HIGH SCORE FILES#
        # load high score

        with io.open(path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

        # Load sounds
        self.snd_dir = path.join(self.dir, 'snd')
        self.jump_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Jump33.wav'))
        self.boost_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Boost16.wav'))
        self.hurt_sound = pg.mixer.Sound(path.join(self.snd_dir, 'hurt.wav'))



    def new(self):
        # Create The Sprite Groups
        self.score = 0
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.player_group = pg.sprite.Group()
        self.platform_group = pg.sprite.Group()
        self.powerup_group = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.cloud_group = pg.sprite.Group()

        for plat in PLATFORM_LIST:
            Platform(self, *plat)

        self.enemy_timer = 0


        # Create Game Objects
        self.player = Player(self)

        # Add Game Objects to Groups


        pg.mixer.music.load(path.join(self.snd_dir, 'Happy Tune.ogg'))
        for i in range(10):
            c = Cloud(self)
            c.rect.y += 500
        # Start Running Game Loop
        self.run()


    def run(self):
        #Game Loop
        pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pg.mixer.music.fadeout(600)



    def events(self):
        for event in pg.event.get():
            # Check For Closing Window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()


    def update(self):
        self.all_sprites.update()

        # Spawn a mob?
        now = pg.time.get_ticks()
        if now - self.enemy_timer > 5000 + r.choice([-1000, -500,  0, 500, 1000]):
            self.enemy_timer = now
            Enemy(self)
        # Check if player hits platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platform_group, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.centery > lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.x < lowest.rect.right + 7 and self.player.pos.x > lowest.rect.left - 7:
                    if self.player.pos.y < lowest.rect.bottom:
                        self.player.pos.y = lowest.rect.top
                        self.player.vel.y = 0
                        self.player.jumping = False


        # if player reaches top 1/4 of screen
        if self.player.rect.top <= HEIGHT / 4:
            if r.randrange(100) < 10:
                Cloud(self)
            self.player.pos.y += max(abs(self.player.vel.y), 2)
            cloud_num = r.randrange(1,7)
            for cloud in self.cloud_group:
                cloud.rect.y += max(abs(self.player.vel.y / cloud_num), 2)
            for enemy in self.enemy_group:
                enemy.rect.y += max(abs(self.player.vel.y), 2)
                if enemy.rect.top > HEIGHT:
                    enemy.kill()
                    self.score += r.randrange(3, 25)
            for plat in self.platform_group:
                plat.rect.y += max(abs(self.player.vel.y), 2)
                if plat.rect.top > HEIGHT:
                    plat.kill()
                    self.score += 10

        # if player hits a power up
        pow_hits = pg.sprite.spritecollide(self.player, self.powerup_group, True)
        for pow in pow_hits:
            if pow.type == 'boost':
                self.boost_sound.play()
                self.player.vel.y = -BOOST_POWER
                self.player.jumping = False
        # If player DIES (to and enemy)
        hits = pg.sprite.spritecollide(self.player, self.enemy_group, False, pg.sprite.collide_mask)
        if hits:
            self.hurt_sound.play()
            self.playing = False

        # DIE!
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()

        if len(self.platform_group) == 0:
            self.playing = False

        # spawn new platforms to keep same avg num of plats
        while len(self.platform_group) < 5:
            height = r.randrange(15,35)
            width = r.randrange(50,125)
            Platform(self, r.randrange(0, WIDTH-width),
                    r.randrange(-75,-30))


    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)

        self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 15)



        # After Drawing EVERYTHING
        pg.display.flip()

    def show_start_screen(self):
        pg.mixer.music.load(path.join(self.snd_dir, 'Yippee.ogg'))
        pg.mixer.music.play(loops=-1)
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Arrows to move, Space to jump!", 30, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press Any Key to Play!", 30, WHITE, WIDTH / 2, HEIGHT * 3/4)
        self.draw_text("The High Score is: " + str(self.highscore), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def show_GO_screen(self):
        if not self.running:
            return
        pg.mixer.music.load(path.join(self.snd_dir, 'Yippee.ogg'))
        pg.mixer.music.play(loops=-1)
        self.screen.fill(BGCOLOR)
        self.draw_text("GAME OVER!", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 30, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press Any Key to Play Again!", 30, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("You Got a New High Score!", 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
            with io.open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text("High Score: " + str(self.highscore), 30, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_GO_screen()


pg.quit()




