from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from ConstructedElement import ConstructedElement
from MapPlus import MapPlus
from SegmentElement import SegmentElement
from typing import TYPE_CHECKING
from LayoutTools import LayoutTools


if TYPE_CHECKING:
    from MainWindow import MainWindow
    from FormatSegment import FormatSegment


class SegmentElements:

    def __init__(self, app:"MainWindow", host:"FormatSegment"):
        self.app: "MainWindow" = app
        self.host: "FormatSegment" = host
        self.constructed_element: ConstructedElement = ConstructedElement()
        self.data: MapPlus = MapPlus()
        self.layout: QHBoxLayout = self.__make_layout()
        self.layout_index: int = -1
        self.element_index: int = -1
        return
    
    def add(self):
        index = self.data.add_max(SegmentElement(self.app, self))
        self.data.map[index].element_index = index
        self.data.map[index].show()
        self.layout.addLayout(self.data.map[index].layout)
        return index

    def remove(self, element:SegmentElement):
        LayoutTools.clear_layout(element.layout)
        del self.data.map[element.element_index]
        self.layout.update()
        self.update_up()
        return
    
    def remove_to_right(self, element_index:int):
        keys = list(self.data.map.keys())
        remove = [x for x in keys if x > element_index]
        for i in remove:
            target = self.data.map[i]
            target.hide()
            self.remove(target)
        self.layout.update()
        return
        
    def hide(self):
        for i in self.data.map:
            self.data.map[i].hide()
        return
    
    def show(self):
        for i in self.data.map:
            self.data.map[i].show()
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
    
    def __make_layout(self):
        layout = QHBoxLayout()
        LayoutTools.shared_container_formatting(layout)
        return layout