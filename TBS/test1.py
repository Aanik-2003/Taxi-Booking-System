# import sqlite3
# import tkinter as tk
# from tkinter import ttk, W
#
# import driver_signUp_form
# from driver_signUp_form import DriverSignUp
#
#
# class AdminDashboard(tk.Tk):
#     def __init__(self, admin_id, first_name):
#         super().__init__()
#
#         self.admin_id = admin_id
#         print(self.admin_id)
#         self.first_name = first_name
#
#         # Creating and using external theme
#         self.tk.call('source', "C:\\Users\\user\\PycharmProjects\\taxi_booking\\Azure\\azure.tcl")
#         self.tk.call('set_theme', 'dark')
#
#         self.geometry("600x440""+500+300")
#         self.title(f"Welcome {self.first_name} :)")
#         self.configure(bg="gray10")
#
#         self.frame1 = ttk.Frame(self, width=100, height=440, style="TFrame")  # Add the 'style' attribute
#         self.frame1.place(x=0, y=0)
#
#         self.frame2 = CustomFrame(self, width=580, height=440, style="TFrame")  # Add the 'style' attribute
#         self.frame2.place(x=110, y=0)
#
#         # style to set the background color
#         self.style = ttk.Style(self)
#         self.style.configure("TFrame", background="gray13")
#
#         self.add_driver_btn = tk.Button(self.frame1, width=12, text="Add Driver", bg="#212121", fg="green", command=self.on_driver_btn)
#         self.add_driver_btn.place(x=5, y=5)
#
#         self.add_emp_btn = tk.Button(self.frame1, width=12, text="Add Employee", bg="#212121", fg="green", command=self.on_emp_btn)
#         self.add_emp_btn.place(x=5, y=45)
#
#         self.booking_btn = tk.Button(self.frame1, width=12, text="Booking", bg="#212121", fg="lightblue", command=self.on_booking_btn)
#         self.booking_btn.place(x=5, y=85)
#
#     def on_driver_btn(self):
#         print("driver clicked")
#         self.frame2.clear_widgets()
#         DriverSignUp()
#         self.frame2.driver_frame()
#
#     def on_emp_btn(self):
#         print("VIEW clicked")
#         self.frame2.clear_widgets()
#         self.frame2.view_frame()
#
#     def on_booking_btn(self):
#         self.frame2.clear_widgets()
#         self.frame2.driver_frame()
#         self.frame2.booking_frame(self.admin_id)
#
#     def close(self):
#         self.destroy()
#
#     def start(self):
#         self.mainloop()
#
# class CustomFrame(ttk.Frame):
#     def __init__(self, master=AdminDashboard, **kwargs):
#         super().__init__(master, **kwargs)
#
#         self.admin_id = None
#         print(self.admin_id)
#
#         # actual path to your SQLite database file
#         db_path = "C:\\Users\\user\\PycharmProjects\\taxi_booking\\prc1"
#
#         # Try to connect to the SQLite database
#         try:
#             self.connection = sqlite3.connect(db_path)
#             self.cursor = self.connection.cursor()
#             print("Database connected successfully!")
#
#             self.connection.commit()
#         except sqlite3.Error as e:
#             print(f"Error connecting to the database: {e}")
#
#     def driver_frame(self):
#
#         self.list_opt = ["All", "Available", "Reserved"]
#         self.x = tk.IntVar()
#
#         # Inside the for loop where you create radio buttons
#         for index in range(len(self.list_opt)):
#             radio_btn = tk.Radiobutton(
#                 self,
#                 text=self.list_opt[index],
#                 variable=self.x,
#                 value=index,
#                 foreground="gray",
#                 background="#212121",
#                 command=lambda idx=index: self.radio_changed_driver(idx)
#             )
#             radio_btn.place(x=index * 90, y=5)
#
#         self.column_names = ("Name", "Vehicle Registration Number", "Status")
#         self.driver_tbl = ttk.Treeview(self, columns=self.column_names, show="headings", height=3)
#
#         # Set manual column headings and widths
#         headings_and_widths = [("Name", 60), ("Vehicle Registration Number", 180), ("Status", 80)]
#
#         for col, width in headings_and_widths:
#             self.driver_tbl.heading(col, text=col)
#             self.driver_tbl.column(col, width=width)
#
#         # Place the Treeview below the radio buttons
#         self.driver_tbl.place(x=5, y=30, anchor=tk.NW)
#
#         self.driver_tbl.bind("<<TreeviewSelect>>", self.on_driver_row_selected)
#
#     def radio_changed_driver(self, index):
#         print("Radio changed!")
#         print("Selected value:", index)
#         # Fetch data based on the selected radio button value
#         if index == 0:
#             query = """select driver_id, first_name, no_plate, status from driver """
#         elif index == 1:
#             query = """select driver_id, first_name, no_plate, status from driver where status = "Available" """
#         elif index == 2:
#             query = """select driver_id, first_name, no_plate, status from driver where status = "Reserved" """
#         else:
#             print("Unexpected value:", index)
#             return
#
#         print("Executing query:", query)
#
#         self.cursor.execute(query)
#         data = self.cursor.fetchall()
#
#         # Clear existing data in the Treeview
#         for item in self.driver_tbl.get_children():
#             self.driver_tbl.delete(item)
#
#         # Check if the data list is not empty
#         if data:
#             print(data)
#             self.driver_id = data[0][0]
#             # Assuming data is a list of tuples, where each tuple represents a row from the database
#             for row in data:
#                 self.driver_tbl.insert("", "end", values=row[1:])  # Skip the first column (driver_id)
#         else:
#             print("No data found.")
#
#     def booking_frame(self, admin_id):
#
#         self.admin_id = admin_id
#         print(self.admin_id)
#
#
#         self.confirm_btn = tk.Button(self, text="CONFIRM", bg="#212121", fg="green", command=self.on_confirm_btn)
#         self.confirm_btn.place(x=300, y=170)
#         self.cancel_btn = tk.Button(self, text="CANCEL", bg="#212121", fg="red", command=self.on_cancel_btn)
#         self.cancel_btn.place(x=385, y=170)
#
#         self.list_opt = ["All", "Pending", "Confirmed"]
#         self.x = tk.IntVar()
#
#         # Inside the for loop where you create radio buttons
#         for index in range(len(self.list_opt)):
#             radio_btn = tk.Radiobutton(
#                 self,
#                 text=self.list_opt[index],
#                 variable=self.x,
#                 value=index,
#                 foreground="gray",
#                 background="#212121",
#                 command=lambda idx=index: self.radio_changed_booking(idx)
#             )
#             radio_btn.place(x=index * 90, y=175)
#
#         self.column_names = ("Name", "PickUp Point", "DropOff Point", "PickUp Time", "Status", "Driver")
#         self.booking_tbl = ttk.Treeview(self, columns=self.column_names, show="headings", height=8)
#
#         # Set manual column headings and widths
#         headings_and_widths = [("Name", 45), ("PickUp Point", 90), ("DropOff Point", 90), ("PickUp Time", 90), ("Status", 67), ("Driver", 50)]
#
#         for col, width in headings_and_widths:
#             self.booking_tbl.heading(col, text=col)
#             self.booking_tbl.column(col, width=width)
#
#         # Place the Treeview below the radio buttons
#         self.booking_tbl.place(x=5, y=200, anchor=tk.NW)
#
#         # Bind the event to the callback functions
#         self.booking_tbl.bind("<<TreeviewSelect>>", self.on_booking_row_selected)
#
#     def radio_changed_booking(self, index):
#         print("Radio changed!")
#         print("Selected value:", index)
#         # Fetch data based on the selected radio button value
#         if index == 0:
#             query = """select b.booking_id, c.first_name, b.pickUp_address, b.dropOff_address, b.pickUp_time, b.status from customer c
#                         inner join booking b
#                         where b.cus_id = c.cus_id; """
#         elif index == 1:
#             query = """select b.booking_id, c.first_name, b.pickUp_address, b.dropOff_address, b.pickUp_time, b.status from customer c
#                         inner join booking b
#                         where b.status = "Pending" and b.cus_id = c.cus_id;"""
#         elif index == 2:
#             query = """select b.booking_id, c.first_name, b.pickUp_address, b.dropOff_address, b.pickUp_time, b.status from customer c
#                         inner join booking b where b.status = "Confirmed" and b.cus_id = c.cus_id; """
#         else:
#             print("Unexpected value:", index)
#             return
#
#         print("Executing query:", query)
#
#         self.cursor.execute(query)
#         data = self.cursor.fetchall()
#
#         # Clear existing data in the Treeview
#         for item in self.booking_tbl.get_children():
#             self.booking_tbl.delete(item)
#
#         # Check if the data list is not empty
#         if data:
#             print(data)
#             self.booking_id = data[0][0]
#             print(self.booking_id)
#             # Assuming data is a list of tuples, where each tuple represents a row from the database
#             for row in data:
#                 self.booking_tbl.insert("", "end", values=row[1:])  # Skip the first column (driver_id)
#         else:
#             print("No data found.")
#
#     def on_confirm_btn(self):
#         # Get the selected driver details
#         selected_driver_item = self.driver_tbl.selection()
#         if selected_driver_item:
#             selected_driver_values = self.driver_tbl.item(selected_driver_item, "values")
#             driver_name = selected_driver_values[0]
#             driver_status = selected_driver_values[2]
#             print("Selected Driver Name:", driver_name)
#             print("Selected Driver Status:", driver_status)
#
#             # Get the selected booking details
#             selected_booking_item = self.booking_tbl.selection()
#             if selected_booking_item:
#                 selected_booking_values = self.booking_tbl.item(selected_booking_item, "values")
#                 booking_id = selected_booking_values[0]
#
#                 # Update the booking status and driver details in the database
#                 update_booking_query = f"""
#                     UPDATE booking
#                     SET status = 'Confirmed', driver_id = '{self.driver_id}', admin_id = '{self.admin_id}'
#                     WHERE booking_id = {self.booking_id}
#                 """
#                 self.cursor.execute(update_booking_query)
#                 self.connection.commit()
#                 print("Booking updated successfully!")
#
#                 # Update the driver status in the database
#                 update_driver_query = f"""
#                     UPDATE driver
#                     SET status = 'Reserved'
#                     WHERE driver_id = '{self.driver_id}'
#                 """
#                 self.cursor.execute(update_driver_query)
#                 self.connection.commit()
#                 print("Driver status updated successfully!")
#
#                 # Update the specific row in the booking_tbl
#                 for child in self.booking_tbl.get_children():
#                     values = self.booking_tbl.item(child, 'values')
#                     if values and values[0] == booking_id:
#                         self.booking_tbl.item(child, values=(
#                         values[0], values[1], values[2], values[3], 'Confirmed', driver_name))
#
#                 # Update the specific row in the driver_tbl
#                 for child in self.driver_tbl.get_children():
#                     values = self.driver_tbl.item(child, 'values')
#                     if values and values[0] == self.driver_id:
#                         self.driver_tbl.item(child, values=(values[0], values[1], 'Reserved'))
#
#     def on_driver_row_selected(self, event):
#         # Function to handle the event of selecting a row in the driver_tbl
#         selected_item = self.driver_tbl.selection()
#         if selected_item:
#             selected_values = self.driver_tbl.item(selected_item, "values")
#             d1 = selected_values[0]
#             print("Selected Driver Name:", d1)
#             d2 = selected_values[2]
#             print("Selected Driver status:", d2)
#
#
#     def on_booking_row_selected(self, event):
#         # Function to handle the event of selecting a row in the booking_tbl
#         selected_item = self.booking_tbl.selection()
#         if selected_item:
#             selected_values = self.booking_tbl.item(selected_item, "values")
#             bs = selected_values[-1]
#             print("Selected Booking status:", bs)
#
#     def on_cancel_btn(self):
#         print("cancelled")
#         self.clear_widgets()
#
#     def view_frame(self):
#         pass
#
#     def clear_widgets(self):
#         for widget in self.winfo_children():
#             widget.destroy()
#
#
# if __name__ == "__main__":
#     ad = AdminDashboard()
#     ad.start()
