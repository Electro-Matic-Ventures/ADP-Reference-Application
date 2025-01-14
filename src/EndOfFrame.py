from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from Tile import Tile


class EndOfFrame(Tile):
    
    def __init__(self, app, host):
        super().__init__()
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
        """
        return style
    
    def _label(self):
        label = QLabel()
        label.setText("Sign ID")
        label.setFixedSize(
            self.settings.label.dimensions.width,
            self.settings.label.dimensions.height
        )
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(self._label_style())
        return label
    
    def _value_style(self):
        style =  f"""
            background-color: rgb({self.settings.value.colors.static_background});
            border-bottom-left-radius: 5px;
            border-bottom-right-radius: 5px;
            color: rgb({self.settings.value.colors.static_foreground});
            font: {self.settings.value.font.size}px "{self.settings.value.font.family}";
            font-weight: {self.settings.value.font.weight};
        """
        return style

    def _value(self):
        value = QLabel()
        value.setText("\\X04")
        value.setFixedSize(
            self.settings.label.dimensions.width,
            self.settings.label.dimensions.height
        )
        value.setAlignment(Qt.AlignCenter)
        value.setStyleSheet(self._value_style())
        return value