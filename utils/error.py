import customtkinter as ctk
from utils.logger import Logger


class ErrorSystem(ctk.CTkToplevel):
    _error_system = None

    def __init__(self):
        super().__init__()
        self.width = 500
        self.height = 80
        self.label = None
        self.logger = Logger("error.log")

    def setup(self, title, message):
        self.title(title)

        if not self.label:
            self.label = ctk.CTkLabel(self, font=("", 16))
            self.label.pack(padx=20, pady=20)

        message_str = str(message)

        if len(message_str) == 0:
            self.label.configure(text="Error: Unknown")
        elif len(message_str) > 40:
            self.label.configure(
                text="Error wouldn't fit here and has been logged in error.log."
            )
            self.logger.log(message_str)
        else:
            self.label.configure(text="Error: " + message_str)
            self.logger.log(message_str)

        self.center()
        self.focus_set()
        self.lift()
        self.grab_set()

    def center(self):
        screen_width = int(self.winfo_screenwidth())
        screen_height = int(self.winfo_screenheight())

        position_x = int((screen_width - self.width) / 2)
        position_y = int((screen_height - self.height) / 2)

        self.geometry(f"{self.width}x{self.height}+{position_x}+{position_y}")

    @classmethod
    def open(cls, title, message):
        if cls._error_system is None or not cls._error_system.winfo_exists():
            cls._error_system = ErrorSystem()
        cls._error_system.setup(title, message)
