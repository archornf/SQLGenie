import customtkinter as ctk
from utils.widgets import Widgets


class StatMultiplier:
    @staticmethod
    def show_component(tab, database):
        _tab = ctk.CTkFrame(tab, fg_color="transparent")
        _tab.pack(side="top", padx=10, pady=20)

        _tab.entries = {}

        Widgets.header(
            _tab,
            "Stat Multiplier",
            "This takes a range of items and multiplies their stats by a given number.",
        )

        Widgets.custom_entry(
            _tab, _tab.entries, "stat_first", "First Entry", 12, 10, 150
        )

        Widgets.custom_entry(_tab, _tab.entries, "stat_last", "Last Entry", 6, 10, 150)

        Widgets.custom_entry(
            _tab, _tab.entries, "stat_multiplier", "Multiplier", 12, 10, 150
        )

        btn_submit = ctk.CTkButton(
            _tab,
            text="Submit",
            width=150,
            command=lambda: StatMultiplier.stat_execute(
                database,
                _tab.entries["stat_first"].get(),
                _tab.entries["stat_last"].get(),
                _tab.entries["stat_multiplier"].get(),
            ),
        )
        btn_submit.pack(side="left", padx=12, pady=10)

    @staticmethod
    def stat_execute(database, first, last, multiplier):
        query = f"""
            UPDATE item_template
            SET
                stat_value1 = (stat_value1 * {multiplier}),
                stat_value2 = (stat_value2 * {multiplier}),
                stat_value3 = (stat_value3 * {multiplier}),
                stat_value4 = (stat_value4 * {multiplier}),
                stat_value5 = (stat_value5 * {multiplier}),
                stat_value6 = (stat_value6 * {multiplier}),
                stat_value7 = (stat_value7 * {multiplier}),
                stat_value8 = (stat_value8 * {multiplier}),
                stat_value9 = (stat_value9 * {multiplier}),
                stat_value10 = (stat_value10 * {multiplier}),
                dmg_min1 = (dmg_min1 * {multiplier}),
                dmg_max1 = (dmg_max1 * {multiplier}),
                armor = (armor * {multiplier}),
                block = (block * {multiplier})
            WHERE
                entry BETWEEN {first} and {last};"""

        database.execute(query)
