from dataclasses import dataclass


@dataclass
class FrameColors:
    background: str = "255,255,255"
    background_changed: str = "255,155,155"
    foreground: str = "0,0,0"
    foreground_changed: str = "255,255,255"