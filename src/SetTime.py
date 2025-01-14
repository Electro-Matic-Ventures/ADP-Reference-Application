from PyQt5.QtWidgets import QVBoxLayout, QLabel, QTimeEdit
from PyQt5.QtCore import Qt, QTime
from typing import TYPE_CHECKING
from Tile import Tile
from ConstructedElement import ConstructedElement
from LayoutTools import LayoutTools


if TYPE_CHECKING:
    from MainWindow import MainWindow
    from SignSettings import SignSettings


class SetTime(Tile):

    def __init__(self, app:"MainWindow", host:"SignSettings"):
        super().__init__()
        self.app: "MainWindow" = app
        self.host: "SignSettings" = host
        self.constructed_element: ConstructedElement = ConstructedElement()
        self.label: QLabel = self._label()
        self.value: QTimeEdit = self._value()
        self.constructed_element.set_text(self.__get_time_as_string())
        self.layout: QVBoxLayout = self.__make_layout()
        self.hide()
        return
    
    def _label_style(self):
        style =  f"""
            background-color: rgb({self.settings.label.colors.background});
            border-top-left-radius: 5px;
            border-top-right-radius: 5px;
            color: rgb({self.settings.label.colors.foreground});
            font: {self.settings.label.font.size}px "{self.settings.label.font.family}";
            font-weight: {self.settings.label.font.weight};
            padding: 5px;
        """
        return style
    
    def _label(self):
        label = QLabel()
        label.setText("Set\nTime")
        label.setFixedSize(
            self.settings.label.dimensions.width, 
            self.settings.label.dimensions.height
        )
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(self._label_style())
        return label
    
    def _value_style(self):
        style =  f"""
            QTimeEdit {{
                background-color: rgb({self.settings.value.colors.selector_background});
                border: 2px solid rgb(0,0,0);
                border-bottom-left-radius: 5px;
                border-bottom-right-radius: 5px;
                color: rgb({self.settings.value.colors.selector_foreground});
                font: {self.settings.value.font.size}px "{self.settings.value.font.family}";
                font-weight: {self.settings.value.font.weight};
                padding: 5px;
            }}
        """
        return style

    def _value(self):
        c = QTimeEdit()
        c.setTime(QTime.currentTime())
        c.setFixedSize(
            self.settings.value.dimensions.width,
            self.settings.value.dimensions.height
        )
        c.setStyleSheet(self._value_style())
        c.timeChanged.connect(self.__changed)
        return c
    
    def __changed(self):
        time = self.__get_time_as_string()
        self.constructed_element.set_text(time)
        self.host.update_up()
        return
    
    def __get_time_as_string(self):
        time = self.value.time()
        hours = f"{time.hour():02}"
        minutes = f"{time.minute():02}"
        seconds = f"{time.second():02}"
        time = f"{hours}{minutes}{seconds}"
        return time
    
    def __make_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.value)
        LayoutTools.shared_control_formatting(layout)
        return layout