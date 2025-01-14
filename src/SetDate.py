from PyQt5.QtWidgets import QVBoxLayout, QLabel, QDateEdit
from PyQt5.QtCore import Qt, QDate
from typing import TYPE_CHECKING
from Tile import Tile
from ConstructedElement import ConstructedElement
from LayoutTools import LayoutTools


if TYPE_CHECKING:
    from MainWindow import MainWindow
    from SignSettings import SignSettings


class SetDate(Tile):

    def __init__(self, app: "MainWindow", host: "SignSettings"):
        super().__init__()
        self.app: "MainWindow" = app
        self.host: "SignSettings" = host
        self.label = self._label()
        self.value = self._value()
        self.layout = self.__make_layout()
        self.constructed_element: ConstructedElement = ConstructedElement()
        self.constructed_element.set_text(self.__get_date_string())
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
        label.setText("Set\nDate")
        label.setFixedSize(
            self.settings.label.dimensions.width, 
            self.settings.label.dimensions.height
        )
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(self._label_style())
        return label
    
    def _value_style(self):
        style =  f"""
            QDateEdit {{
                background-color: rgb({self.settings.value.colors.selector_background});
                border: 2px solid rgb(0,0,0);
                border-bottom-left-radius: 5px;
                border-bottom-right-radius: 5px;
                color: rgb({self.settings.value.colors.selector_foreground});
                font: {self.settings.value.font.size}px "{self.settings.value.font.family}";
                font-weight: {self.settings.value.font.weight};
                padding: 5px;
            }}
            QDateEdit::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 25px;
                border-left: 1px solid rgb(0,0,0);
                border-bottom-right-radius: 5px;
                padding: 5px;
            }}
            QDateEdit::down-arrow {{
                image: url("./src/graphics/caret-down-{self.settings.value.caret.size}.png"); 
                width: 23px;
                height: 17px;
            }}
        """
        return style

    def _value(self):
        control = QDateEdit()
        control.setCalendarPopup(True)
        control.setDate(QDate.currentDate())
        control.setFixedSize(
            self.settings.value.dimensions.width,
            self.settings.value.dimensions.height
        )
        control.setStyleSheet(self._value_style())
        control.dateChanged.connect(self.__changed)
        return control
    
    def __changed(self):
        self.constructed_element.set_text(self.__get_date_string())
        self.host.update_up()
        return
    
    def __get_date_string(self):
        date = self.value.date()
        year = f"{date.year()}"[-2:]
        month = f"{date.month():02}"
        day = f"{date.day():02}"
        date = f"{month}{day}{year}"
        return date
    
    def __make_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.value)
        LayoutTools.shared_control_formatting(layout)
        return layout