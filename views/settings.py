import customtkinter as ctk
from components.config_settings import ConfigSettings


class Settings(ctk.CTkFrame):
    def __init__(self, parent, config, database):
        super().__init__(parent)
        self.config = config
        self.database = database
        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True)

        # This stores the references to our entry widgets
        frame.entries = {}
        ConfigSettings.show_component(frame, config, database)
