from Caret import Caret
from Dimensions import Dimensions
from Font import Font
from ValueColors import ValueColors


class ValueSettings:

    caret: Caret
    colors: ValueColors
    dimensions: Dimensions
    font: Font

    def __init__(self, font_size="16"):
        self.initialize(font_size)
        return

    def initialize(self, font_size="16"):
        if isinstance(font_size, int):
            font_size = str(font_size)
        self.caret = Caret(font_size)
        self.colors = ValueColors()
        self.dimensions = Dimensions()
        self.dimensions.redim_value(font_size)
        self.font = Font(size=font_size)
        return
    
    def change_font_size(self, font_size):
        self.caret.redim(font_size)
        self.dimensions.redim_value(font_size)
        self.font.size = font_size
