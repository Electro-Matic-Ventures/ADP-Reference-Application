from PyQt5.QtWidgets import QHBoxLayout
from typing import TYPE_CHECKING
from ConstructedElement import ConstructedElement
from AddressPreFiller import AddressPreFiller
from GroupID import GroupID
from SignID import SignID
from LayoutTools import LayoutTools


if TYPE_CHECKING:
    from MainWindow import MainWindow


class Header:

    def __init__(self, app: "MainWindow"):
        self.app: "MainWindow" = app
        self.constructed_element: ConstructedElement = ConstructedElement()
        self.address_pre_filler: AddressPreFiller = AddressPreFiller(self.app, self)
        self.group_id: GroupID = GroupID(self.app, self)
        self.sign_id: SignID = SignID(self.app, self)
        self.layout: QHBoxLayout = self.__make_layout()
        self.update_down()
        return 
    
    def redraw(self):
        self.address_pre_filler.redraw()
        self.group_id.redraw()
        self.sign_id.redraw()
        self.layout.update()
        return
    
    def change_font_size(self, new_size):
        self.address_pre_filler.change_font_size(new_size)
        self.group_id.change_font_size(new_size)
        self.sign_id.change_font_size(new_size)
        self.layout.update()
        return
    
    def update_down(self):
        text = "\\X01"
        text += self.address_pre_filler.constructed_element.text
        text += self.group_id.constructed_element.text
        text += self.sign_id.constructed_element.text
        self.constructed_element.set_text(text)
        return
    
    def update_up(self):
        self.update_down()
        self.app.update()
        return
    
    def __make_layout(self):
        layout = QHBoxLayout()
        layout.addLayout(self.address_pre_filler.layout)
        layout.addLayout(self.group_id.layout)
        layout.addLayout(self.sign_id.layout)
        LayoutTools.shared_container_formatting(layout)
        return layout