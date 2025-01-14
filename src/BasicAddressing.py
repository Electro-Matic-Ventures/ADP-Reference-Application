from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from typing import TYPE_CHECKING
from File import File
from ConstructedElement import ConstructedElement
from LayoutTools import LayoutTools


if TYPE_CHECKING:
    from Addressing import Addressing
    from MainWindow import MainWindow


class BasicAddressing:


    def __init__(self, app: "MainWindow", host: "Addressing"):
        self.app: "MainWindow" = app
        self.host: "Addressing" = host
        self.constructed_element: ConstructedElement = ConstructedElement()
        self.file: File = File(self.app, self)
        self.layout: QHBoxLayout = self.__make_layout()
        self.hide()
        return
    
    def __make_layout(self):
        layout: QHBoxLayout = QHBoxLayout()
        layout.addLayout(self.file.layout)
        LayoutTools.shared_container_formatting(layout)
        return layout
    
    def show(self):
        self.file.show()
        self.layout.update()
        return
    
    def hide(self):
        self.file.hide()
        self.layout.update()
        return

    def change_font_size(self, font_size):
        self.file.change_font_size(font_size)
        self.layout.update()
        return
    
    def update_constructed_element(self):
        text = f"{self.file.value.currentText()}"
        self.constructed_element.set_text(text)
        self.host.update_constructed_element()
        return
