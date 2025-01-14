from dataclasses import dataclass
from CONSTANTS import COLORS


@dataclass
class ButtonColors:
    background:str = COLORS.EM_BLUE
    foreground:str = COLORS.EM_GRAY