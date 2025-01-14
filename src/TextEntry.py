from PyQt5.QtWidgets import QVBoxLayout, QLabel, QTextEdit, QSizePolicy
from PyQt5.QtCore import Qt
from ConstructedElement import ConstructedElement
from Tile import Tile
from typing import TYPE_CHECKING
from LayoutTools import LayoutTools


if TYPE_CHECKING:
    from MainWindow import MainWindow
    from SegmentElement import SegmentElement

class TextEntry(Tile):
    
    def __init__(self, app:"MainWindow", host:"SegmentElement"):
        super().__init__()
        self.app: "MainWindow" = app
        self.host: "SegmentElement" = host
        self.label = self._label()
        self.value = self._value()
        self.layout = self.__make_layout()
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
        label.hide()
        label.setText("Segment\nText")
        self.settings.label.dimensions.width *= 2
        self.settings.label.dimensions.width += self.app.settings.padding
        label.setFixedSize(
            self.settings.label.dimensions.width, 
            self.settings.label.dimensions.height
        )
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(self._label_style())
        return label
    
    def _value_style(self):
        style =  f"""
        QTextEdit {{
            background-color: rgb({self.settings.value.colors.selector_background});
            border: 2px solid rgb(0,0,0);
            border-bottom-left-radius: 5px;
            border-bottom-right-radius: 5px;
            color: rgb({self.settings.value.colors.selector_foreground});
            font: {self.settings.value.font.size}px "{self.settings.value.font.family}";
            font-weight: {self.settings.value.font.weight};
            padding: 5px;
        }}
        QTextEdit QScrollBar:vertical {{
            width: 0px;
        }}
        """
        return style

    def _value(self):
        text = QTextEdit()
        text.hide()
        self.settings.value.dimensions.width *= 2
        self.settings.value.dimensions.width += self.app.settings.padding
        text.setFixedSize(
            self.settings.value.dimensions.width, 
            self.settings.value.dimensions.height
        )
        text.setSizePolicy(
            QSizePolicy.Fixed,
            QSizePolicy.Fixed
        )
        text.setAlignment(Qt.AlignLeft)
        text.setStyleSheet(self._value_style())
        text.textChanged.connect(self.__text_changed)
        return text
    
    def __text_changed(self):
        self.host.update_up()
        return
    
    def __make_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.value)
        LayoutTools.shared_control_formatting(layout)
        return layout