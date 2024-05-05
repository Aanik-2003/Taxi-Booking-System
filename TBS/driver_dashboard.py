import sqlite3
import tkinter as tk
from tkinter import ttk


class DriverDashboard(tk.Tk):
    def __init__(self, driver_id, first_name):
        super().__init__()

        self.driver_id = driver_id
        self.first_name = first_name
        print(driver_id)

        # Creating and using external theme
        self.tk.call('source', "C:\\Users\\user\\PycharmProjects\\taxi_booking\\Azure\\azure.tcl")
        self.tk.call('set_theme', 'dark')

        self.geometry("600x440""+500+300")
        self.title(f"Welcome {first_name} :)")
        self.configure(bg="gray10")

        self.frame1 = ttk.Frame(self, width=100, height=440, style="TFrame")  # Add the 'style' attribute
        self.frame1.place(x=0, y=0)

        self.frame2 = CustomFrame(self, width=580, height=440, style="TFrame")  # Add the 'style' attribute
        self.frame2.place(x=110, y=0)

        # style to set the background color
        self.style = ttk.Style(self)
        self.style.configure("TFrame", background="gray13")

        self.view_btn = tk.Button(self.frame1, width=12, text="VIEW", bg="#212121", fg="blue", command=self.on_view_btn)
        self.view_btn.place(x=5, y=5)

    def on_view_btn(self):
        print("view clicked")
        self.frame2.clear_widgets()
        self.frame2.view_frame(self.driver_id)

    def close(self):
        self.destroy()

    def start(self):
        self.mainloop()


class CustomFrame(ttk.Frame):
    def __init__(self, master=DriverDashboard, **kwargs):
        super().__init__(master, **kwargs)

        # actual path to your SQLite database file
        db_path = "C:\\Users\\user\\PycharmProjects\\taxi_booking\\prc1"

        # Try to connect to the SQLite database
        try:
            self.connection = sqlite3.connect(db_path)
            self.cursor = self.connection.cursor()
            print("Database connected successfully!")

            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")

    def view_frame(self, driver_id):
        self.clear_widgets()  # Clear existing widgets

        self.driver_id = driver_id
        print(driver_id)

        self.heading_lbl = tk.Label(self, text="Your Upcoming Trips", font=('Century Gothic', 15, "underline"),
                                    bg="#212121", fg="gray")
        self.heading_lbl.place(x=145, y=5)

        self.column_names = ("Name", "PickUp Point", "DropOff Point", "PickUp Date", "PickUp Time", "Status")
        self.booking_tbl = ttk.Treeview(self, columns=self.column_names, show="headings", height=11)

        # Set manual column headings and widths
        headings_and_widths = [("Name", 40), ("PickUp Point", 85), ("DropOff Point", 85), ("PickUp Date", 85),
                               ("PickUp Time", 75), ("Status", 65)]

        for col, width in headings_and_widths:
            self.booking_tbl.heading(col, text=col)
            self.booking_tbl.column(col, width=width)

        self.booking_tbl.place(x=0, y=45)

        # Fetch data from the booking table
        query = """select c.first_name, b.pickUp_address, b.dropOff_address, b.pickUp_date, b.pickUp_time, b.status
                    from booking b
                    inner join customer c on c.cus_id = b.cus_id 
                    inner join driver d on b.driver_id = d.driver_id 
                    where d.driver_id = ?;"""

        self.cursor.execute(query, (self.driver_id,))
        data = self.cursor.fetchall()

        # Clear existing data in the Treeview
        for item in self.booking_tbl.get_children():
            self.booking_tbl.delete(item)

        # Insert new data into the Treeview
        for row in data:
            self.booking_tbl.insert("", "end", values=row)

        self.connection.close()

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    dd = DriverDashboard()
    dd.start()
