from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import Qt
from MapPlus import MapPlus
from FormatSegment import FormatSegment
from ConstructedElement import ConstructedElement
from typing import TYPE_CHECKING
from LayoutTools import LayoutTools


if TYPE_CHECKING:
    from MainWindow import MainWindow
    from Message import Message


class FormatSegments:

    def __init__(self, app:"MainWindow", host:"Message"):
        self.app: "MainWindow" = app
        self.host: "Message" = host
        self.constructed_element: ConstructedElement = ConstructedElement()
        self.layout: QVBoxLayout = self.__make_layout()
        self.data: MapPlus = MapPlus()
        self.add()
        self.data.map[0].hide()
        return

    def add(self):
        index = self.data.add(FormatSegment(self.app, self))
        self.data.map[index].segment_index = index
        self.data.map[index].layout_index = self.layout.count()
        self.layout.addLayout(self.data.map[index].layout)
        self.layout.update()        
        return
    
    def remove(self, segment:FormatSegment):
        self.data.remove(segment.segment_index)
        taken = self.layout.takeAt(segment.layout_index)
        LayoutTools.clear_layout(taken)
        LayoutTools.recalculate_layout_indices(self.data.map, 0)
        self.layout.update()
        self.host.update_up()
        return
    
    def reset(self):
        while len(self.data.map) > 0:
            next_key = list(self.data.map.keys())[0]
            target = self.data.map[next_key]
            self.remove(target)
        self.add()
        self.data.map[0].hide()
        return
    
    def hide(self):
        for i in self.data.map:
            self.data.map[i].hide()
        self.reset()
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
        layout = QVBoxLayout()
        LayoutTools.shared_container_formatting(layout)
        return layout