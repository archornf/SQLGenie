import customtkinter as ctk
import webbrowser


class ProjectInfo:
    @staticmethod
    def show_component(tab, config):
        _frame = ctk.CTkFrame(master=tab, fg_color="transparent")
        _frame.pack(side="top", padx=10, pady=20)

        label_header = ctk.CTkLabel(
            _frame, text="SQLGenie", font=("", 26), bg_color="transparent"
        )
        label_header.pack(side="top", padx=5, pady=25)

        label_copy = ctk.CTkLabel(
            _frame, text="Copyright (c) 2023 SQLGenie contributors", font=("", 20)
        )
        label_copy.pack(side="top", padx=15)

        label_version = ctk.CTkLabel(
            _frame, text="Version: " + config.get("app_version"), font=("", 20)
        )
        label_version.pack(side="top", padx=15)

        btn_github = ctk.CTkButton(
            _frame, text="GitHub Page", width=300, command=lambda: open_github()
        )
        btn_github.pack(side="top", padx=5, pady=25)

        def open_github():
            webbrowser.open("https://github.com/MrTacoTastic/SQLGenie")
