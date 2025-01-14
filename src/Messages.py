from typing import TYPE_CHECKING
from MapPlus import MapPlus
from PyQt5.QtWidgets import QVBoxLayout
from Message import Message
from LayoutTools import LayoutTools


if TYPE_CHECKING:
    from MainWindow import MainWindow
    

class Messages:
    
    def __init__(self, app):
        self.app: "MainWindow" = app
        self.data: MapPlus = MapPlus()
        self.layout: QVBoxLayout = self.__make_layout()
        self.add()
        return
    
    def add(self):
        index = self.data.add(Message(self.app, self))
        self.data.map[index].message_index = index
        self.data.map[index].layout_index = self.layout.count()
        self.layout.addLayout(self.data.map[index].layout)
        self.layout.update()
        return
    
    def remove(self, message:Message):
        message.hide()
        self.data.remove(message.message_index)
        taken = self.layout.takeAt(message.layout_index)
        LayoutTools.clear_layout(taken)
        LayoutTools.recalculate_layout_indices(self.data.map, 0)
        self.layout.update()
        self.app.update()
        return
    
    def __make_layout(self):
        layout = QVBoxLayout()
        LayoutTools.shared_container_formatting(layout)
        return layout        