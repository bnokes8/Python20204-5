from tkinter import *
from PIL import Image,ImageTk


HEIGHT = 400
WIDTH = 400
TITLE = "new program"
BACKGROUND = "darkgray"
FONT = "San_Serif"



class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.pack(fill = BOTH,expand = 1)
        self.create_widgets()

    def create_widgets(self):
        self.canvas = Canvas(self)
        # self.canvas.create_line(20,20,100,200)
        # self.canvas.create_line(200,35,200,300,dash = (6,3))
        # self.canvas.create_line(50,50,70,50,50,70,70,50)

        # self.canvas.create_rectangle(30,10,120,80,fill="#546ead",outline="red",width=5)
        # self.canvas.create_oval(10,10,80,80, outline = "#f11",fill="#1f1",width=2)
        # self.canvas.create_oval(110,10,210,80,outline="#f11",fill="#1f1",width=2)
        # self.canvas.create_arc(30,200,90,100,start=0,extent=210,outline="#f11",fill="#1f1",width=2)



        self.img = Image.open("test.jpg")
        self.pic = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(10,10,anchor = NW,image=self.pic)

        self.canvas.pack(fill = BOTH, expand = 1)


def main():
    root = Tk()
    root.geometry(str.format("{}x{}",WIDTH,HEIGHT))
    root.title(TITLE)
    root.config(bg = BACKGROUND)
    app = App(root)
    root.mainloop()


main()