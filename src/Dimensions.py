from dataclasses import dataclass
from CONSTANTS import HEIGHT_BUTTON_LOOKUP, HEIGHT_LABEL_LOOKUP, HEIGHT_VALUE_LOOKUP, WIDTH_LOOKUP

@dataclass
class Dimensions:
    
    height: int = 0
    width: int = 0

    def redim_button(self, new_font_size):
        self.height = HEIGHT_BUTTON_LOOKUP[new_font_size]
        self.width = WIDTH_LOOKUP[new_font_size]
        return

    def redim_label(self, new_font_size):
        self.height = HEIGHT_LABEL_LOOKUP[new_font_size]
        self.width = WIDTH_LOOKUP[new_font_size]
        return
    
    def redim_value(self, new_font_size):
        self.height = HEIGHT_VALUE_LOOKUP[new_font_size]
        self.width = WIDTH_LOOKUP[new_font_size]
        return
    
    def redim_frame(self, new_font_size):
        return