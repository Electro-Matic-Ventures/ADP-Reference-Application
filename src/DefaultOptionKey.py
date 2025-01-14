from PyQt5.QtWidgets import QVBoxLayout, QLabel, QComboBox
from PyQt5.QtCore import Qt
from Tile import Tile
from CONSTANTS import SETTINGS_DEFAULTS
from typing import TYPE_CHECKING
from ConstructedElement import ConstructedElement


if TYPE_CHECKING:
    from MainWindow import MainWindow

class DefaultOptionKey(Tile):
    
    def __init__(self, app, host):
        super().__init__()
        self.app: "MainWindow" = app
        self.host = host
        self.constructed_element: ConstructedElement = self._make_constructed_element()
        self.label: QLabel = self._label()
        self.value: QComboBox = self._value()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.value)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        self.layout.setAlignment(Qt.AlignTop)
        return
    
    def _make_constructed_element(self):
        c = ConstructedElement()
        k = list(SETTINGS_DEFAULTS.keys())[0]
        s = SETTINGS_DEFAULTS[k]
        t = s["key"]
        c.set_text(t)
        return c


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
        label.setText("Default\nType")
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
        select_box = QComboBox()
        select_box.addItems(SETTINGS_DEFAULTS.keys())
        select_box.setFixedSize(
            self.settings.value.dimensions.width,
            self.settings.value.dimensions.height
        )
        select_box.setEditable(True)
        select_box.lineEdit().setAlignment(Qt.AlignCenter)
        select_box.setStyleSheet(self._value_style())
        select_box.currentIndexChanged.connect(self.__text_changed)
        return select_box
    
    def __text_changed(self):
        target = self.host.value.value
        target.clear()
        key = self.value.currentText()
        settings = SETTINGS_DEFAULTS[key]
        new_items = settings["values"]
        target.addItems(new_items.keys())
        text = settings["key"]
        self.constructed_element.set_text(text)
        self.host.update_up()
        return