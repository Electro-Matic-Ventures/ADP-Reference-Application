from dataclasses import dataclass


@dataclass
class Font:
    family: str = "Consolas"
    size: str = "16"
    style: str = "normal"
    weight: str = "normal"