from ButtonSettings import ButtonSettings
from CONSTANTS import COLORS


class Button:

    app: any
    host: any
    settings: ButtonSettings

    def __init__(self):
        self.settings = ButtonSettings()
        return

    def _darken(self):
        colors = self.settings.colors.background.split(",")
        for i, color in enumerate(colors):
            colors[i] = str(int(int(color) * 0.7))
        self.settings.colors.background = ",".join(colors)
        self.button.setStyleSheet(self._button_style())
        self.redraw()
        return
    
    def _reset_color(self):
        self.settings.colors.background = COLORS.EM_BLUE
        self.button.setStyleSheet(self._button_style())
        self.redraw()
        return
        
    def hide(self):
        self.button.hide()
        self.redraw()
        return

    def show(self):
        self.button.show()
        self.redraw()
        return

    def redraw(self):
        self.button.setStyleSheet(self._button_style())
        self.button.setFixedSize(
            self.settings.dimensions.width,
            self.settings.dimensions.height
        )
        self.button.update()
        self.layout.update()
        return
    
    def change_font_size(self, new_size):
        self.settings.font.size = new_size
        self.settings.dimensions.redim_button(new_size)
        self.redraw()
        return