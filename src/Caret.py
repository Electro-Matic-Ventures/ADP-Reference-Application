from dataclasses import dataclass
from CONSTANTS import CARET_SIZES, CARET_PADDING


@dataclass
class Caret:

    size: str = "19x14"
    padding: str = "5"

    def __init__(self, font_size):
        self.redim(font_size)
        return

    def redim(self, font_size):
        self.size = CARET_SIZES[font_size]
        self.padding = CARET_PADDING[font_size]
        return