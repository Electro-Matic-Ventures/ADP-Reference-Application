from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from AddElement import AddElement
from ElementMode import ElementMode
from ElementOptionType import ElementOptionType
from ElementOptionValue import ElementOptionValue
from TextEntry import TextEntry
from ConstructedElement import ConstructedElement
from LineFeed import LineFeed
from typing import TYPE_CHECKING
from CONSTANTS import OPTION_CODES
from LayoutTools import LayoutTools


if TYPE_CHECKING:
    from MainWindow import MainWindow
    from SegmentElements import SegmentElements


class SegmentElement:

    def __init__(self, app:"MainWindow", host:"SegmentElements"):
        self.app: "MainWindow" = app
        self.host: "SegmentElements" = host
        self.constructed_element: ConstructedElement = ConstructedElement()
        self.element_index: int = -1
        self.layout_index: int = -1
        self.add_: AddElement = AddElement(app, self)
        # self.remove_: RemoveElement= RemoveElement(app, self)
        self.mode: ElementMode = ElementMode(app, self)
        self.type: ElementOptionType = ElementOptionType(app, self, "font")
        self.value: ElementOptionValue = ElementOptionValue(app, self, "font")
        self.text: TextEntry = TextEntry(app, self)
        self.line_feed: LineFeed = LineFeed(app, self)
        self.layout = self.__make_layout()
        return
    
    def add(self):
        mode = self.mode.value.currentText()
        if mode == "line_feed":
            self.__line_feed_mode()
            return
        self.__option_mode()
        self.update_up()
        self.host.add()
        return
    
    def remove(self):
        return
    
    def show(self):
        self.add_.show()
        self.mode.hide()
        self.type.hide()
        self.value.hide()
        self.text.hide()
        self.line_feed.hide()
        self.layout.update()
        return
    
    def hide(self):
        self.add_.hide()
        self.mode.hide()
        self.type.hide()
        self.value.hide()
        self.text.hide()
        self.line_feed.hide()
        self.layout.update()
        return
    
    def mode_select(self):
        mode = self.mode.value.currentText()
        if mode == "remove":
            return
        if mode == "format":
            self.__option_mode()
            return
        if mode == "text":
            self.__text_mode()
            return
        if mode == "line_feed":
            self.__line_feed_mode()
            return
        return

    def __option_mode(self):
        self.add_.hide()
        self.mode.show()
        self.type.show()
        self.value.show()
        self.text.hide()
        self.line_feed.hide()
        self.layout.update()
        self.update_up()
        return
    
    def __text_mode(self):
        self.add_.hide()
        self.mode.show()
        self.type.hide()
        self.value.hide()
        self.text.show()
        self.line_feed.hide()
        self.layout.update()
        self.update_up()
        self.host.remove_to_right(self.element_index)
        self.host.add()
        return
    
    def __line_feed_mode(self):
        self.add_.hide()
        self.mode.show()
        self.type.hide()
        self.value.hide()
        self.text.hide()
        self.line_feed.show()
        self.layout.update()
        self.host.remove_to_right(self.element_index)
        self.update_up()
        return
    
    def update_up(self):
        text = self.__update_text()
        self.constructed_element.set_text(text)
        self.host.update_up()
        return
    
    def __update_text(self):
        text = ""
        mode = self.mode.value.currentText()
        if mode == "remove":
            text = self.__get_mode_remove_text()
            return text
        if mode == "format":
            text = self.__update_mode_format()
            return text
        if mode == "text":
            text = self.__update_mode_text()
            return text
        if mode == "line_feed":
            text = self.__update_mode_line_feed()
            return text
        return text
    
    def __get_mode_remove_text(self):
        text = ""
        return text
    
    def __update_mode_format(self):
        type = self.type.value.currentText()
        value = self.value.value.currentText()
        text = ""
        if value == "":
            return text
        if type != "scroll_speed":
            text += OPTION_CODES[type]["key"]
        text += OPTION_CODES[type]["values"][value]
        return text
    
    def __update_mode_text(self):
        text = self.text.value.toPlainText()
        return text
    
    def __update_mode_line_feed(self):
        text = "\\X0D"
        return text
    
    def __make_layout(self):
        layout = QHBoxLayout()
        layout.addLayout(self.add_.layout)
        layout.addLayout(self.mode.layout)
        layout.addLayout(self.type.layout)
        layout.addLayout(self.value.layout)
        layout.addLayout(self.text.layout)
        layout.addLayout(self.line_feed.layout)
        LayoutTools.shared_container_formatting(layout)
        return layout