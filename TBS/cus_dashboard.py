import sqlite3
import tkinter as tk
import datetime
from tkinter import ttk
from tkcalendar import DateEntry
from custom_msg import CustomMessageBox


class CusDashboard(tk.Tk):
    def __init__(self, cus_id, first_name):
        super().__init__()

        self.cus_id = cus_id
        self.first_name = first_name
        print(cus_id)

        # Creating and using external theme
        self.tk.call('source', "C:\\Users\\user\\PycharmProjects\\taxi_booking\\Azure\\azure.tcl")
        self.tk.call('set_theme', 'dark')

        self.geometry("600x440""+500+300")
        self.title(f"Welcome {self.first_name} :)")
        self.configure(bg="gray10")

        self.frame1 = ttk.Frame(self, width=100, height=440, style="TFrame")  # Add the 'style' attribute
        self.frame1.place(x=0, y=0)

        self.frame2 = CustomFrame(self, width=580, height=440, style="TFrame")  # Add the 'style' attribute
        self.frame2.place(x=110, y=0)

        # style to set the background color
        self.style = ttk.Style(self)
        self.style.configure("TFrame", background="gray13")

        self.create_btn = tk.Button(self.frame1, width=12, text="CREATE", bg="#212121", fg="green", command=self.on_create_btn)
        self.create_btn.place(x=5, y=5)

        self.view_btn = tk.Button(self.frame1, width=12, text="VIEW", bg="#212121", fg="blue", command=self.on_view_btn)
        self.view_btn.place(x=5, y=45)


    def on_create_btn(self):
        print("CREATE clicked")
        self.frame2.clear_widgets()
        self.frame2.create_frame(self.cus_id)

    def on_view_btn(self):
        print("VIEW clicked")
        self.frame2.clear_widgets()
        self.frame2.view_frame(self.cus_id)

    def close(self):
        self.destroy()

    def start(self):
        self.mainloop()

class CustomFrame(ttk.Frame):
    def __init__(self, master=CusDashboard, **kwargs):
        super().__init__(master, **kwargs)

        self.cus_id = None

        # actual path to your SQLite database file
        db_path = "C:\\Users\\user\\PycharmProjects\\taxi_booking\\prc1"

        # Try to connect to the SQLite database
        try:
            self.connection = sqlite3.connect(db_path)
            self.cursor = self.connection.cursor()
            print("Database connected successfully!")

            # Create the registration table if not exists
            self.cursor.execute('''
                                               create table if not exists booking (
                                                booking_id integer primary key autoincrement,
                                                pickUp_address varchar(55),
                                                dropOff_address varchar(55),
                                                pickUp_date date,
                                                pickUp_time varchar(15),
                                                payment_type char(10),
                                                status char(15),
                                                cus_id integer,
                                                driver_id integer,
                                                admin_id integer,
                                                foreign key(cus_id) references customer(cus_id),
                                                foreign key(driver_id) references driver(driver_id),
                                                foreign key(admin_id) references admin(admin_id)
                                               );
                                           ''')
            self.connection.commit()

        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")

    def create_frame(self, cus_id):

        self.cus_id = cus_id
        print(cus_id)

        self.pickup_lbl = tk.Label(self, text="PickUp Point*", font=('Century Gothic', 10),
                                        bg="#212121", fg="gray")
        self.pickup_lbl.place(x=5, y=5)
        self.pickup_entry = tk.Entry(self, width=20, bg="#212121", fg="gray")
        self.pickup_entry.place(x=105, y=5)

        self.dropoff_lbl = tk.Label(self, text="DropOff Point*", font=('Century Gothic', 10),
                                   bg="#212121", fg="gray")
        self.dropoff_lbl.place(x=250, y=5)
        self.dropoff_entry = tk.Entry(self, width=20, bg="#212121", fg="gray")
        self.dropoff_entry.place(x=360, y=5)

        self.pickup_date_lbl = tk.Label(self, text="PickUp Date*", font=('Century Gothic', 10),
                                   bg="#212121", fg="gray")
        self.pickup_date_lbl.place(x=5, y=50)
        self.pickup_date_entry = DateEntry(self, width=17, background="#212121", foreground="gray",
                                           font=('Century Gothic', 10), date_pattern = "dd/mm/yyyy")
        self.pickup_date_entry.place(x=105, y=46)

        self.payment_lbl = tk.Label(self, text="Payment*", font=('Century Gothic', 10),
                                   bg="#212121", fg="gray")
        self.payment_lbl.place(x=5, y=95)
        self.payment_types = ["Cash", "Online"]
        self.payment_types_combo = ttk.Combobox(self, width=15, values=self.payment_types, state="readonly")
        self.payment_types_combo.set("")
        self.payment_types_combo.place(x=105, y=95)

        self.pickup_time_lbl = tk.Label(self, text="PickUp Time*", font=('Century Gothic', 10),
                                        bg="#212121", fg="gray")
        self.pickup_time_lbl.place(x=250, y=50)
        self.pickup_time_entry = tk.Entry(self, width=20, bg="#212121", fg="gray")
        self.pickup_time_entry.place(x=360, y=50)

        self.confirm_btn = tk.Button(self, text="Confirm", bg="#212121", fg="green", width=10, command=self.on_confirm_btn)
        self.confirm_btn.place(x=250, y=95)

        self.cancel_btn = tk.Button(self, text="Cancel", bg="#212121", fg="red", width=10,
                                     command=self.on_cancel_btn)
        self.cancel_btn.place(x=350, y=95)

        self.column_names = ("Name", "PickUp Point", "DropOff Point", "PickUp Time", "Status")
        self.booking_tbl = ttk.Treeview(self, columns=self.column_names, show="headings", height=11)

        # Set manual column headings and widths
        headings_and_widths = [("Name", 40), ("PickUp Point", 90), ("DropOff Point", 90), ("PickUp Time", 90),
                               ("Status", 50)]

        for col, width in headings_and_widths:
            self.booking_tbl.heading(col, text=col)
            self.booking_tbl.column(col, width=width)

        # Fetch data from the booking table
        query = """select c.first_name, b.pickUp_address, b.dropOff_address, b.pickUp_time, b.status from customer c
                        inner join booking b on b.cus_id=c.cus_id
                        where c.cus_id = ? and b.status = "Pending";"""
        self.cursor.execute(query, (self.cus_id,))
        data = self.cursor.fetchall()

        # Clear existing data in the Treeview
        for item in self.booking_tbl.get_children():
            self.booking_tbl.delete(item)

        # Insert new data into the Treeview
        for row in data:
            self.booking_tbl.insert("", "end", values=row)

        self.booking_tbl.place(x=0, y=140)


    def on_confirm_btn(self):

        pickUp_address = self.pickup_entry.get()
        dropOff_address = self.dropoff_entry.get()
        pickUp_date = self.pickup_date_entry.get_date()
        pickUp_time = self.pickup_time_entry.get()
        payment_type = self.payment_types_combo.get()

        if pickUp_date < datetime.date.today():
            self.show_custom_dialog("Incorrect Date!")
        else:
            # Insert data into the booking table
            self.cursor.execute('''
                                   insert into booking (pickUp_address, dropOff_address, pickUp_date, pickUp_time, payment_type, status, cus_id)
                                   values (?, ?, ?, ?, ?, "Pending",?)
                               ''', (pickUp_address, dropOff_address, pickUp_date, pickUp_time, payment_type, self.cus_id))
            self.connection.commit()

            self.show_custom_dialog("Booking Successful.")


            print("Confirmed")

            # Clear all the fields after submission
            self.pickup_entry.delete(0, tk.END)
            self.dropoff_entry.delete(0, tk.END)
            self.pickup_date_entry.delete(0, tk.END)
            self.pickup_time_entry.delete(0, tk.END)
            self.payment_types_combo.set("")

            # Fetch data from the booking table
            query = """select c.first_name, b.pickUp_address, b.dropOff_address, b.pickUp_time, b.status from customer c
                                inner join booking b on b.cus_id=c.cus_id
                                where c.cus_id = ? and b.status = "Pending";"""
            self.cursor.execute(query, (self.cus_id,))
            data = self.cursor.fetchall()

            # Clear existing data in the Treeview
            for item in self.booking_tbl.get_children():
                self.booking_tbl.delete(item)

            # Insert new data into the Treeview
            for row in data:
                self.booking_tbl.insert("", "end", values=row)

    def on_cancel_btn(self):
        print("cancelled")
        self.clear_widgets()

    def show_custom_dialog(self, message):

        custom_dialog = CustomMessageBox(self, message)
        custom_dialog.geometry("300x100+600+400")
        custom_dialog.wait_window()

    def view_frame(self, cus_id):
        self.clear_widgets()  # Clear existing widgets

        self.cus_id = cus_id
        print(cus_id)

        self.pickup_lbl = tk.Label(self, text="PickUp Point*", font=('Century Gothic', 10),
                                   bg="#212121", fg="gray")
        self.pickup_lbl.place(x=5, y=5)
        self.pickup_entry = tk.Entry(self, width=20, bg="#212121", fg="gray")
        self.pickup_entry.place(x=105, y=5)

        self.dropoff_lbl = tk.Label(self, text="DropOff Point*", font=('Century Gothic', 10),
                                    bg="#212121", fg="gray")
        self.dropoff_lbl.place(x=250, y=5)
        self.dropoff_entry = tk.Entry(self, width=20, bg="#212121", fg="gray")
        self.dropoff_entry.place(x=360, y=5)

        # Create DateEntry widget with the validation function
        self.pickup_date_entry = DateEntry(self, width=17, background="#212121", foreground="gray",
                                           font=('Century Gothic', 10), date_pattern="dd-mm-yyyy")

        self.pickup_date_entry.place(x=105, y=46)

        self.pickup_date_lbl = tk.Label(self, text="PickUp Date*", font=('Century Gothic', 10),
                                        bg="#212121", fg="gray")
        self.pickup_date_lbl.place(x=5, y=50)
        self.pickup_date_entry = DateEntry(self, width=17, background="#212121", foreground="gray",
                                           font=('Century Gothic', 10), date_pattern="dd/mm/yyyy")
        self.pickup_date_entry.place(x=105, y=46)

        self.pickup_time_lbl = tk.Label(self, text="PickUp Time*", font=('Century Gothic', 10),
                                        bg="#212121", fg="gray")
        self.pickup_time_lbl.place(x=250, y=50)
        self.pickup_time_entry = tk.Entry(self, width=20, bg="#212121", fg="gray")
        self.pickup_time_entry.place(x=360, y=50)

        self.payment_lbl = tk.Label(self, text="Payment*", font=('Century Gothic', 10),
                                    bg="#212121", fg="gray")
        self.payment_lbl.place(x=5, y=95)
        self.payment_types = ["Cash", "Online"]
        self.payment_types_combo = ttk.Combobox(self, width=15, values=self.payment_types, state="readonly")
        self.payment_types_combo.set("")
        self.payment_types_combo.place(x=105, y=95)

        self.update_btn = tk.Button(self, text="UPDATE", bg="#212121", fg="green", width=10,
                                    command=self.on_update_btn)
        self.update_btn.place(x=250, y=95)

        self.delete_btn = tk.Button(self, text="DELETE", bg="#212121", fg="red", width=10,
                                    command=self.on_delete_btn)
        self.delete_btn.place(x=350, y=95)

        self.list_opt = ["All", "Pending", "Confirmed"]
        self.x = tk.IntVar()

        # Inside the for loop where you create radio buttons
        for index in range(len(self.list_opt)):
            radio_btn = tk.Radiobutton(
                self,
                text=self.list_opt[index],
                variable=self.x,
                value=index,
                foreground="gray",
                background="#212121",
                command=lambda idx=index: self.radio_changed_booking(idx)
            )
            radio_btn.place(x=index * 90, y=155)

        self.column_names = ("Name", "PickUp Point", "DropOff Point", "PickUp Time", "Status", "Driver")
        self.booking_tbl = ttk.Treeview(self, columns=self.column_names, show="headings", height=11)

        # Set manual column headings and widths
        headings_and_widths = [("Name", 35), ("PickUp Point", 80), ("DropOff Point", 80), ("PickUp Time", 80),
                               ("Status", 50), ("Driver", 35)]

        for col, width in headings_and_widths:
            self.booking_tbl.heading(col, text=col)
            self.booking_tbl.column(col, width=width)

        self.booking_tbl.place(x=0, y=190)

        # Bind the event to the callback functions
        self.booking_tbl.bind("<<TreeviewSelect>>", self.on_booking_row_selected)

        # Fetch data from the booking table
        query = """select c.first_name, b.pickUp_address, b.dropOff_address, b.pickUp_time, b.status,d.first_name from customer c
                                        inner join booking b on b.cus_id=c.cus_id
                                        inner join driver d on b.driver_id = d.driver_id
                                        where c.cus_id = ? and (b.status="Pending" or b.status="Confirmed"); """
        self.cursor.execute(query, (self.cus_id,))
        data = self.cursor.fetchall()

        # Clear existing data in the Treeview
        for item in self.booking_tbl.get_children():
            self.booking_tbl.delete(item)

        # Insert new data into the Treeview
        for row in data:
            self.booking_tbl.insert("", "end", values=row)

    def radio_changed_booking(self, index):
        print("Radio changed!")
        print("Selected value:", index)
        # Fetch data based on the selected radio button value
        if index == 0:
            query = """select b.booking_id, c.first_name, b.pickUp_address, b.dropOff_address, b.pickUp_time, b.status,d.first_name from customer c
                        inner join booking b on b.cus_id = c.cus_id
                        inner join driver d on b.driver_id = d.driver_id
                        where c.cus_id=? and (b.status="Confirmed" or (b.status="Pending"));"""
        elif index == 1:
            query = """select b.booking_id, c.first_name, b.pickUp_address, b.dropOff_address, b.pickUp_time, b.status from customer c
                        inner join booking b        
                        on b.cus_id = c.cus_id
                        where b.status = "Pending" and c.cus_id =?;"""
        elif index == 2:
            query = """select b.booking_id, c.first_name, b.pickUp_address, b.dropOff_address, b.pickUp_time, b.status,d.first_name from customer c
                        inner join booking b on b.cus_id = c.cus_id
                        inner join driver d on b.driver_id = d.driver_id
                        where b.status = "Confirmed" and c.cus_id =?; """
        else:
            print("Unexpected value:", index)
            return

        print("Executing query:", query)

        self.cursor.execute(query, (self.cus_id,))
        data = self.cursor.fetchall()

        # Clear existing data in the Treeview
        for item in self.booking_tbl.get_children():
            self.booking_tbl.delete(item)

        # Check if the data list is not empty
        if data:
            print(data)
            self.booking_id = data[0][0]
            print(self.booking_id)
            # Assuming data is a list of tuples, where each tuple represents a row from the database
            for row in data:
                self.booking_tbl.insert("", "end", values=row[1:])

        else:
            print("No data found.")

    def on_booking_row_selected(self, event):
        # Function to handle the event of selecting a row in the booking_tbl
        selected_item = self.booking_tbl.selection()
        if selected_item:
            selected_values = self.booking_tbl.item(selected_item, "values")
            print("Selected Booking status:", selected_values)
            self.pickup_entry.delete(0, tk.END)
            self.pickup_entry.insert(0, selected_values[1])

            self.dropoff_entry.delete(0, tk.END)
            self.dropoff_entry.insert(0, selected_values[2])

            self.pickup_time_entry.delete(0, tk.END)
            self.pickup_time_entry.insert(0, selected_values[3])

    def on_update_btn(self):
        # Retrieve values from entry widgets
        pickup_address = self.pickup_entry.get()
        dropoff_address = self.dropoff_entry.get()
        pickup_date = self.pickup_date_entry.get_date()
        pickup_time = self.pickup_time_entry.get()
        payment_type = self.payment_types_combo.get()


        # Check if the booking status is "Pending"
        selected_item = self.booking_tbl.selection()
        if selected_item:
            selected_values = self.booking_tbl.item(selected_item, "values")
            if selected_values and selected_values[4] == "Pending":
                if pickup_date > datetime.date.today():
                    # Update data in the booking table
                    query = '''
                        update booking
                        set pickUp_address=?, dropOff_address=?, pickUp_date=?, pickUp_time=?, payment_type=?
                        where cus_id=? AND status="Pending";
                    '''
                    # Execute the query with the provided values
                    self.cursor.execute(query, (
                    pickup_address, dropoff_address, pickup_date, pickup_time, payment_type, self.cus_id))
                    self.connection.commit()

                    # Show a message indicating the update
                    self.show_custom_dialog("Booking updated successfully.")

                    # Fetch and display updated data in the Treeview
                    self.view_frame(self.cus_id)

                else:
                    self.show_custom_dialog("Invalid Date!")
            else:
                self.show_custom_dialog("Cannot update confirmed booking.")
        else:
            self.show_custom_dialog("No booking selected.")


    def on_delete_btn(self):
        # Check if any booking is selected
        selected_item = self.booking_tbl.selection()
        if selected_item:
            selected_values = self.booking_tbl.item(selected_item, "values")
            if selected_values:
                # Check if the booking status is "Pending" before updating to "Cancelled"
                if selected_values[4] == "Pending":

                    # Update the booking status to "Cancelled" in the database using booking_id
                    cancel_query = """update booking set status="Cancelled" WHERE booking_id=? and status="Pending";"""
                    self.cursor.execute(cancel_query, (self.booking_id,))
                    self.connection.commit()

                    # Show a message indicating the cancellation
                    self.show_custom_dialog("Booking cancelled successfully.")
                    self.connection.close()
                    # Fetch and display updated data in the Treeview
                    self.view_frame(self.cus_id)

                else:
                    self.show_custom_dialog("Cannot cancel a confirmed booking.")
            else:
                self.show_custom_dialog("No booking selected.")
        else:
            self.show_custom_dialog("No booking selected.")



    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    cd = CusDashboard()
    cd.start()
