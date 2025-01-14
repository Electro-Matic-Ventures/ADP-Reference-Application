from typing import TYPE_CHECKING
from ConstructedElement import ConstructedElement
from AddPlaylistElement import AddPlaylistElement
from RemovePlaylistElement import RemovePlaylistElement
from Addressing import Addressing
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from LayoutTools import LayoutTools

if TYPE_CHECKING:
    from MainWindow import MainWindow
    from SignSettings import SignSettings


class PlaylistElement:

    def __init__(self, app:"MainWindow", host:"SignSettings"):
        self.app: "MainWindow" = app
        self.host: "SignSettings" = host
        self.constructed_element: ConstructedElement = ConstructedElement()
        self.element_index: int = -1
        self.layout_index: int = -1
        self.add_: AddPlaylistElement = AddPlaylistElement(app, self)
        self.remove_: RemovePlaylistElement = RemovePlaylistElement(app, self)
        self.addressing: Addressing = Addressing(app, self)
        self.layout: QHBoxLayout = self.__make_layout()
        self.hide()
        return
    
    def __make_layout(self):
        layout = QHBoxLayout()
        layout.addLayout(self.add_.layout)
        layout.addLayout(self.remove_.layout)
        layout.addLayout(self.addressing.layout)
        LayoutTools.shared_container_formatting(layout)
        return layout

    
    def hide(self):
        self.add_.hide()
        self.remove_.hide()
        self.addressing.hide()
        self.layout.update()
        self.constructed_element.reset()
        return
    
    def show(self):
        self.add_.show()
        self.remove_.hide()
        self.addressing.hide()
        self.layout.update()
        self.constructed_element.reset()
        return
    
    def add(self):
        self.add_.hide()
        self.remove_.show()
        self.addressing.show()
        self.update_up()
        self.host.add()
        return
    
    def remove(self):
        self.hide
        self.host.remove(self)
        return
    
    def update_up(self):
        self.__update_constructed_element()
        self.host.update_up()
        return
    
    def __update_constructed_element(self):
        text = self.addressing.constructed_element.text
        self.constructed_element.set_text(text)
        return
