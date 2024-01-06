import customtkinter as ctk
from utils.config import Config
from utils.database import Database
from utils.widgets import Widgets
from views.items import Items
from views.other import Other
from views.info import Info
from views.settings import Settings
from components.view_buttons import ViewButtons


class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.config = Config()
        self.database = Database(self.config.get_all_data())
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme(self.config.get("app_theme"))

        if self.config.get("app_theme") == "blue":
            self.iconbitmap("assets/blue_icon.ico")
        else:
            self.iconbitmap("assets/green_icon.ico")

        self.title(self.config.get("app_name"))
        self.minsize(1000, 700)

        Widgets.center_window(
            self, int(self.config.get("app_width")), int(self.config.get("app_height"))
        )

        # Tabs
        view_classes = {
            Items: (self, self.config, self.database),
            Other: (self, self.config, self.database),
            Info: (self, self.config, self.database),
            Settings: (self, self.config, self.database),
        }

        self.views = {}

        for view_class, args in view_classes.items():
            view_instance = view_class(*args)
            self.views[view_class] = view_instance
            view_instance.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Sidebar
        sidebar = ctk.CTkFrame(self, fg_color="#333333")
        sidebar.pack(side="left", fill="both", padx=10, pady=10)

        ViewButtons.show_component(sidebar, self.views, Items, "Items", 10, 5)
        ViewButtons.show_component(sidebar, self.views, Other, "Other", 10, 5)
        ViewButtons.show_component(sidebar, self.views, Info, "Info", 10, 5)
        ViewButtons.show_component(sidebar, self.views, Settings, "Settings", 10, 5)
        # Shows the default tab
        ViewButtons.view_button_activate(self.views, Items)


if __name__ == "__main__":
    app = Main()
    app.mainloop()
