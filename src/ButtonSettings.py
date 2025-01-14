from Dimensions import Dimensions
from Font import Font
from ButtonColors import ButtonColors


class ButtonSettings:

    colors: ButtonColors
    dimensions: Dimensions
    font: Font

    def __init__(self, font_size="16"):
        self.initialize(font_size)
        return

    def initialize(self, font_size="16"):
        if isinstance(font_size, int):
            font_size = str(font_size)
        self.colors = ButtonColors()
        self.dimensions = Dimensions()
        self.dimensions.redim_button(font_size)
        self.font = Font(size=font_size,weight="bold")
        return