# Calculator Program
# By Abe and Brady


# IMPORTS
from tkinter import *
# Initializing the basic settings for GUI
HEIGHT = 361
WIDTH = 291
TITLE = "Calculator"
BACKGROUND = "darkgrey"
FONT = "Sans_Serif"


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.screen = "0"
        self.opperand1 = ""
        self.opperand2 = ""
        self.operator = ""
        self.create_widgets()

    #
    # making widgets
    def create_widgets(self):

        self.lbl = Label(self, bg="white", width=32, height=4, text="", font=9)
        self.lbl.grid(row=0, column=0, columnspan=4)

        self.one = Button(self, text="1", command=self.num1, width=9, height=4).grid(row=1, column=0)
        self.two = Button(self, text="2", command=self.num2, width=9, height=4).grid(row=1, column=1)
        self.three = Button(self, text="3", command=self.num3, width=9, height=4).grid(row=1, column=2)
        self.four = Button(self, text="4", command=self.num4, width=9, height=4).grid(row=2, column=0)
        self.five = Button(self, text="5", command=self.num5, width=9, height=4).grid(row=2, column=1)
        self.six = Button(self, text="6", command=self.num6, width=9, height=4).grid(row=2, column=2)
        self.seven = Button(self, text="7", command=self.num7, width=9, height=4).grid(row=3, column=0)
        self.eight = Button(self, text="8", command=self.num8, width=9, height=4).grid(row=3, column=1)
        self.nine = Button(self, text="9", command=self.num9, width=9, height=4).grid(row=3, column=2)
        self.clear = Button(self, text="C", command=self.delete, width=9, height=4).grid(row=4, column=0)
        self.zero = Button(self, text="0", command=self.num0, width=9, height=4).grid(row=4, column=1)
        self.enter = Button(self, text="=", command=self.equals, width=9, height=4).grid(row=4, column=2)
        self.plus = Button(self, text="+", command=self.add, width=9, height=4).grid(row=1, column=3)
        self.minus = Button(self, text="-", command=self.subtract, width=9, height=4).grid(row=2, column=3)
        self.multiply = Button(self, text="*", command=self.multiple, width=9, height=4).grid(row=3, column=3)
        self.divide = Button(self, text="/", command=self.div, width=9, height=4).grid(row=4, column=3)

    def num1(self):
        if self.screen == "0":
            self.screen = "1"
        else:
            self.screen += "1"
        self.lbl.config(text=self.screen)

    def num2(self):
        if self.screen == "0":
            self.screen = "2"
        else:
            self.screen += "2"
        self.lbl.config(text=self.screen)

    def num3(self):
        if self.screen == "0":
            self.screen = "3"
        else:
            self.screen += "3"
        self.lbl.config(text=self.screen)

    def num4(self):
        if self.screen == "0":
            self.screen = "4"
        else:
            self.screen += "4"
        self.lbl.config(text=self.screen)

    def num5(self):
        if self.screen == "0":
            self.screen = "5"
        else:
            self.screen += "5"
        self.lbl.config(text=self.screen)

    def num6(self):
        if self.screen == "0":
            self.screen = "6"
        else:
            self.screen += "6"
        self.lbl.config(text=self.screen)

    def num7(self):
        if self.screen == "0":
            self.screen = "7"
        else:
            self.screen += "7"
        self.lbl.config(text=self.screen)

    def num8(self):
        if self.screen == "0":
            self.screen = "8"
        else:
            self.screen += "8"
        self.lbl.config(text=self.screen)

    def num9(self):
        if self.screen == "0":
            self.screen = "9"
        else:
            self.screen += "9"
        self.lbl.config(text=self.screen)

    def num0(self):
        self.screen += "0"
        self.lbl.config(text=self.screen)

    def add(self):
        self.opperand1 = self.screen
        self.screen = "0"
        self.operator = "+"
        self.lbl.config(text=self.screen)


    def subtract(self):
        self.opperand1 = self.screen
        self.screen = "0"
        self.operator = "-"
        self.lbl.config(text=self.screen)


    def multiple(self):
        self.opperand1 = self.screen
        self.screen = "0"
        self.operator = "*"
        self.lbl.config(text=self.screen)


    def div(self):
        self.opperand1 = self.screen
        self.screen = "0"
        self.operator = "/"
        self.lbl.config(text=self.screen)


    def delete(self):
        self.opperand1 = ""
        self.operator = ""
        self.opperand2 = ""
        self.screen = "0"
        self.lbl.config(text=self.screen)

    def equals(self):
        self.opperand2 = self.screen
        if self.opperand2 == "0" and self.operator == "/":
            self.lbl.config(text="Error")
        else:
            if self.operator == "+":
                self.lbl.config(text=int(self.opperand1)+int(self.opperand2))
            elif self.operator == "-":
                self.lbl.config(text=int(self.opperand1)-int(self.opperand2))
            elif self.operator == "*":
                self.lbl.config(text=int(self.opperand1)*int(self.opperand2))
            elif self.operator == "/":
                self.lbl.config(text=int(self.opperand1)/int(self.opperand2))
# main loop


def main():
    root = Tk()
    root.geometry(str.format("{}x{}", WIDTH, HEIGHT))
    root.title(TITLE)
    root.config(bg=BACKGROUND)
    app = App(root)
    root.mainloop()



main()
