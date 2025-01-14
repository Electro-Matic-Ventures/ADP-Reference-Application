from abc import ABC, abstractmethod
from TileSettings import TileSettings


class Tile(ABC):

    app: any
    host: any
    settings: TileSettings

    def __init__(self):
        self.settings = TileSettings()
        return

    @abstractmethod
    def _label_style(self):
        pass

    @abstractmethod
    def _label(self):
        pass

    @abstractmethod    
    def _value_style(self):
        pass

    @abstractmethod
    def _value(self):
        pass
    
    def redraw(self):
        self.label.setStyleSheet(self._label_style())
        self.label.setFixedSize(
            self.settings.label.dimensions.width, 
            self.settings.label.dimensions.height
        )
        self.value.setStyleSheet(self._value_style())
        self.value.setFixedSize(
            self.settings.value.dimensions.width, 
            self.settings.value.dimensions.height
        )
        self.label.update()
        self.value.update()
        self.layout.update()
        return
    
    def hide(self):
        self.label.hide()
        self.value.hide()
        self.redraw()
        return
    
    def show(self):
        self.label.show()
        self.value.show()
        self.redraw()
        return
    
    def change_font_size(self, new_size):
        self.settings.label.font.size = new_size
        self.settings.value.font.size = new_size
        self.settings.label.dimensions.redim_label(new_size)
        self.settings.value.dimensions.redim_value(new_size)
        self.settings.value.caret.redim(new_size)
        self.redraw()
        return
    