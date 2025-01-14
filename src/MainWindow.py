from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QAction, QWidget, QScrollArea
from PyQt5.QtCore import Qt
from ConstructedFrame import ConstructedFrame
from Header import Header
from Messages import Messages
from CONSTANTS import FONT_SIZES
from Settings import Settings


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.setWindowTitle("ADP Message Builder")
        geo = (0,0,100,100)
        self.setGeometry(*geo)
        # self.__make_menu_bar()
        self.constructed_frame: ConstructedFrame = ConstructedFrame(self)
        self.header: Header = Header(self)
        self.messages: Messages = Messages(self)
        self.layout: QVBoxLayout = self.__make_layout()
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.scroll_area: QScrollArea = self.__make_scroll_area()
        self.setCentralWidget(self.scroll_area)
        self.update()
        self.layout.update()
        return    
    
    def __make_menu_bar(self):
        menu = self.menuBar()
        resize = menu.addMenu("Change Size")
        small = QAction("Small", self)
        medium = QAction("Medium", self)
        large = QAction("Large", self)
        resize.addAction(small)
        resize.addAction(medium)
        resize.addAction(large)
        small.triggered.connect(lambda: self.__change_font_size(FONT_SIZES._16))
        medium.triggered.connect(lambda: self.__change_font_size(FONT_SIZES._24))
        large.triggered.connect(lambda: self.__change_font_size(FONT_SIZES._36))
        return
    
    def __make_layout(self):
        layout: QVBoxLayout = QVBoxLayout()
        layout.addLayout(self.constructed_frame.layout)
        layout.addLayout(self.header.layout)
        layout.addLayout(self.messages.layout)
        layout.setContentsMargins(5,5,5,5)
        layout.setSpacing(5)
        layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        return layout
    
    def __make_scroll_area(self):
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.widget)
        scroll_area.setWidgetResizable(True)
        return scroll_area
    
    def __change_font_size(self, new_size):
        self.settings.change_font_size(new_size)
        self.header.change_font_size(new_size)
        for key in self.messages.map:
            self.messages.map[key].change_font_size(new_size)
        p = self.setttings.padding
        self.layout.setContentsMargins(5,5,5,5)
        self.layout.setSpacing(5)
        self.layout.update()
        self.widget.update()
        return
    
    def update(self):
        text = self.header.constructed_element.text
        for index in self.messages.data.map:
            if not self.messages.data.map[index].constructed_element.in_use:
                continue
            text += self.messages.data.map[index].constructed_element.text
        text += "\\X04"
        self.constructed_frame.change_text(text)
        return