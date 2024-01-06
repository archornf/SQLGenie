import customtkinter as ctk


class Widgets:
    @staticmethod
    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        window.geometry("%dx%d+%d+%d" % (width, height, x, y))

    @staticmethod
    def custom_entry(frame, dict, identifier, text, entry_padx, entry_pady, width):
        entry = ctk.CTkEntry(frame, width=width, placeholder_text=text)
        entry.pack(side="left", padx=entry_padx, pady=entry_pady)
        dict[identifier] = entry

    @staticmethod
    def header(frame, title, description):
        label_header = ctk.CTkLabel(frame, text=title, font=("", 16))
        label_header.pack(side="top", padx=20, pady=5)

        label_description = ctk.CTkLabel(frame, text=description, font=("", 14))
        label_description.pack(side="top", padx=20, pady=0)
