# Brady Nokes
# 1/26

from tkinter import *



def main():
    root = Tk()
    root.title("Passwords GUI")
    root.geometry("664x260")
    #root.resizable(0,0)
    root.attributes("-fullscreen" , False)
    app = App(root)
    frame = Frame(root)
    frame.grid()
    root.mainloop()


class App(Frame):
    usernames = ["brady", "warmachine68", "thelegend27"]
    passwords = ["password", "WARMACHINEROX", "bestplayer"]
    def __init__(self,master):
        super(App,self).__init__(master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):


        self.lbl = Label(self,text="Welcome to the password gui")


        self.lblUser = Label(self,text="USERNAME:")


        self.lblPass = Label(self,text="PASSWORD:")


        self.btn = Button(self,text="SUBMIT")


        self.entUser = Entry(self, width = 40)


        self.entPass = Entry(self, width = 40, show = "*")

        self.output = Text(self)

        self.unmaskBtn = Button(self, text = "SHOW PASS")

        self.maskBtn = Button(self, text="HIDE PASS")

        #MAKE NEW USER

        self.lblUser2 = Label(self, text="USERNAME:", state = "disabled")

        self.lblPass2 = Label(self, text="PASSWORD:", state = "disabled")

        self.btn2 = Button(self, text="SUBMIT", state = "disabled")

        self.entUser2 = Entry(self, width=40, state = "disabled")

        self.entPass2 = Entry(self, width=40, show="*", state = "disabled")

        self.unmaskBtn2 = Button(self, text="SHOW PASS", state = "disabled")

        self.maskBtn2 = Button(self, text="HIDE PASS", state = "disabled")

        self.newBtn = Button(self, text = "NEW USER", state = "disabled")


        # put on grid


        self.lbl.grid(row = 0, column = 0, columnspan = 3)
        self.lblUser.grid(row = 1, column = 0, sticky = NW)
        self.lblPass.grid(row = 2, column = 0, sticky = SW)
        self.btn.grid(row = 3, column = 0, sticky = W)
        self.entUser.grid(row = 1, column = 1, columnspan = 2, sticky = W)
        self.entPass.grid(row = 2, column = 1, columnspan = 2, sticky = W)
        self.output.grid(columnspan = 4, row = 4, column = 0)
        self.unmaskBtn.grid(row = 3, column = 1, sticky = W)
        self.maskBtn.grid(row=3, column=2, sticky=W)



        self.btn["command"] = self.submit
        self.unmaskBtn["command"] = self.unmask
        self.maskBtn["command"] = self.mask

        # MAKE NEW USER IF THEY ARE LOGGED IN
        self.lblUser2.grid(row=1, column=3, sticky=NW)
        self.lblPass2.grid(row=2, column=3, sticky=SW)
        self.btn2.grid(row=3, column=3, sticky=W)
        self.entUser2.grid(row=1, column=4, columnspan=2, sticky=W)
        self.entPass2.grid(row=2, column=4, columnspan=2, sticky=W)
        self.newBtn.grid(row = 4, column = 5, sticky = NW)
        #self.unmaskBtn2.grid(row=3, column=4, sticky=W)
        #self.maskBtn2.grid(row=3, column=5, sticky=W)

        #self.btn2["command"] = self.
        #self.unmaskBtn2["command"] = self.
        #self.maskBtn2["command"] = self.
        self.newBtn["command"] = self.newUser






        self.output.config(width = 40, height = 10)
    def submit(self):
        self.verified = False
        username = self.entUser.get()
        password = self.entPass.get()
        if username in self.usernames:
            if password in self.passwords:
                if self.usernames.index(username) == self.passwords.index(password):
                    self.verified = True
                    message = "You got in!"
                    self.tries = 0
                    self.newBtn.config(state = "normal")
                else:
                    message = "Those dont match"
                    self.tries += 1
                    self.entPass.delete(0, END)

            else:
                message = "Wrong Password Bro"
                self.tries += 1
                self.entPass.delete(0, END)
        else:
            message = "Wrong Username Bro"
        if self.tries > 3:
            message = "Oh no, you're in trouble"
            self.entPass.config(state = "disabled")
            self.entUser.config(state="disabled")
            self.btn.config(state="disabled")
        self.output.delete(0.0, END)
        self.output.insert(0.0, message)
        print(self.tries)

    def mask(self):
        self.entPass.config(show = "*")
    def unmask(self):
        self.entPass.config(show = "")

    def newUser(self):
        if self.verified == True:
            # OPEN UB BOXES

            self.lblUser2.config(state = "normal")
            self.lblPass2.config(state = "normal")
            self.btn2.config(state = "normal")
            self.entUser2.config(state = "normal")
            self.entPass2.config(state = "normal")
            self.unmaskBtn2.config(state = "normal")
            self.maskBtn2.config(state = "normal")




    def add_user(self):
        new_user = self.entUser2.get()
        new_pass = self.entPass2.get()
        self.usernames.append(new_user)
        self.passwords.append(new_pass)


main()