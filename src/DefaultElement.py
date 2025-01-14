from typing import TYPE_CHECKING
from ConstructedElement import ConstructedElement
from AddDefaultElement import AddDefaultElement
from RemoveDefaultElement import RemoveDefaultElement
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from DefaultOptionKey import DefaultOptionKey
from DefaultOptionValue import DefaultOptionValue
from LayoutTools import LayoutTools


if TYPE_CHECKING:
    from MainWindow import MainWindow
    from SignSettings import SignSettings


class DefaultElement:

    def __init__(self, app:"MainWindow", host:"SignSettings"):
        self.app: "MainWindow" = app
        self.host: "SignSettings" = host
        self.constructed_element: ConstructedElement = ConstructedElement()
        self.element_index = -1
        self.layout_index = -1
        self.add_: AddDefaultElement = AddDefaultElement(app, self)
        self.remove_: RemoveDefaultElement = RemoveDefaultElement(app, self)
        self.key: DefaultOptionKey = DefaultOptionKey(app, self)
        self.value: DefaultOptionValue = DefaultOptionValue(app, self)
        self.layout: QHBoxLayout = self.__make_layout()
        self.hide()
        return
    
    def __make_layout(self):
        layout = QHBoxLayout()
        layout.addLayout(self.add_.layout)
        layout.addLayout(self.remove_.layout)
        layout.addLayout(self.key.layout)
        layout.addLayout(self.value.layout)
        LayoutTools.shared_container_formatting(layout)
        return layout

    
    def hide(self):
        self.add_.hide()
        self.remove_.hide()
        self.key.hide()
        self.value.hide()
        self.layout.update()
        self.constructed_element.reset()
        return
    
    def show(self):
        self.add_.show()
        self.remove_.hide()
        self.key.hide()
        self.value.hide()
        self.layout.update()
        self.constructed_element.reset()
        return
    
    def add(self):
        self.add_.hide()
        self.remove_.show()
        self.key.show()
        self.value.show()
        self.update_up()
        self.host.add()
        return
    
    def remove(self):
        self.hide()
        self.layout.update()
        self.host.remove(self)
        return
    
    def update_up(self):
        self.__update_constructed_element()
        self.host.update_up()
        return
    
    def __update_constructed_element(self):
        text = self.key.constructed_element.text
        text += self.value.constructed_element.text
        self.constructed_element.set_text(text)
        return
