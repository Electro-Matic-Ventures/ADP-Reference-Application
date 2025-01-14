from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from EndOfFrame import EndOfFrame


class Footer:

    def __init__(self, app):
        self.end_of_frame = EndOfFrame(app, self)
        self.layout = QHBoxLayout()
        self.layout.addLayout(self.end_of_frame.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        self.layout.setAlignment(Qt.AlignLeft)
        return 
    
    def redraw(self):
        self.end_of_frame.redraw()
        self.layout.update()
        return
    
    def change_font_size(self, new_size):
        self.end_of_frame.change_font_size(new_size)
        self.layout.update()
        return