import customtkinter as ctk
from utils.tab import Tab
from components.player_start_location import PlayerStartLocation


class Other(ctk.CTkFrame):
    def __init__(self, parent, config, database):
        super().__init__(parent)
        self.config = config
        self.database = database
        frame = ctk.CTkFrame(self)
        frame.pack(fill="both", expand=True)

        MyTabs = Tab(frame)
        MyTabs.tab_psl = MyTabs.create_tab("Player Start Location")

        PlayerStartLocation.show_component(MyTabs.tab_psl, self.database)
