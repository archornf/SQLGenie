import json
from utils.error import ErrorSystem


class Config:
    def __init__(self, file_name="config.json"):
        self.file_name = file_name
        self.config_data = {}
        self.load()

    def load(self):
        try:
            with open(self.file_name, "r") as file:
                self.config_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            ErrorSystem.open("File:", f"Error: {self.file_name} not found.")

    def save(self, data):
        try:
            with open(self.file_name, "w") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            ErrorSystem.open("File:", f"Error: {self.file_name} not found.")

    def get_all_data(self):
        return self.config_data

    def get(self, key):
        return self.config_data[key]

    def set(self, key, value):
        self.config_data[key] = value
        self.save(self.config_data)
