import customtkinter as ctk


class Tab(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    tabs = {}

    def create_tab(self, tab_name):
        self._segmented_button.configure(font=("", 18))
        self.add(tab_name)
        self.tabs[tab_name] = self.tab(tab_name)
        self.tabs[tab_name]._border_color = None
        self.pack(padx=10, pady=10, fill="both", expand=True)
        return self.tabs[tab_name]

    def get_tab(self, tab_name):
        return self.tabs[tab_name]

    def get_tabs(self):
        return self.tabs
