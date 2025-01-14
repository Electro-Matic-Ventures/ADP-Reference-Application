from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from typing import TYPE_CHECKING
from AddFormatSegment import AddFormatSegment
from RemoveFormatSegment import RemoveFormatSegment
from SegmentElements import SegmentElements
from ConstructedElement import ConstructedElement
from LayoutTools import LayoutTools


if TYPE_CHECKING:
    from MainWindow import MainWindow
    from FormatSegments import FormatSegments


class FormatSegment:

    def __init__(self, app:"MainWindow", host:"FormatSegments"):
        self.app: "MainWindow" = app
        self.host: "FormatSegments" = host
        self.constructed_element: ConstructedElement = ConstructedElement()
        self.add_: AddFormatSegment = AddFormatSegment(app, self)
        self.remove_: RemoveFormatSegment = RemoveFormatSegment(app, self)
        self.segment_elements: SegmentElements = SegmentElements(app, self)
        self.layout_index: int = -1
        self.segment_index: int = -1
        self.layout = self.__make_layout()
        return
    
    def show(self):
        self.add_.show()
        self.remove_.hide()
        self.segment_elements.hide()
        self.layout.update()
        return
    
    def hide(self):
        self.add_.hide()
        self.remove_.hide()
        self.segment_elements.hide()
        self.layout.update()
        return
    
    def add(self):
        self.add_.hide()
        self.remove_.show()
        self.segment_elements.add()
        self.layout.update()
        self.host.add()
        return 
    
    def remove(self):      
        self.add_.show()
        self.remove_.hide()  
        self.segment_elements.hide()
        self.host.remove(self)
        return
    
    def redraw(self):
        self.layout.update()
        return
    
    def update_up(self):
        text = self.__update_text()
        self.constructed_element.set_text(text)
        self.host.update_up()
        return
    
    def __update_text(self):
        text = ""
        for i in self.segment_elements.data.map:
            text += self.segment_elements.data.map[i].constructed_element.text
        return text 
    
    def __make_layout(self):
        layout = QHBoxLayout()
        layout.addLayout(self.add_.layout)
        layout.addLayout(self.remove_.layout)
        layout.addLayout(self.segment_elements.layout)
        LayoutTools.shared_container_formatting(layout)
        return layout  