import tkinter as tk
from tkinter import Menu, Label
from PIL import Image, ImageTk
from login_form import LoginForm
from registration_form import RegistrationForm


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Creating and using external theme
        self.tk.call('source', "C:\\Users\\user\\PycharmProjects\\taxi_booking\\Azure\\azure.tcl")
        self.tk.call('set_theme', 'dark')

        self.geometry(f"{screen_width}x{screen_height}")
        self.geometry("+0+0")
        self.title("Aanik's Cab")
        self.resizable(False, False)

        self.menubar = Menu(self, background="black")
        self.config(menu=self.menubar)

        self.admin_menu = Menu(self.menubar, tearoff=0, bg="black", fg="white", activebackground="darkred")
        self.menubar.add_cascade(label="Admin", menu=self.admin_menu)
        self.admin_menu.add_command(label="Login", command=self.login_btn)

        self.driver_menu = Menu(self.menubar, tearoff=0, bg="black", fg="white", activebackground="darkred")
        self.menubar.add_cascade(label="Driver", menu=self.driver_menu)
        self.driver_menu.add_command(label="Login", command=self.login_btn)

        self.customer_menu = Menu(self.menubar, tearoff=0, bg="black", fg="white", activebackground="darkred")
        self.menubar.add_cascade(label="Customer", menu=self.customer_menu)
        self.customer_menu.add_command(label="Login", command=self.login_btn)
        self.customer_menu.add_command(label="SignUp", command=self.signUp_btn)

        self.img = Image.open("C:\\Users\\user\\PycharmProjects\\taxi_booking\\newBg5.jpg")
        self.photo = ImageTk.PhotoImage(self.img)

        self.frame = tk.Frame(master=self, width=screen_width, height=screen_height)
        self.frame.pack()

        self.img_lbl = Label(self.frame, image=self.photo)
        self.img_lbl.image = self.photo  # To prevent image from being garbage collected
        self.img_lbl.place(x=0, y=0)

        self.header_lbl = Label(master=self.frame, height=2, width=28, text="Welcome To Aanik's Tour and Travels",
                                font=('Times New Roman', 40, 'bold', 'underline'), bg="#383838", fg="gray")
        self.header_lbl.place(x=350, y=80)

        self.slogan_lbl = Label(master=self.frame, height=3, width=56,
                                text="Ride with Ease, Arrive with Style – Your Journey, Your Way!",
                                font=('Times New Roman', 20, 'bold'), bg="#383838", fg="gray")
        self.slogan_lbl.place(x=350, y=170)

        self.text_lbl = Label(
            master=self.frame, width=35,
            text=(
                "Picture this simple bookings, services \ntailored just for you,"
                "and a touch of \nluxury to sweeten "
                "the deal. "
                "Jump in \nwith our crew of smart travelers who \nlove that comfy, trusty vibe and a dash \nof extra style. "
                "Your journey, your way – \nbecause why settle for less? Intrigued \nto turn every ride into an adventure? \n"
                "Just hit that sign-up button and \nlet's kick off your travel story!"
            ),
            font=('Times New Roman', 18),
            bg="#383838", fg="gray"
        )

        self.text_lbl.place(x=1050, y=310)

        self.login_btn = tk.Button(master=self.frame, width=10, text="Login", bg="#383838", fg="green", command=self.login_btn)
        self.login_btn.place(x=1200, y=600)

        self.signUp_btn = tk.Button(master=self.frame, width=10, text="SignUp", bg="#383838", fg="green", command=self.signUp_btn)
        self.signUp_btn.place(x=1300, y=600)

    def start(self):
        self.mainloop()

    def login_btn(self):
        self.login_form = LoginForm(self)  #accessing all the features of LoginForm class

    def signUp_btn(self):
        self.register_form = RegistrationForm()  #accessing all the features of RegistrationForm class


if __name__ == "__main__":
    mw = MainWindow()
    mw.start()
