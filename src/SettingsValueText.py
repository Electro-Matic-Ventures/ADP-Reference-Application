from PyQt5.QtWidgets import QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import Qt
from Tile import Tile


class SettingsValueText(Tile):

    def __init__(self, app, host):
        super().__init__(app, host)
        self.label = self._label()
        self.value = self._value()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.value)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
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
        label.setText("Setting\Value")
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
                width: 25px;
                border-left: 1px solid rgb(0,0,0);
                border-bottom-right-radius: 5px;
                padding: 5px;
            }}
            QComboBox::down-arrow {{
                image: url("./src/graphics/caret-down-{self.settings.value.caret.size}.png"); 
                width: 23px;
                height: 17px;
            }}
        """
        return style

    def _value(self):
        select_box = QLineEdit()
        select_box.setFixedSize(
            self.settings.value.dimensions.width,
            self.settings.value.dimensions.height
        )
        select_box.setEditable(True)
        select_box.lineEdit().setAlignment(Qt.AlignCenter)
        select_box.setStyleSheet(self._value_style())
        return select_box