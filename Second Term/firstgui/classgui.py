# Brady Nokes
# GUIS 1/21

# imports
from tkinter import *
from tkinter import font as font
import time

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.grid()
        self.clicks = 0
        self.colors = ["white","red","blue","yellow","#189159"]
        self.color_index = 0
        self.create_widgets()
    def create_widgets(self):
        self.lbltotal = Label(self, text = "Total Clicks: ")
        self.lblnumclicks = Label(self, text = str(self.clicks))
        self.addbtn = Button(self, text = "+ to count")
        self.minbtn = Button(self, text = "- from count")
        self.colorbtn = Button(self, text ="Change Color")


        self.colorbtn.config(width = 28, height = 3)
        
        self.addbtn.config(width = 28, height = 3)
        self.addbtn["command"] = self.add_to_count
        self.minbtn.config(width = 28, height = 3)
        self.minbtn["command"] = self.take_from_count
        self.colorbtn["command"] = self.change_bg


        self.colorbtn.grid()
        self.lbltotal.grid()
        self.lblnumclicks.grid()
        self.addbtn.grid()
        self.minbtn.grid()
    def add_to_count(self):
        self.clicks += 1
        print(self.clicks)
        self.lblnumclicks.config(text=str(self.clicks))
    def take_from_count(self):
        self.clicks -= 1
        print(self.clicks)
        self.lblnumclicks.config(text=str(self.clicks))
        if self.clicks < 0:
            self.clicks = 0
    def change_bg(self):
        self.color_index += 1
        if self.color_index > len(self.colors[self.color_index]):
            self.colors = 0








root = Tk()
root.title("First GUI")
root.geometry("200x400")

root.attributes("-fullscreen", False)
app = App(root)







root.mainloop()