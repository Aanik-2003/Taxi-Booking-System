import sqlite3
import tkinter as tk
from tkinter import ttk
from admin_dashboard import AdminDashboard
from custom_msg import CustomMessageBox
from registration_form import RegistrationForm
from driver_dashboard import DriverDashboard


class LoginForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # SQLite database connection
        self.connection = sqlite3.connect("C:\\Users\\user\\PycharmProjects\\taxi_booking\\prc1")
        self.cursor = self.connection.cursor()

        # Check if the theme exists before trying to set it
        theme_name = 'azure-light'
        if theme_name not in self.tk.call('ttk::themes'):
            self.tk.call('source', "C:\\Users\\user\\PycharmProjects\\taxi_booking\\Azure\\azure.tcl")
            self.tk.call('set_theme', theme_name)

        self.geometry("600x440""+900+310")
        self.title("Login")
        self.configure(bg="gray10")
        self.resizable(False, False)

        self.frame = ttk.Frame(self, width=320, height=360, style="TFrame")  # Add the 'style' attribute
        self.frame.place(x=130, y=30)

        # Create a style to set the background color
        self.style = ttk.Style(self)
        self.style.configure("TFrame", background="gray13")

        self.l2 = tk.Label(self.frame, text="Log into your Account", font=('Century Gothic', 20, "underline"), bg="#212121", fg="gray")
        self.l2.place(x=12, y=10)

        self.customer_types = ["Driver", "Customer", "Admin"]
        self.ct_combobox = ttk.Combobox(self.frame, width=20, values=self.customer_types, state="readonly")
        self.ct_combobox.set("User Type*")
        self.ct_combobox.place(x=80, y=60)

        self.email_lbl = tk.Label(self.frame, text="Email*", bg="#212121", fg="gray")
        self.email_lbl.place(x=80, y=100)
        self.email_entry = tk.Entry(self.frame, bg="#212121", fg="gray", width=20)
        self.email_entry.place(x=80, y=120)

        self.password_lbl = tk.Label(self.frame, text="Password*", bg="#212121", fg="gray")
        self.password_lbl.place(x=80, y=160)
        self.password_entry = tk.Entry(self.frame, bg="#212121", fg="gray", show='*', width=20)
        self.password_entry.place(x=80, y=180)

        self.show_password_var = tk.BooleanVar()
        self.show_password_box = tk.Checkbutton(self.frame, text="", bg="#212121", fg="black", command=self.toggle_password_visibility, variable=self.show_password_var)
        self.show_password_box.place(x=220, y=175)

        self.login_btn = tk.Button(self.frame, text="Login", bg="#212121", fg="green", width=10, command=self.login)
        self.login_btn.place(x=100, y=220)

        self.l3 = tk.Label(self.frame, text="Don't have an account!", font=('Century Gothic', 12, "underline"), bg="#212121", fg="gray")
        self.l3.place(x=50, y=250)

        self.sign_up_btn = tk.Button(self.frame, text="Sign Up", bg="#212121", fg="green", width=10, command=self.sign_up)
        self.sign_up_btn.place(x=100, y=285)

        self.custom_message_var = tk.StringVar()
        self.custom_message_label = tk.Label(self.frame, textvariable=self.custom_message_var, fg="red", bg="#212121")
        self.custom_message_label.place(x=80, y=250)

        # Initialize type_id
        self.type_id = None

    def toggle_password_visibility(self):
        show = self.show_password_var.get()
        if show:
            self.password_entry.configure(show='')
        else:
            self.password_entry.configure(show='*')

    def login(self):
        from cus_dashboard import CusDashboard, CustomFrame
        # Get user input
        user_type = self.ct_combobox.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        # if user select customer from combobox then it directly sets the user type id to 3 similarly
        # if user select manager from combobox then it directly sets the user type id to 1 and so on for driver.
        if user_type == "Customer":
            self.type_id = 3
            # Query to check login credentials
            query = "select cus_id,first_name,email,password,type_id from customer where type_id=? AND email=? AND password=?"
            self.cursor.execute(query, (self.type_id, email, password))
            result = self.cursor.fetchone()
            if result:

                CustomMessageBox.show_custom_dialog(self, "Login Successful!")
                self.close()
                # Assuming you have a 'first_name' attribute in your result
                cus_id = result[0]
                first_name = result[1]  # Replace with the actual attribute name
                print(cus_id)
                print(first_name)

                cd = CusDashboard(cus_id=cus_id, first_name=first_name)
                cd.start()
            else:
                CustomMessageBox.show_custom_dialog(self, "Login Failed. Please try again.")

        elif user_type == "Admin":
            self.type_id = 1
            # Query to check login credentials
            query = "select admin_id,first_name,email,password,type_id from admin where type_id=? AND email=? AND password=?"
            self.cursor.execute(query, (self.type_id, email, password))
            result = self.cursor.fetchone()
            if result:

                CustomMessageBox.show_custom_dialog(self, "Login Successful!")
                self.close()
                # Assuming you have a 'first_name' attribute in your result
                admin_id = result[0]
                first_name = result[1]  # Replace with the actual attribute name
                print(admin_id)
                print(first_name)

                t = AdminDashboard(admin_id=admin_id, first_name=first_name)
                t.start()
            else:
                CustomMessageBox.show_custom_dialog(self, "Login Failed. Please try again.")

        elif user_type == "Driver":
            self.type_id = 2
            # Query to check login credentials
            query = "select driver_id,first_name,email,password,type_id from driver where type_id=? AND email=? AND password=?"
            self.cursor.execute(query, (self.type_id, email, password))
            result = self.cursor.fetchone()
            if result:
                CustomMessageBox.show_custom_dialog(self, "Login Successful!")
                self.close()
                # Assuming you have a 'first_name' attribute in your result
                driver_id = result[0]
                first_name = result[1]  # Replace with the actual attribute name
                print(driver_id)
                print(first_name)

                dd = DriverDashboard(driver_id=driver_id, first_name=first_name)
                dd.start()
            else:
                CustomMessageBox.show_custom_dialog(self, "Login Failed. Please try again.")
            self.connection.close()
    def sign_up(self):
        self.close()
        self.register_form = RegistrationForm()  # accessing all the features of RegistrationForm class

    def close(self):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    lf = LoginForm()
    lf.start()
