from CONSTANTS import PADDING


class Settings:

    def __init__(self):
        self.padding = PADDING["16"]
        return

    def change_font_size(self, font_size):
        self.padding = PADDING[font_size]
        return