import customtkinter as ctk
from utils.widgets import Widgets


class PlayerStartLocation:
    @staticmethod
    def show_component(tab, database):
        _tab = ctk.CTkFrame(master=tab)
        _tab.pack(side="top", padx=10, pady=20)

        _tab.entries = {}

        Widgets.header(
            _tab,
            "Player Start Location",
            "This sets the starting location of all class/race combinations.",
        )

        Widgets.custom_entry(_tab, _tab.entries, "player_start_map", "Map", 10, 10, 70)
        Widgets.custom_entry(
            _tab, _tab.entries, "player_start_zone", "Zone", 10, 10, 70
        )
        Widgets.custom_entry(_tab, _tab.entries, "player_start_x", "X", 10, 10, 70)
        Widgets.custom_entry(_tab, _tab.entries, "player_start_y", "Y", 10, 10, 70)
        Widgets.custom_entry(_tab, _tab.entries, "player_start_z", "Z", 10, 10, 70)
        Widgets.custom_entry(_tab, _tab.entries, "player_start_o", "O", 10, 10, 70)

        btn_submit = ctk.CTkButton(
            _tab,
            text="Submit",
            width=150,
            command=lambda: PlayerStartLocation.player_start_location_execute(
                database,
                _tab.entries["player_start_map"].get(),
                _tab.entries["player_start_zone"].get(),
                _tab.entries["player_start_x"].get(),
                _tab.entries["player_start_y"].get(),
                _tab.entries["player_start_z"].get(),
                _tab.entries["player_start_o"].get(),
            ),
        )
        btn_submit.pack(side="left", padx=10, pady=5)

    @staticmethod
    def player_start_location_execute(database, map, zone, x, y, z, o):
        query = f"UPDATE playercreateinfo SET map = {map}, zone = {zone}, position_x = {x}, position_y = {y}, position_z = {z}, orientation = {o} WHERE `race` BETWEEN 1 AND 11"
        database.execute(query)
