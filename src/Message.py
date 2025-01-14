from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from typing import TYPE_CHECKING
from ConstructedElement import ConstructedElement
from AddMessage import AddMessage
from RemoveMessage import RemoveMessage
from MessageMode import MessageMode
from SignSettings import SignSettings
from Addressing import Addressing
from FormatSegments import FormatSegments
from LayoutTools import LayoutTools

if TYPE_CHECKING:
    from MainWindow import MainWindow
    from Messages import Messages


class Message:

    def __init__(self, app:"MainWindow", host:"Messages"):
        self.app: "MainWindow" = app
        self.host: "Messages" = host
        self.constructed_element: ConstructedElement = ConstructedElement()
        self.add_: AddMessage = AddMessage(self.app, self)
        self.remove_: RemoveMessage = RemoveMessage(self.app, self)
        self.mode: MessageMode = MessageMode(self.app, self)
        self.addressing: Addressing = Addressing(self.app, self)
        self.format_segments: FormatSegments = FormatSegments(app, self)
        self.sign_settings: SignSettings = SignSettings(self.app, self)
        self.layout_index: int = -1
        self.message_index: int = -1
        self.layout: QHBoxLayout = self.__make_layout()

        return
    
    def __make_layout(self):
        layout = QHBoxLayout()
        layout.addLayout(self.add_.layout)
        layout.addLayout(self.remove_.layout)
        layout.addLayout(self.mode.layout)
        layout.addLayout(self.addressing.layout)
        layout.addLayout(self.format_segments.layout)
        layout.addLayout(self.sign_settings.layout)
        LayoutTools.shared_container_formatting(layout)
        return layout
        
    def change_font_size(self, font_size):
        self.add_.change_font_size(font_size)
        self.remove_.change_font_size(font_size)
        self.mode.change_font_size(font_size)
        self.sign_settings.change_font_size(font_size)
        self.addressing.change_font_size(font_size)
        return
    
    def hide(self):
        self.add_.hide()
        self.remove_.hide()
        self.mode.hide()
        self.addressing.hide()
        self.format_segments.hide()
        self.sign_settings.hide()
        self.layout.update()
        return
    
    def show(self):
        self.add_.show()
        self.remove_.hide()
        self.mode.hide()
        self.addressing.hide()
        self.format_segments.hide()
        self.sign_settings.hide()
        self.layout.update()
        return

    def add(self):
        self.add_.hide()
        self.remove_.show()
        self.mode.show()
        self.addressing.show()
        self.format_segments.show()
        self.sign_settings.hide()
        self.host.add()
        self.layout.update()
        return
    
    def remove(self):        
        self.add_.hide()
        self.remove_.hide()
        self.mode.hide()
        self.addressing.hide()
        self.format_segments.hide()
        self.sign_settings.hide()
        self.host.remove(self)
        self.layout.update()
        return
    
    def settings_mode(self):
        self.sign_settings.setting_mode.value.setCurrentIndex(0)
        self.add_.hide()
        self.remove_.show()
        self.mode.show()
        self.addressing.hide()
        self.format_segments.hide()
        self.sign_settings.show()
        self.layout.update()
        self.update_up()
        return
    
    def content_or_variable_mode(self):
        self.addressing.address_mode.value.setCurrentIndex(0)
        self.add_.hide()
        self.remove_.show()
        self.mode.show()
        self.addressing.show()
        self.format_segments.show()
        self.sign_settings.hide()
        self.layout.update()
        self.update_up()
        return
    
    def mode_select(self)-> None:
        """
            switches message control mode for message
        """
        mode = self.mode.value.currentText()
        if mode == "content":
            self.content_or_variable_mode()
            return
        if mode == "settings":
            self.settings_mode()
            return
        if mode == "variable":
            self.content_or_variable_mode()
            return
        return

    def update_up(self):
        text = self.__update_text()
        self.constructed_element.set_text(text)
        self.app.update()
        return
    
    def __update_text(self):
        text = f"\\X02"
        mode = self.mode.value.currentText()
        if mode == "content":
            text += self.__get_content_text()
        if mode == "settings":
            text += self.__get_settings_text()
        if mode == "variable":
            text += self.__get_variable_text()
        return text
    
    def __get_content_text(self):
        text = "A"
        text += self.addressing.constructed_element.text
        for i in self.format_segments.data.map:
            text += self.format_segments.data.map[i].constructed_element.text
        return text
    
    def __get_settings_text(self):
        text = "E"
        text += self.sign_settings.constructed_element.text
        return text
    
    def __get_variable_text(self):
        text = "G"
        text += self.addressing.constructed_element.text
        for i in self.format_segments.data.map:
            text += self.format_segments.data.map[i].constructed_element.text
        return text