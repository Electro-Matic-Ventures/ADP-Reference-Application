from LabelSettings import LabelSettings
from ValueSettings import ValueSettings


class TileSettings:

    label: LabelSettings
    value: ValueSettings

    def __init__(self):
        self.label = LabelSettings()
        self.value = ValueSettings()
        return