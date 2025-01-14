from FrameColors import FrameColors
from Dimensions import Dimensions
from Font import Font


class FrameSettings:

    colors: FrameColors
    dimensions: Dimensions
    font: Font

    def __init__(self):
        self.colors = FrameColors()
        self.dimensions = Dimensions()
        self.dimensions.redim_frame("16")
        self.font = Font()
        return