# Brady Nokes
# GUIS 1/21

# imports
from tkinter import *
from tkinter import font as font
root = Tk()
root.title("First GUI")
root.geometry("1200x800")
root.config(bg="red")
root.attributes("-fullscreen" , False)

frame = Frame(root)/
frame.grid()

lbl = Label(frame, text="This is the best looking label ever", font='helvetica 32 bold italic')
lbl.grid()
lbl.config(fg="#db37d3")
lbl.config(bg="yellow")
lbl.config(width = "32")

lbl2 = Label(frame, text ="This is the second best looking label ever.", font="helvetica 32 bold italic")
lbl2.grid()
lbl2.config(fg="blue")
lbl2.config(bg="violet")
lbl2.config(width = "32")

lbl3 = Label(frame, text="This is the third best looking label ever.", font = "helvetica 32 bold italic")
lbl3.grid()
lbl3.config(fg="orange")
lbl3.config(bg="lime")
lbl3.config(width = "32")

btn = Button(frame, text="This is a button", font = "helvetica")
btn.grid()
btn.config(bg="black")
btn.config(fg="red")

btn2 = Button(frame, text="This is a button", font = "helvetica")
btn2.grid()
btn2.config(bg="black")
btn2.config(fg="red")

btn3 = Button(frame, text="This is a button", font = "helvetica")
btn3.grid()
btn3.config(bg="black")
btn3.config(fg="red")

btn4 = Button(frame)
btn4.grid()
btn4["text"] = "Dont click me"


keys = {"favcolor":"Red", "food":"pizza"}

favlbl = Label(frame, text = keys["favcolor"])
favlbl.grid()

for i in range(10):
    bttn = Button(frame, text="This is a button"+str(i+1), font="helvetica")
    bttn.grid()


root.mainloop()