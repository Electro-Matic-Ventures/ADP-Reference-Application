from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from typing import TYPE_CHECKING
from ConstructedElement import ConstructedElement
from AddressMode import AddressMode
from BasicAddressing import BasicAddressing
from AdvancedAddressing import AdvancedAddressing
from LayoutTools import LayoutTools


if TYPE_CHECKING:
    from MainWindow import MainWindow

class Addressing:

    def __init__(self, app: "MainWindow", host):
        self.app: "MainWindow" = app
        self.host = host
        self.constructed_element: ConstructedElement = ConstructedElement()
        self.address_mode: AddressMode = AddressMode(self.app, self)
        self.advanced_addressing: AdvancedAddressing = AdvancedAddressing(self.app, self)
        self.basic_addressing: BasicAddressing = BasicAddressing(self.app, self)
        self.layout: QHBoxLayout = self.__make_layout()
        return 
    
    def change_font_size(self, new_size):
        self.address_mode.change_font_size(new_size)
        self.basic_addressing.change_font_size(new_size)
        self.advanced_addressing.change_font_size(new_size)
        self.layout.update()
        return
    
    def show(self):
        self.address_mode.show()
        self.basic_addressing.show()
        self.basic_addressing.update_constructed_element()
        self.advanced_addressing.hide()
        self.layout.update()
        return
    
    def hide(self):
        self.address_mode.hide()
        self.basic_addressing.hide()
        self.advanced_addressing.hide()
        self.layout.update()
        return
    
    def select_address_layout(self):
        text = self.address_mode.value.currentText()
        if text == "basic":
            self._basic_address_mode()
            return
        if text == "advanced":
            self._advanced_address_mode()
            return
        return
    
    def _basic_address_mode(self):
        self.basic_addressing.update_constructed_element()
        self.address_mode.show()
        self.basic_addressing.show()
        self.advanced_addressing.hide()
        self.layout.update()
        return
    
    def _advanced_address_mode(self):
        self.advanced_addressing.update_constructed_element()
        self.address_mode.show()
        self.basic_addressing.hide()
        self.advanced_addressing.show()
        self.layout.update()
        return
    
    def update_constructed_element(self):
        mode = self.address_mode.value.currentText()
        if mode == "basic":
            text = self.basic_addressing.constructed_element.text
        if mode == "advanced":
            text = self.advanced_addressing.constructed_element.text
        self.constructed_element.set_text(text)
        self.host.update_up()
        return
    
    def __make_layout(self):
        layout = QHBoxLayout()
        layout.addLayout(self.address_mode.layout)
        layout.addLayout(self.basic_addressing.layout)
        layout.addLayout(self.advanced_addressing.layout)
        LayoutTools.shared_container_formatting(layout)
        return layout