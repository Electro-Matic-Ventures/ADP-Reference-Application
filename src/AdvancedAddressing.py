from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from typing import TYPE_CHECKING
from ConstructedElement import ConstructedElement
from Drive import Drive
from Folder import Folder
from File import File
from LayoutTools import LayoutTools


if TYPE_CHECKING:
    from MainWindow import MainWindow
    from Addressing import Addressing


class AdvancedAddressing:
    
    """
    properties:\n
    \tapp: MainWindow
    \tconstructed: ConstructedElement
    \tdrive: Drive
    \tfile_0: File
    \tfile_1: File
    \tfolder: Folder
    \thost: Addressing
    \tlayout: QHBoxLayout
    """

    def __init__(self, app: "MainWindow", host: "Addressing"):
        self.app: "MainWindow" = app
        self.host: "Addressing" = host
        self.constructed_element: ConstructedElement = ConstructedElement()
        self.drive: Drive = Drive(self.app, self)
        self.file_0: File = File(self.app, self)
        self.file_1: File = File(self.app, self)
        self.folder: Folder = Folder(self.app, self)
        self.layout: QHBoxLayout = self.__make_layout()
        return
    
    def __make_layout(self):
        layout = QHBoxLayout()
        layout.addLayout(self.drive.layout)
        layout.addLayout(self.folder.layout)
        layout.addLayout(self.file_0.layout)
        layout.addLayout(self.file_1.layout)
        LayoutTools.shared_container_formatting(layout)
        return layout
    
    def show(self):
        self.drive.show()
        self.folder.show()
        self.file_0.show()
        self.file_1.show()
        self.redraw()
        return
    
    def hide(self):
        self.drive.hide()
        self.folder.hide()
        self.file_0.hide()
        self.file_1.hide()
        self.redraw()
        return
    
    def redraw(self):
        self.layout.update()
        return

    def change_font_size(self, font_size):
        return
    
    def update_constructed_element(self):
        text = "\\X0F"
        text += self.drive.value.currentText()
        text += self.folder.value.currentText()
        text += self.file_0.value.currentText()
        text += self.file_1.value.currentText()
        self.constructed_element.set_text(text)
        self.host.update_constructed_element()
        return