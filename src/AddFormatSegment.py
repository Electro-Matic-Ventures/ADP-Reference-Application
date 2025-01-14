from PyQt5.QtWidgets import QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from typing import TYPE_CHECKING
from Button import Button
from LayoutTools import LayoutTools


if TYPE_CHECKING:
    from MainWindow import MainWindow
    from FormatSegment import FormatSegment


class AddFormatSegment(Button):

    def __init__(self, app: "MainWindow", host: "FormatSegment"):
        super().__init__()
        self.app: "MainWindow" = app
        self.host: "FormatSegment" = host
        self.button: QPushButton = self.__make_button()
        self.layout: QVBoxLayout = self.__make_layout()
        return

    def _button_style(self):
        style =  f"""
            background-color: rgb({self.settings.colors.background});
            border-radius: 5px;
            color: rgb({self.settings.colors.foreground});
            font: {self.settings.font.size}px "{self.settings.font.family}";
            font-weight: {self.settings.font.weight};
            padding: 5px;
        """
        return style
    
    def __make_button(self):
        button = QPushButton()
        button.setText("Add Format\nSegment")
        button.setFixedSize(
            self.settings.dimensions.width, 
            self.settings.dimensions.height
        )
        button.setStyleSheet(self._button_style())
        button.mousePressEvent = self.__pressed
        button.mouseReleaseEvent = self.__released
        return button
    
    def __pressed(self, event):
        if event.button() == Qt.LeftButton:
            self.__pressed_left(event)
            return
        if event.button() == Qt.RightButton:
            self.__pressed_right(event)
            return
        return
    
    def __pressed_left(self, event):
        self._darken()
        self.redraw()
        return
    
    def __pressed_right(self, event):
        # intentionally blank 2024/11/13
        return
    
    def __released(self, event):
        if event.button() == Qt.LeftButton:
            self.__released_left(event)
            return
        if event.button() == Qt.RightButton:
            self.__released_right(event)
            return
        return
    
    def __released_left(self, event):
        # from Message import Message
        self._reset_color()
        self.redraw()
        self.host.add()
        return
    
    def __released_right(self, event):
        # intentionally blank 2024/11/13
        return
    
    def __make_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        LayoutTools.shared_control_formatting(layout)
        return layout