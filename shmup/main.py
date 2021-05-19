
##################### Attribution #######################
# tutorial found at kidscancode.org
# Code created by: Eric Broadbent
# Art Created by: www.kenney.nl

##################### end Attribution #######################


##################### imports ###########################
import pygame as pg
import random as r
import math as m
from os import *
import io
###################### imports ##########################



###################### Game object classes #########################
# player class
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.shield = 100
        self.fuel =100
        self.lives = 3
        self.difficulty = 1
        self.hidden = False
        self.hide_timer = pg.time.get_ticks()
        # self.image = pg.Surface((50, 40))
        # self.image.fill(GREEN)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(self.image, (75, 55))
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * .75 / 2
        if debug:
            pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = (HEIGHT - (HEIGHT*.05))
        self.speedx = 0
        self.shoot_delay = 250
        self.last_shot = pg.time.get_ticks()
        self.powerlevel = 1
        self.power_timer = pg.time.get_ticks()

    def shields_up(self,num):
        self.shield += num
        if self.shield >= 100:
            self.shield = 100

    def fuel_add(self,num):
        self.fuel += num
        if self.fuel >= 100:
            self.fuel = 100

    def gun_pow(self):
        self.powerlevel+=1
        self.power_timer = pg.time.get_ticks()
    def life_add(self):
        if self.lives >= 4:
            self.lives = 4
        else:
            self.lives += 1


    def shoot(self):
        now = pg.time.get_ticks()
        self.shoot_delay = 250
        if difficulty == 1:
            self.shoot_delay = 250
        elif difficulty == 2:
            self.shoot_delay = 325
        elif difficulty == 3:
            self.shoot_delay = 400
        if (now-self.last_shot) > self.shoot_delay:
            self.last_shot = now
            if self.powerlevel == 1:
                b = Bullet(self.rect.centerx,self.rect.top-1)
                all_sprites.add(b)
                bullet_group.add(b)
                shoot_sound.play()
            if self.powerlevel == 2:
                b = Bullet(self.rect.left, self.rect.centery)
                all_sprites.add(b)
                bullet_group.add(b)
                b = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(b)
                bullet_group.add(b)
                shoot_sound.play()
            if self.powerlevel == 3:
                b = Bullet(self.rect.centerx, self.rect.top - 1)
                all_sprites.add(b)
                bullet_group.add(b)
                b = Bullet(self.rect.left, self.rect.centery)
                all_sprites.add(b)
                bullet_group.add(b)
                b = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(b)
                bullet_group.add(b)
                shoot_sound.play()
            if self.powerlevel >= 4:
                b = Bullet(self.rect.centerx, self.rect.top - 1)
                b.spread = 2
                all_sprites.add(b)
                bullet_group.add(b)
                b = Bullet(self.rect.centerx, self.rect.top - 1)
                all_sprites.add(b)
                bullet_group.add(b)
                b = Bullet(self.rect.centerx, self.rect.top - 1)
                b.spread = -2
                all_sprites.add(b)
                bullet_group.add(b)
                b = Bullet(self.rect.left, self.rect.centery)
                b.spread = -3
                all_sprites.add(b)
                bullet_group.add(b)
                b = Bullet(self.rect.right, self.rect.centery)
                b.spread = 3
                all_sprites.add(b)
                bullet_group.add(b)
                shoot_sound.play()

    def get_hit(self,radius):
        self.shield -= radius * 2

    def hide(self):
        # hide the player temporarily
        self.hidden = True
        self.lives -=1
        self.hide_timer = pg.time.get_ticks()
        self.rect.center = (WIDTH/2, HEIGHT + 500)

    def update(self):
        # timeout for powerups
        if self.powerlevel >=2 and pg.time.get_ticks() - self.power_timer > POWERUP_TIME:
            self.powerlevel -= 1
            self.power_timer = pg.time.get_ticks()
        # unhide if hidden
        if self.hidden and pg.time.get_ticks() - self.hide_timer > 3000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = (HEIGHT - (HEIGHT * .05))
            self.shield = 100


        # basic movement side to side
        if keyboard:
            self.speedx = 0

            keystate = pg.key.get_pressed()
            if (keystate[pg.K_LEFT] or keystate[pg.K_a]) and self.fuel>0:
                self.speedx = -5
                self.fuel-=.5
            if ( keystate[pg.K_RIGHT] or keystate[pg.K_d]) and self.fuel>0:
                self.speedx = 5
                self.fuel -= .5
            if keystate[pg.K_SPACE] and  not self.hidden:
                self.shoot()
        if mouse:
            mousestate = pg.mouse.get_pressed(3)
            if mousestate[0]:
                self.shoot()
            mouse_pos = pg.mouse.get_pos()
            self.rect.centerx = mouse_pos[0]
            self.fuel -= .5

        # binding ship to screen
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH

        self.rect.x += self.speedx

# Player projectile
class Bullet(pg.sprite.Sprite):
    def __init__(self,x,y):
        super(Bullet, self).__init__()
        # self.image = pg.Surface((5, 10))
        # self.image.fill(BLUE)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.image=pg.transform.scale(self.image,(15,25))
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * .75 / 2
        if debug:
            pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10
        self.spread = 0

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.spread
        # kill bullet when rect.bottom <= 0
        if self.rect.bottom < 0:
            self.kill()


# background objects
class Star(pg.sprite.Sprite):
    def __init__(self):
        super(Star,self).__init__()
        self.size =r.randint(1,7)
        self.image = pg.Surface((self.size, self.size))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.x = r.randint(5,WIDTH-5)
        self.y = r.randint(-1000,HEIGHT)
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.speedy = 5

    def update(self):
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT:
            self.x = r.randint(5, WIDTH - 5)
            self.y = r.randint(-1000, 0)
            self.rect.center = (self.x,self.y)

#explostions class
class Explosion(pg.sprite.Sprite):

    def __init__(self, center, size):
        super(Explosion, self).__init__()
        self.size = size
        self.image = exp_anim[self.size][0]
        self.rect=self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame +=1
            if self.frame == len(exp_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = exp_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

# enemy class
class NPC(pg.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        # self.image = pg.Surface((25, 25))
        # self.image.fill(RED)
        self.image_orig = r.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        # self.image_orig = pg.transform.scale(self.image_orig,(75,75))
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = self.rect.width *.75 /2
        self.x = r.randint(0,WIDTH)
        self.rect.centerx = self.x
        self.rect.bottom = 0
        self.rx = r.randint(0,10)
        self.ry = r.randint(1, 10)
        self.speedx = self.rx
        self.speedy = self.ry
        self.rot = 0
        self.rot_speed = r.randint(-8,8)
        self.last_update = pg.time.get_ticks()

    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 20:
            self.last_update = now
            #rotate sprite
            self.rot = (self.rot + self.rot_speed)%360
            new_image = pg.transform.rotate(self.image_orig,self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center


    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.top >= HEIGHT+20 or self.rect.left >= WIDTH+10 or self.rect.right <= -10:
            self.rx = r.randint(-5,5)
            self.ry = r.randint(1,10)
            self.speedx = self.rx
            self.speedy = self.ry
            newposx = r.randint(15,WIDTH-15)
            newposy = r.randint(10,25)*-1
            self.rect.center = (newposx,newposy)

class Collectables(pg.sprite.Sprite):
    def __init__(self, center):
        super(Collectables, self).__init__()
        self.type = r.choice(powchance)
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the bottom of the screen
        if self.rect.top > HEIGHT:
            self.kill()



######################## Game object classes ########################



######################## game Constants ########################
title = "Shmup"
WIDTH = 600
HEIGHT = 900
FPS = 60
difficulty = 1

# Colors (R,G,B)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

font_name = pg.font.match_font('arial')

debug = False
mouse = False
keyboard = True

powchance =["shield","gun","fuel","shield","shield","shield","fuel","fuel","fuel","fuel","life","life","life","life","life","life"]
powTypes = ["gun","shield","fuel", "life"]

POWERUP_TIME = 6000

creator = "Brady Nokes"

###################### game Constants ##########################

# folder variables
####################################################################
game_folder = path.dirname(__file__)
imgs_folder = path.join(game_folder,"imgs")
snds_folder = path.join(game_folder,"snds")
scores_folder = path.join(game_folder,"scores")
background_folder = path.join(imgs_folder,"backgrounds")
enemy_imgs_folder = path.join(imgs_folder,"enemy_imgs")
player_imgs_folder = path.join(imgs_folder,"player_imgs")
animation_folder = path.join(imgs_folder,"animations")
pows_folder = path.join(imgs_folder,"pows")



####################################################################

###################### game functions ##########################
def spawn_npc():
    for i in range(1):
        npc = NPC()
        npc_group.add(npc)
        all_sprites.add(npc)

def draw_text(surf,text,size,x,y,color):
    font = pg.font.Font(font_name, size)
    text_surf = font.render(text,True,color)
    text_rect = text_surf.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surf,text_rect)

def draw_bar(surf,x,y,pct,color):
    if pct < 0:
        pct = 0
    bar_len = 180
    bar_height = 40
    fill = (pct/100)*bar_len
    outline = pg.Rect(x,y,bar_len,bar_height)
    fillrect =pg.Rect(x,y,fill,bar_height)
    pg.draw.rect(surf,color,fillrect)
    pg.draw.rect(surf,WHITE,outline,3)

def draw_lives(surf,x,y,lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x+30 * i
        img_rect.y = y
        surf.blit(img,img_rect)

def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, title, 64, WIDTH/2, HEIGHT/4, WHITE)
    draw_text(screen, "Created by "+creator, 22, WIDTH/2, HEIGHT/2, WHITE)
    draw_text(screen, "You use the space bar to fire, and the arrow keys to shoot.", 18, WIDTH/2, HEIGHT*3/4, WHITE)
    draw_text(screen, "Press any key to begin", 18, WIDTH/2, HEIGHT*7/8, WHITE)
    pg.display.flip()
    waiting = True
    while waiting:
        keystate = pg.key.get_pressed()
        difficulty = 1
        clock.tick()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYUP:
                if keystate[pg.K_KP1]:
                    Player.difficulty = 1
                    waiting = False
                if keystate[pg.K_KP2]:
                    Player.difficulty = 2
                    waiting = False
                if keystate[pg.K_KP1]:
                    Player.difficulty = 3
                    waiting = False
                else:
                    Player.difficulty = 2
                    waiting = False




###################### end game functions ##########################


################ initialize pygame and create window ###############
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()
################# end initialize pygame and create window ##############



############### load imgs ################
background = pg.image.load(path.join(background_folder,"bg1.png")).convert()
background = pg.transform.scale(background, (WIDTH,HEIGHT))
background_rect = background.get_rect()
npc_img = pg.image.load(path.join(enemy_imgs_folder,"img_3.png")).convert()
player_img = pg.image.load(path.join(player_imgs_folder,"player1ship.png")).convert()
player_mini_img = pg.transform.scale(player_img,(25,19))
player_mini_img.set_colorkey(BLACK)


bullet_img = pg.image.load(path.join(player_imgs_folder,"bulletred.png")).convert()
meteor_images = []
meteor_list =['meteorBrown_big1.png','meteorBrown_big3.png','meteorBrown_big2.png','meteorBrown_big4.png',
              'meteorBrown_med1.png','meteorBrown_med3.png',
              'meteorBrown_small1.png','meteorBrown_small2.png',
              'meteorBrown_tiny1.png','meteorBrown_tiny2.png',
              'meteorGrey_big1.png','meteorGrey_big2.png','meteorGrey_big3.png','meteorGrey_big4.png',
              'meteorGrey_med1.png','meteorGrey_med2.png',
              'meteorGrey_small1.png','meteorGrey_small2.png',
              'meteorGrey_tiny1.png','meteorGrey_tiny2.png']
for img in meteor_list:
    meteor_images.append(pg.image.load(path.join(enemy_imgs_folder,img)).convert())

exp_anim = {}
exp_anim["lg"] = []
exp_anim["sm"] = []
for i in range(9):
    filename = "regularExplosion0{}.png".format(i)
    img = pg.image.load(path.join(animation_folder,filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pg.transform.scale(img,(200,200))
    exp_anim["lg"].append(img_lg)
    img_sm = pg.transform.scale(img, (75, 75))
    exp_anim["sm"].append(img_sm)

powerup_images = {}
for i in range(len(powTypes)):
    fn = "img_{}.png".format(i)
    powerup_images[powTypes[i]] = pg.image.load(path.join(pows_folder,fn)).convert()



############### end load imgs ################

# load sounds
############################################
shoot_sound = pg.mixer.Sound(path.join(snds_folder,"pew.wav"))
expl_snds = []
for snd in ["expl3.wav","expl6.wav"]:
    expl_snds.append(pg.mixer.Sound(path.join(snds_folder, snd)))

shield_snd = pg.mixer.Sound(path.join(snds_folder,"Cancel - 1.wav"))
gun_snd = pg.mixer.Sound(path.join(snds_folder,"Cancel - 2.wav"))
fuel_snd = pg.mixer.Sound(path.join(snds_folder,"Cancel - 4.wav"))
life_snd = pg.mixer.Sound(path.join(snds_folder,"life.wav"))

pg.mixer.music.load(path.join(snds_folder,'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pg.mixer.music.set_volume(0.2)

############################################

#################### Game Loop ############################

############### game update Variables ################
playing = True
game_over = True
score = 0
level = 1
diff = 0
pg.mixer.music.play(loops=-1)

############## end game update Variables #################

############### Play loop ################
while playing:
    if game_over:
        show_go_screen()
        game_over = False
        ################ create Sprite groups ###############
        all_sprites = pg.sprite.Group()
        players_group = pg.sprite.Group()
        npc_group = pg.sprite.Group()
        bullet_group = pg.sprite.Group()
        star_group = pg.sprite.Group()
        collectable_group = pg.sprite.Group()
        ################ end create Sprite groups ##############
        ################# create Game Objects ##############
        player = Player()
        for i in range(20):
            npc = NPC()
            npc_group.add(npc)
        for i in range(25):
            star = Star()
            star_group.add(star)
        ############### end create Game Objects ################
        ################ add objects to sprite groups ###############
        players_group.add(player)
        for i in star_group:
            all_sprites.add(i)
        for i in players_group:
            all_sprites.add(i)
        for i in npc_group:
            all_sprites.add(i)
        ############### end add objects to sprite groups ################

    ############### #timing #################
    clock.tick(FPS)
    ################ end timing #################


    ############### # Collect Input #################

    # Quiting the game when we hit the x or hits escape
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing=False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                playing = False
            # # player shooting
            # if event.key == pg.K_SPACE:
            #     player.shoot()
            if event.key == pg.K_F12:
                debug = not debug

    ################# end Collect Input ################


    ################# Update ################
    #checking for hit between player and npc
    hits = pg.sprite.spritecollide(player,npc_group,True,pg.sprite.collide_circle)
    if hits:
        exp = Explosion(hits[0].rect.center,"sm")
        all_sprites.add(exp)
        r.choice(expl_snds).play()
        spawn_npc()
        player.get_hit(hits[0].radius)
        if player.shield <= 0:
            finalexp = Explosion(player.rect.center,"lg")
            all_sprites.add(exp)
            player.hide()

            if player.lives <= 0 and not finalexp.alive():
                player.kill()
                game_over = True

    hits =  pg.sprite.spritecollide(player,collectable_group,True)
    for hit in hits:
        if hit.type == "shield":
            num = r.randint(15,35)
            player.shields_up(num)
            shield_snd.play()

        if hit.type == "gun":
            player.gun_pow()
            gun_snd.play()

        if hit.type == "fuel":
            player.fuel_add(50)
            fuel_snd.play()
        if hit.type == "life":
            player.life_add()
            life_snd.play()

    # bullet hits NPC
    hits = pg.sprite.groupcollide(npc_group,bullet_group,True,True, pg.sprite.collide_circle)
    for hit in hits:
        if hit.radius < 30:
            size = "sm"
        else:
            size = "lg"
        exp = Explosion(hit.rect.center,size)
        all_sprites.add(exp)
        r.choice(expl_snds).play()
        score += 50 - int(hit.radius)
        if r.random() > 0.85:
            pow = Collectables(hit.rect.center)
            all_sprites.add(pow)
            collectable_group.add(pow)
        spawn_npc()


    all_sprites.update()
    ################ end Update #################


    ############## # Render ##################
    screen.fill(BLACK)
    screen.blit(background,background_rect)

    all_sprites.draw(screen)

    # draw HUD
    draw_text(screen,"Score: "+str(score),40, WIDTH/2,15,WHITE)
    draw_bar(screen, 5, 15, player.shield, GREEN)
    draw_bar(screen, 5, 55, player.fuel, BLUE)
    draw_lives(screen,WIDTH-150,15,player.lives,player_mini_img)

    pg.display.flip()
    ############### end Render ##################

############# end Play loop #################
pg.quit()

################ end Game Loop ###############################