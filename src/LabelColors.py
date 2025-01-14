from dataclasses import dataclass
from CONSTANTS import COLORS

@dataclass
class LabelColors:
    background: str = COLORS.EM_BLUE
    foreground: str = COLORS.EM_GRAY