import customtkinter as ctk


class ConfigSettings:
    @staticmethod
    def show_component(frame, config, database):
        _frame = ctk.CTkFrame(master=frame, fg_color="transparent")
        _frame.pack(side="top", padx=10, pady=20)
        # App Settings
        _frame.entries = {}

        label = ctk.CTkLabel(_frame, text="APP Settings", font=("", 18))
        label.pack(side="top", padx=5, pady=15)

        # Window Size
        ConfigSettings.make_settings_element(
            _frame, "app_width", "Window Width:", config.get("app_width"), 6
        )

        ConfigSettings.make_settings_element(
            _frame, "app_height", "Window Height:", config.get("app_height"), 4
        )

        # App Theme
        ConfigSettings.make_settings_element(
            _frame, "app_theme", "Theme:", config.get("app_theme"), 31
        )

        # MYSQL
        label = ctk.CTkLabel(_frame, text="MySQL Settings", font=("", 18))
        label.pack(side="top", padx=5, pady=15)

        # Host
        ConfigSettings.make_settings_element(
            _frame, "mysql_host", "Host:", config.get("mysql_host"), 40
        )

        # Port
        ConfigSettings.make_settings_element(
            _frame, "mysql_port", "Port:", config.get("mysql_port"), 42
        )

        # User
        ConfigSettings.make_settings_element(
            _frame, "mysql_user", "User:", config.get("mysql_user"), 42
        )

        # Password
        ConfigSettings.make_settings_element(
            _frame, "mysql_password", "Password:", config.get("mysql_password"), 22
        )

        # Database
        ConfigSettings.make_settings_element(
            _frame, "mysql_database", "World Database:", config.get("mysql_database"), 0
        )

        # Save Button
        btn_save = ctk.CTkButton(
            _frame,
            text="Save",
            width=485,
            command=lambda: ConfigSettings.save(_frame, config, database),
        )
        btn_save.pack(padx=10, pady=10)

    # This is just a function to reduce some code duplication.
    @staticmethod
    def make_settings_element(frame, entry_name, text, entry_text, label_padx):
        _frame = ctk.CTkFrame(frame)
        _frame.pack(side="top", padx=15, pady=5)

        label = ctk.CTkLabel(_frame, text=text, font=("", 16))
        label.pack(side="left", padx=label_padx + 8, pady=10)

        entry = ctk.CTkEntry(_frame, width=336)
        entry.pack(side="left", padx=10, pady=10)
        entry.insert(0, entry_text)

        frame.entries[entry_name] = entry

    # Save Settings To Config File
    @staticmethod
    def save(frame, config, database):
        for entry in frame.entries.items():
            config.set(entry[0], entry[1].get())
        config.save(config.get_all_data())
        config.load()
        database.reload_configs(config.get_all_data())
