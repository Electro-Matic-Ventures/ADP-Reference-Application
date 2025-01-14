from PyQt5.QtWidgets import QVBoxLayout, QLabel, QComboBox
from PyQt5.QtCore import Qt
from typing import TYPE_CHECKING
from Tile import Tile
from CONSTANTS import ELEMENT_MODES
from LayoutTools import LayoutTools


if TYPE_CHECKING:
    from MainWindow import MainWindow
    from SegmentElement import SegmentElement


class ElementMode(Tile):

    def __init__(self, app: "MainWindow", host: "SegmentElement"):
        super().__init__()
        self.app: "MainWindow" = app
        self.host: "SegmentElement" = host
        self.label: QLabel = self._label()
        self.value: QComboBox = self._value()
        self.layout: QVBoxLayout = self.__make_layout()
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
        label.setText("Element\nMode")
        label.setFixedSize(
            self.settings.label.dimensions.width, 
            self.settings.label.dimensions.height
        )
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(self._label_style())
        return label
    
    def _value_style(self):
        style =  f"""
            QComboBox {{
                background-color: rgb({self.settings.value.colors.selector_background});
                border: 2px solid rgb(0,0,0);
                border-bottom-left-radius: 5px;
                border-bottom-right-radius: 5px;
                color: rgb({self.settings.value.colors.selector_foreground});
                font: {self.settings.value.font.size}px "{self.settings.value.font.family}";
                font-weight: {self.settings.value.font.weight};
                padding: 5px;
            }}
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: {self.settings.value.font.size}px;
                border-left: 1px solid rgb(0,0,0);
                border-bottom-right-radius: 5px;
                padding-left: {self.settings.value.caret.padding}px;
                padding-right: {self.settings.value.caret.padding}px;
            }}
            QComboBox::down-arrow {{
                image: url("./src/graphics/caret-down-{self.settings.value.caret.size}.png");
            }}
        """
        return style

    def _value(self):
        box = QComboBox()
        box.hide()
        box.addItems(self.__determine_items())
        box.setCurrentText("format")
        box.setFixedSize(
            self.settings.value.dimensions.width, 
            self.settings.value.dimensions.height
        )
        box.setEditable(True)
        box.lineEdit().setAlignment(Qt.AlignCenter)
        box.setStyleSheet(self._value_style())
        box.currentIndexChanged.connect(self.host.mode_select)
        return box
    
    def __determine_items(self):
        keys = list(self.host.host.data.map.keys())
        if len(keys) == 0:
            return ELEMENT_MODES
        left = self.host.host.data.map[keys[-1]]
        mode = left.mode.value.currentText()
        if mode == "text":
            return [ELEMENT_MODES[-1]]
        if mode == "format":
            return ELEMENT_MODES
        return ["invalid mode"]
    
    def __make_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.value)
        LayoutTools.shared_control_formatting(layout)
        return layout