
import tkinter as tk

class CustomMessageBox(tk.Toplevel):
    def __init__(self, parent, message):
        super().__init__(parent)

        self.title("Message Box")
        self.geometry("300x100""+1046+420")
        self.resizable(False, False)

        self.label = tk.Label(self, text=message, padx=10, pady=10)
        self.label.pack()

        self.ok_button = tk.Button(self, text="OK", command=self.destroy)
        self.ok_button.pack()

    # @staticmethod
    # def show_custom_dialog(parent, message):
    #     custom_dialog = CustomMessageBox(parent, message)
    #     custom_dialog.transient(parent)
    #     custom_dialog.grab_set()
    #     parent.wait_window(custom_dialog)

    @staticmethod
    def show_custom_dialog(parent, message, width=300, height=100, x_position=None, y_position=None):
        custom_dialog = CustomMessageBox(parent, message)

        if x_position is not None and y_position is not None:
            custom_dialog.geometry(f"{width}x{height}+{x_position}+{y_position}")
        else:
            custom_dialog.geometry(f"{width}x{height}")

        custom_dialog.transient(parent)
        custom_dialog.grab_set()
        parent.wait_window(custom_dialog)
