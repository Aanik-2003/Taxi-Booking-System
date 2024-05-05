import tkinter as tk
from tkinter import ttk, messagebox

class AdminSignUp(tk.Toplevel):
    def __init__(self):
        super().__init__()

        # Creating and using external theme
        self.tk.call('source', "C:\\Users\\user\\PycharmProjects\\taxi_booking\\Azure\\azure.tcl")
        self.tk.call('set_theme', 'dark')

        self.geometry("600x440""+900+310")
        self.title("Admin Registration Form")
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
        # Add your form submission logic here
        messagebox.showinfo("Submission", "Form submitted successfully!")

    def close(self):
        self.destroy()

    def start(self):
        self.mainloop()

if __name__ == "__main__":
    adsup = AdminSignUp()
    adsup.start()