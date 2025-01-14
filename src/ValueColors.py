from dataclasses import dataclass
from CONSTANTS import COLORS


@dataclass
class ValueColors:
    selector_background: str = COLORS.WHITE
    selector_foreground: str = COLORS.BLACK
    static_background: str = COLORS.EM_GRAY
    static_foreground: str = COLORS.BLACK