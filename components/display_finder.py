import customtkinter as ctk
import os
import subprocess
from utils.widgets import Widgets
from utils.error import ErrorSystem


class DisplayFinder:
    @staticmethod
    def show_component(tab, database):
        _tab = ctk.CTkFrame(master=tab, fg_color="transparent")
        _tab.pack(side="top", padx=10, pady=20)

        Widgets.header(
            _tab,
            "Display Finder",
            "This takes entry id / name of an item and finds their display id.",
        )

        _tab.var_search = ctk.IntVar(value=0)

        _tab.group = ctk.CTkFrame(_tab, fg_color="#242424")
        _tab.group.pack(side="top", pady=2, padx=10)

        _tab.label_search = ctk.CTkLabel(_tab.group, text="Search By:", font=("", 16))
        _tab.label_search.pack(side="left", pady=10, padx=30)

        _tab.btn_entry = ctk.CTkRadioButton(
            _tab.group, text="Entry", variable=_tab.var_search, value=0
        )
        _tab.btn_entry.pack(side="left", pady=5)

        _tab.btn_name = ctk.CTkRadioButton(
            _tab.group, text="Name", variable=_tab.var_search, value=1
        )
        _tab.btn_name.pack(side="left", pady=5)

        _tab.entry = ctk.CTkEntry(_tab, width=336, placeholder_text="Entry ID / Name")
        _tab.entry.pack(padx=10, pady=5)
        _tab.label_result = ctk.CTkLabel(_tab, text="", font=("", 16), width=400)
        _tab.btn_submit = ctk.CTkButton(
            _tab,
            text="Search & Copy",
            width=336,
            command=lambda: DisplayFinder.display_execute(
                _tab,
                _tab.var_search.get(),
                _tab.entry.get(),
                _tab.label_result,
                database,
            ),
        )
        _tab.btn_submit.pack(padx=10, pady=2)
        _tab.label_result.pack(side="top", pady=5, padx=10)

    @staticmethod
    def display_execute(tab, type, value, label, database):
        # If entry is selected
        if type == 0:
            query = "SELECT displayid FROM item_template WHERE entry = %s;"
            result = database.fetch(query, (value,))
        else:  # If name is selected as its only other option
            query = "SELECT displayid FROM item_template WHERE name LIKE %s;"
            result = database.fetch(query, (value,))

        # Check if the result is empty or None
        if not result:
            label.configure(text="No results were found.")
            ErrorSystem.open("Error:", "Error: No results were found.")
            return

        # If there are results, then display and copy the first result
        try:
            output = f"Display ID: {result[0]['displayid']} and it was copied to your clipboard."
            label.configure(text=output)
            DisplayFinder.copy_to_clipboard(tab, result[0]["displayid"])
        except Exception as error:
            ErrorSystem.open("Error:", error)

    @staticmethod
    def copy_to_clipboard(instance, value):
        if os.name == "nt":
            value = str(value)
            process = subprocess.Popen(["clip"], stdin=subprocess.PIPE)
            process.communicate(value.encode("utf-8"))
        else:
            instance.clipboard_clear()
            instance.clipboard_append(value)
            instance.update()
