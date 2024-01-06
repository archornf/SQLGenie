import customtkinter as ctk
from components.project_info import ProjectInfo


class Info(ctk.CTkFrame):
    def __init__(self, parent, config, database):
        super().__init__(parent)
        self.config = config
        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True)
        ProjectInfo.show_component(frame, config)
