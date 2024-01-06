import customtkinter as ctk
from utils.tab import Tab
from components.display_finder import DisplayFinder
from components.stat_multiplier import StatMultiplier
from components.wrathful_clone import WrathfulClone


class Items(ctk.CTkFrame):
    def __init__(self, parent, config, database):
        super().__init__(parent)
        self.config = config
        self.database = database
        frame = ctk.CTkFrame(self)

        frame.pack(fill="both", expand=True)

        MyTabs = Tab(frame)
        MyTabs.tab_display = MyTabs.create_tab("Display Finder")
        MyTabs.tab_stat = MyTabs.create_tab("Stat Multiplier")
        MyTabs.tab_wrathful = MyTabs.create_tab("Clone Wrathful")

        DisplayFinder.show_component(MyTabs.tab_display, self.database)
        StatMultiplier.show_component(MyTabs.tab_stat, self.database)
        WrathfulClone.show_component(MyTabs.tab_wrathful, self.database)
