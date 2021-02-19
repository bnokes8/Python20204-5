# Brady Nokes
# Snake Game
# imports
import random
import sys
from tkinter import *
from PIL import ImageTk, Image

class Cons():
    BOARD_WIDTH = 300
    BOARD_HEIGHT =  300
    DELAY = 100
    DOT_SIZE = 10
    MAX_RANDPOS = 27


class Board(Canvas):
    def __init__(self):
        super(Board, self).__init__(width=Cons.BOARD_WIDTH, height=Cons.BOARD_HEIGHT, background="black")

        self.initGame()
        self.pack()

    def initGame(self):
        '''initializes the game'''
        self.inGame = True
        self.dots = 3
        self.score = 0

        #variables used to move the snake object
        self.moveX = Cons.DOT_SIZE
        self.moveY = 0

        #starting apple cords
        self.appleX = 100
        self.appleY = 190

        # load images
        self.loadImages()
        # create game objects
        self.createObjects()
        # place apple on screen
        self.locateApple()
        self.bind_all("<Key>", self.onKeyPressed)
        self.after(Cons.DELAY,self.onTimer)

    def onTimer(self):
        '''creates a game cycle each timer event'''
        self.drawScore()
        self.checkCollision()
        if self.inGame:
            self.checkAppleCollision()
            self.moveSnake()
            self.after(Cons.DELAY, self.onTimer)
        else:
            self.gameOver()

    def gameOver(self):
        pass

    def moveSnake(self):
        pass

    def checkCollision(self):
        pass

    def checkAppleCollision(self):
        pass

    def drawScore(self):
        pass

    def onKeyPressed(self,e):
        '''controls direction variables with cursor keys'''
        key = e.keysym
        LEFT_CURSOR_KEY = "Left"
        if key == LEFT_CURSOR_KEY and self.moveX <= 0:
            self.moveX = -Cons.DOT_SIZE
            self.moveY = 0
        RIGHT_CURSOR_KEY = "Right"
        if key == RIGHT_CURSOR_KEY and self.moveX >= 0:
            self.moveX = Cons.DOT_SIZE
            self.moveY = 0
        UP_CURSOR_KEY = "Up"
        if key == UP_CURSOR_KEY and self.moveY <= 0:
            self.moveX = 0
            self.moveY = -Cons.DOT_SIZE
        DOWN_CURSOR_KEY = "Down"
        if key == DOWN_CURSOR_KEY and self.moveY >= 0:
            self.moveX = 0
            self.moveY = Cons.DOT_SIZE



    def locateApple(self):
        '''places the apple object on Canvs'''
        apple = self.find_withtag("apple")
        rx = random.randint(0,Cons.MAX_RANDPOS)
        ry = random.randint(0,Cons.MAX_RANDPOS)
        self.appleX = rx * Cons.DOT_SIZE
        self.appleY = ry * Cons.DOT_SIZE
        self.create_image(self.appleX, self.appleY, image=self.apple, anchor=NW, tag="apple")

    def createObjects(self):
        '''create objects on canvas'''
        self.create_text(30, 10, text = "Score: {0}".format(self.score),tag = "score", fill = "lime green")
        self.create_image(self.appleX, self.appleY, image = self.apple,anchor = NW, tag = "apple")
        self.create_image(50, 50, image=self.head, anchor=NW, tag="head")
        self.create_image(30, 50, image=self.body, anchor=NW, tag="body")
        self.create_image(40, 50, image=self.body, anchor=NW, tag="body")

    def loadImages(self):
        '''loads images from the disk'''
        try:
            self.ibody = Image.open("images/body.png")
            self.ihead = Image.open("images/head.png")
            self.iapple = Image.open("images/apple.png")
            self.body = ImageTk.PhotoImage(self.ibody)
            self.head = ImageTk.PhotoImage(self.ihead)
            self.apple = ImageTk.PhotoImage(self.iapple)
        except IOError as e:
            print(e)
            sys.exit(1)


class Snake(Frame):
    def __init__(self,master):
        super(Snake, self).__init__(master)
        self.master.title("Snake Clone")
        self.board = Board()
        self.pack()


def main():
    root = Tk()
    snake = Snake(root)
    root.mainloop()
main()