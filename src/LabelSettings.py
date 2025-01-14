from CONSTANTS import HEIGHT_LABEL_LOOKUP, WIDTH_LOOKUP
from Dimensions import Dimensions
from Font import Font
from LabelColors import LabelColors


class LabelSettings:

    colors: LabelColors
    dimensions: Dimensions
    font: Font

    def __init__(self, font_size="16"):
        self.initialize(font_size)
        return

    def initialize(self, font_size="16"):
        if isinstance(font_size, int):
            font_size = str(font_size)
        self.colors = LabelColors()
        self.dimensions = Dimensions()
        self.dimensions.width = WIDTH_LOOKUP[font_size]
        self.dimensions.height = HEIGHT_LABEL_LOOKUP[font_size]
        self.font = Font(size=font_size,weight="bold")
        return