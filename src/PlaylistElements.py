from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from ConstructedElement import ConstructedElement
from MapPlus import MapPlus
from PlaylistElement import PlaylistElement
from typing import TYPE_CHECKING
from LayoutTools import LayoutTools


if TYPE_CHECKING:
    from MainWindow import MainWindow
    from SignSettings import SignSettings


class PlaylistElements:

    def __init__(self, app:"MainWindow", host:"SignSettings"):
        self.app: "MainWindow" = app
        self.host: "SignSettings" = host
        self.constructed_element: ConstructedElement = ConstructedElement()
        self.data: MapPlus = MapPlus()
        self.layout = self.__make_layout()
        index = self.add()
        self.data.map[index].hide()
        return

    def add(self):
        index = self.data.add(PlaylistElement(self.app, self))
        self.data.map[index].element_index = index
        self.data.map[index].layout_index = self.layout.count()
        self.layout.addLayout(self.data.map[index].layout)
        self.data.map[index].show()
        return index
    
    def remove(self, element:PlaylistElement):
        element.hide()
        self.data.remove(element.element_index)
        taken = self.layout.takeAt(element.layout_index)
        LayoutTools.clear_layout(taken)
        LayoutTools.recalculate_layout_indices(self.data.map, 0)
        self.layout.update()
        self.update_up()
        return
    
    def update_up(self):
        text = self.__update_text()
        self.constructed_element.set_text(text)
        self.host.update_up()
        return
    
    def __update_text(self):
        text = ""
        for i in self.data.map:
            text += self.data.map[i].constructed_element.text
        return text
    
    def show(self):
        for i in self.data.map:
            self.data.map[i].show()
        return
    
    def hide(self):
        for i in self.data.map:
            self.data.map[i].hide()
        self.reset()
        return
    
    def reset(self):
        while len(self.data.map) > 0:
            next_key = list(self.data.map.keys())[0]
            target = self.data.map[next_key]
            self.remove(target)
        self.add()
        self.data.map[0].hide()
        return
    
    def __make_layout(self):
        layout = QHBoxLayout()
        for i in self.data.map:
            layout.addLayout(self.data.map[i].layout)
        LayoutTools.shared_container_formatting(layout)
        return layout