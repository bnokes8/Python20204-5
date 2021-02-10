# Brady Nokes
# 1/28  Pizza Order Form

from tkinter import *



def main():
    root = Tk()
    root.title("Pizza Order Form")
    root.geometry("600x600")
    #root.resizable(0,0)
    root.attributes("-fullscreen" , False)
    app = App(root)
    frame = Frame(root)
    frame.grid()
    root.mainloop()


class App(Frame):
    def __init__(self,master):
        super(App,self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):


        #self.lbl = Label(self,text="Welcome to the password gui")

        self.lblUser = Label(self,text="NAME:")

        self.lblAdd = Label(self,text="ADDRESS: ")

        self.lblPhone = Label(self, text = "PHONE #: ")

        self.lblSize = Label(self, text="SIZE")

        # TEXT ENTRY BOXES

        self.entUser = Entry(self)

        self.entAdd = Entry(self)

        self.entPhone = Entry(self)

        # PICK SIZE
        self.size = StringVar()
        self.size.set(None)
        Radiobutton(self, variable=self.size, text="Small", value="small", command = self.test).grid(row=4, column=0, columnspan=2, sticky=W)

        Radiobutton(self, variable=self.size, text="Medium", value="medium", command=self.test).grid(row=4, column=3,columnspan=2, sticky=W)

        Radiobutton(self, variable=self.size, text="Large", value="large", command=self.test).grid(row=4, column=5, columnspan=2, sticky=W)
        self.size.set("large")
        self.lblCrust = Label(self, text="CRUST")
        #PICK CRUST
        self.crust = StringVar()
        self.crust.set(None)
        Radiobutton(self, variable=self.crust, text="Regular", value="regular", command=self.test).grid(row=6, column=0,
                                                                                                   columnspan=2,
                                                                                                   sticky=W)

        Radiobutton(self, variable=self.crust, text="Thin", value="thin", command=self.test).grid(row=6, column=3,
                                                                                                     columnspan=2,
                                                                                                     sticky=W)

        Radiobutton(self, variable=self.crust, text="New York", value="ny", command=self.test).grid(row=6, column=5,
                                                                                                   columnspan=2,
                                                                                                   sticky=W)

        Radiobutton(self, variable=self.crust, text="Stuffed", value="stuffed", command=self.test).grid(row=7, column=0,
                                                                                                        columnspan=2,
                                                                                                        sticky=W)

        Radiobutton(self, variable=self.crust, text="Deep Dish", value="deep", command=self.test).grid(row=7, column=3,
                                                                                                  columnspan=2,
                                                                                                  sticky=W)

        Radiobutton(self, variable=self.crust, text="None", value="none", command=self.test).grid(row=7, column=5,
                                                                                                    columnspan=2,
                                                                                                    sticky=W)
        self.crust.set("stuffed")

        def create_check_boxes(self, var, top, r, c):
            Checkbutton(self,
                        variable=var,
                        text=top,
                        ).grid(row=r, column=c, sticky=W)


        self.lblTop = Label(self, text="TOPPINGS")
        #TOPPINGS
        self.pep = BooleanVar()
        create_check_boxes(self, self.pep, "Pepperoni", 9, 0)

        self.cheese = BooleanVar()
        create_check_boxes(self, self.cheese, "Cheese", 9, 1)

        self.bacon = BooleanVar()
        create_check_boxes(self, self.bacon, "Bacon", 9, 2)

        self.ham = BooleanVar()
        create_check_boxes(self, self.ham, "Ham", 10, 0)

        self.sasg = BooleanVar()
        create_check_boxes(self, self.sasg, "Sausage", 10, 1)

        self.onion = BooleanVar()
        create_check_boxes(self, self.onion, "Onion", 10, 2)

        self.chick = BooleanVar()
        create_check_boxes(self, self.chick, "Chicken", 11, 0)

        self.mush = BooleanVar()
        create_check_boxes(self, self.mush, "Mushroom", 11, 1)

        self.olive = BooleanVar()
        create_check_boxes(self, self.olive, "Olive", 11, 2)

        self.pine = BooleanVar()
        create_check_boxes(self, self.pine, "Pineapple", 12, 0)

        self.brc = BooleanVar()
        create_check_boxes(self, self.brc, "Broccoli", 12, 1)

        self.jala = BooleanVar()
        create_check_boxes(self, self.jala, "Jalapeno", 12, 2)

        self.ranch = BooleanVar()
        create_check_boxes(self, self.ranch, "Ranch", 13, 0)

        self.shrimp = BooleanVar()
        create_check_boxes(self, self.shrimp, "Shrimp", 13, 1)

        self.tbacon = BooleanVar()
        create_check_boxes(self, self.tbacon, "Turkey Bacon", 13, 2)







        # ORDER BUTTON

        self.btn = Button(self, text="ORDER", command = self.test)

        # END TEXT BOX

        self.output = Text(self)





        # put on grid


        #self.lbl.grid(row = 0, column = 0, columnspan = 3)
        self.lblUser.grid(row=0, column=0, columnspan=2, sticky=W)
        self.lblAdd.grid(row=1, column=0, columnspan=2, sticky=W)
        self.lblPhone.grid(row=2, column=0, columnspan=2, sticky=W)
        self.entUser.grid(row=0, column=3, columnspan=4, sticky=W)
        self.entAdd.grid(row=1, column=3, columnspan=4, sticky=W)
        self.entPhone.grid(row=2, column=3, columnspan=4, sticky=W)
        self.lblSize.grid(row=3, column=0, columnspan=2, sticky=W)
        self.lblCrust.grid(row=5, column=0, columnspan=2, sticky=W)
        self.lblTop.grid(row=8, column=0, columnspan=2, sticky=W)
        self.btn.grid(sticky=W)
        self.output.grid(columnspan=6, sticky=W)

        # CONIFG TEST

        self.output.config(width = 50)

    def test(self):
        order_size = self.size.get()
        order_crust = self.crust.get()
        toppings = []
        if self.pep.get():
            toppings.append("Pepperoni")
        if self.cheese.get():
            toppings.append("Cheese")
        if self.bacon.get():
            toppings.append("Bacon")
        if self.ham.get():
            toppings.append("Ham")
        if self.sasg.get():
            toppings.append("Sausage")
        if self.onion.get():
            toppings.append("Onion")
        if self.chick.get():
            toppings.append("Chicken")
        if self.mush.get():
            toppings.append("Mushroom")
        if self.olive.get():
            toppings.append("Olive")
        if self.pine.get():
            toppings.append("Pineapple")
        if self.brc.get():
            toppings.append("Broccoli")
        if self.jala.get():
            toppings.append("Jalapeno")
        if self.ranch.get():
            toppings.append("Ranch")
        if self.shrimp.get():
            toppings.append("Shrimp")
        if self.tbacon.get():
            toppings.append("Turkey Bacon")

        x = ""
        for i in range(len(toppings)):
            x += ", " + toppings[i]
        order = order_size + ", " + order_crust +x
        self.output.delete(0.0,END)
        self.output.insert(0.0,order)





main()