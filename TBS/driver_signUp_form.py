import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

from custom_msg import CustomMessageBox


class DriverSignUp(tk.Toplevel):
    def __init__(self):
        super().__init__()


        # actual path to your SQLite database file
        db_path = "C:\\Users\\user\\PycharmProjects\\taxi_booking\\prc1"

        # Try to connect to the SQLite database
        try:
            self.connection = sqlite3.connect(db_path)
            self.cursor = self.connection.cursor()
            print("Database connected successfully!")

            # Create the registration table if not exists
            self.cursor.execute('''
                                       create table if not exists driver (
                                            driver_id integer primary key autoincrement,
                                            first_name char(25),
                                            last_name char(25),
                                            country char(25),
                                            city char(25),
                                            phone varchar(25),
                                            email varchar(25),
                                            password varchar(25),
                                            no_plate varchar(25),
                                            status char(15),
                                            type_id integer,
                                            foreign key(type_id) references user_type(type_id)
                                        );
                                   ''')
            self.connection.commit()

        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")


        # Check if the theme exists before trying to set it
        theme_name = 'azure-light'
        if theme_name not in self.tk.call('ttk::themes'):
            self.tk.call('source', "C:\\Users\\user\\PycharmProjects\\taxi_booking\\Azure\\azure.tcl")
            self.tk.call('set_theme', theme_name)

        self.geometry("600x440""+900+310")
        self.title("Driver Registration Form")
        self.configure(bg="gray10")

        self.frame = ttk.Frame(self, width=380, height=360, style="TFrame")  # Add the 'style' attribute
        self.frame.place(x=110, y=30)

        # Create a style to set the background color
        self.style = ttk.Style(self)
        self.style.configure("TFrame", background="gray13")

        self.l1 = tk.Label(self.frame, text="Registration Form", font=('Century Gothic', 20, "underline"), bg="#212121", fg="gray")
        self.l1.place(x=60, y=10)

        self.first_name_lbl = tk.Label(self.frame, text="First Name*", font=('Century Gothic', 10), bg="#212121", fg="gray")
        self.first_name_lbl.place(x=5, y=80)

        self.first_name_entry = tk.Entry(self.frame, width=15, bg="#212121", fg="gray")
        self.first_name_entry.place(x=85, y=80)

        self.last_name_lbl = tk.Label(self.frame, text="Last Name*", font=('Century Gothic', 10), bg="#212121", fg="gray")
        self.last_name_lbl.place(x=197, y=80)

        self.last_name_entry = tk.Entry(self.frame, width=15, bg="#212121", fg="gray")
        self.last_name_entry.place(x=280, y=80)

        self.country_lbl = tk.Label(self.frame, text="Country*", font=('Century Gothic', 10), bg="#212121", fg="gray")
        self.country_lbl.place(x=5, y=120)

        self.country_entry = tk.Entry(self.frame, width=15, bg="#212121", fg="gray")
        self.country_entry.place(x=85, y=120)

        self.city_lbl = tk.Label(self.frame, text="City/Town*", font=('Century Gothic', 10), bg="#212121", fg="gray")
        self.city_lbl.place(x=197, y=120)

        self.city_entry = tk.Entry(self.frame, width=15, bg="#212121", fg="gray")
        self.city_entry.place(x=280, y=120)

        self.phone_lbl = tk.Label(self.frame, text="Phone", font=("Century Gothic", 10), bg="#212121", fg="gray")
        self.phone_lbl.place(x=5, y=160)

        self.phone_entry = tk.Entry(self.frame, width=15, bg="#212121", fg="gray")
        self.phone_entry.place(x=85, y=160)

        self.email_lbl = tk.Label(self.frame, text="Email*", font=("Century Gothic", 10), bg="#212121", fg="gray")
        self.email_lbl.place(x=197, y=160)

        self.email_entry = tk.Entry(self.frame, width=15, bg="#212121", fg="gray")
        self.email_entry.place(x=280, y=160)

        self.password_lbl = tk.Label(self.frame, text="Password*", font=("Century Gothic", 10), bg="#212121", fg="gray")
        self.password_lbl.place(x=5, y=200)

        self.password_entry = tk.Entry(self.frame, width=15, bg="#212121", fg="gray", show='*')
        self.password_entry.place(x=85, y=200)

        self.license_plate_lbl = tk.Label(self.frame, text="No. Plate*", font=("Century Gothic", 10), bg="#212121", fg="gray")
        self.license_plate_lbl.place(x=197, y=200)

        self.license_plate_entry = tk.Entry(self.frame, width=15, bg="#212121", fg="gray")
        self.license_plate_entry.place(x=280, y=200)

        self.confirm_pass_lbl = tk.Label(self.frame, text="Confirm Password*", font=("Century Gothic", 10), bg="#212121", fg="gray")
        self.confirm_pass_lbl.place(x=5, y=240)

        self.confirm_pass_entry = tk.Entry(self.frame, width=15, bg="#212121", fg="gray", show='*')
        self.confirm_pass_entry.place(x=140, y=240)

        self.show_password_var = tk.BooleanVar()
        self.show_password_box = tk.Checkbutton(self.frame, text="", bg="#212121", fg="black", command=self.toggle_password_visibility,
                                                variable=self.show_password_var)
        self.show_password_box.place(x=240, y=237)

        self.submit_btn = tk.Button(self.frame, text="Submit", bg="#212121", fg="green", command=self.submit_form)
        self.submit_btn.place(x=10, y=290)

        self.cancel_btn = tk.Button(self.frame, text="Cancel", bg="#212121", fg="red", command=self.close)
        self.cancel_btn.place(x=80, y=290)



    def toggle_password_visibility(self):
        show = self.show_password_var.get()
        if show:
            self.password_entry.configure(show='')
            self.confirm_pass_entry.configure(show='')
        else:
            self.password_entry.configure(show='*')
            self.confirm_pass_entry.configure(show='*')

    def submit_form(self):
        # Extract data from the form
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        country = self.country_entry.get()
        city = self.city_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_pass = self.confirm_pass_entry.get()
        no_plate = self.license_plate_entry.get()

        # if the user input password correctly then only the form is submitted.
        if password == confirm_pass:
            # Insert data into the registration table
            self.cursor.execute('''
                                insert into driver (first_name, last_name, country, city, phone, email, password, no_plate, status,type_id)
                                values (?, ?, ?, ?, ?, ?, ?,?,"Available",2)
                            ''', (first_name, last_name, country, city, phone, email, password, no_plate))
            self.connection.commit()
            # Don't forget to close the connection when done
            self.connection.close()  # This line is not needed here
            print("Database connection closed.")

            CustomMessageBox.show_custom_dialog(self, "Submission Successful!")
            self.close()

            # Clear all the fields after submission
            self.first_name_entry.delete(0, tk.END)
            self.last_name_entry.delete(0, tk.END)
            self.country_entry.delete(0, tk.END)
            self.city_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.confirm_pass_entry.delete(0, tk.END)
            self.license_plate_entry.delete(0, tk.END)



        else:
            CustomMessageBox.show_custom_dialog(self, "Password don't match!")
        pass

    def close(self):
        self.destroy()

    def start(self):
        self.mainloop()

if __name__ == "__main__":
    ds = DriverSignUp()
    ds.start()