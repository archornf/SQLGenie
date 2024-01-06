import os
import datetime


class Logger:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None

    def open(self):
        print("Opening " + self.file_path)
        if self.file is None:
            try:
                self.file = open(self.file_path, "a")
            except FileNotFoundError:
                os.makedirs(os.path.dirname(self.file_path))
                self.file = open(self.file_path, "a")

    def save(self):
        print("Saving " + self.file_path)
        if self.file:
            self.file.close()
            self.file = None

    def log(self, line):
        if self.file is None:
            date = datetime.datetime.now().strftime("[%H:%M:%S]:")
            self.open()
            self.file.write(date + line + "\n")
            self.save()
