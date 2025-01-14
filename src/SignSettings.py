from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from typing import TYPE_CHECKING
from SettingMode import SettingMode
from SetDate import SetDate
from SetTime import SetTime
from SetDayOfWeek import SetDayOfWeek
from ConstructedElement import ConstructedElement
from CONSTANTS import SETTINGS_VALUES
from SetTimeFormat import SetTimeFormat
from PlaylistElements import PlaylistElements
from DefaultElements import DefaultElements
from LayoutTools import LayoutTools


if TYPE_CHECKING:
    from MainWindow import MainWindow
    from Message import Message


class SignSettings:

    def __init__(self, app: "MainWindow", host: "Message"):
        self.app: "MainWindow" = app
        self.host: "Message" = host
        self.constructed_element: ConstructedElement = ConstructedElement()
        self.setting_mode: SettingMode = SettingMode(app, self)
        self.set_date: SetDate = SetDate(app, self)
        self.set_time: SetTime = SetTime(app, self)
        self.set_day_of_week: SetDayOfWeek = SetDayOfWeek(app, self)
        self.set_time_format: SetTimeFormat = SetTimeFormat(app, self)
        self.playlist_elements: PlaylistElements = PlaylistElements(app, self)
        self.default_elements: DefaultElements = DefaultElements(app, self)
        self.layout: QHBoxLayout = self.__make_layout()
        return

    def change_font_size(self, new_size):
        self.setting_mode.change_font_size(new_size)
        self.set_date.change_font_size(new_size)
        self.layout.update()

    def base_mode(self):
        self.setting_mode.show()
        self.set_date.hide()
        self.set_day_of_week.hide()
        self.default_elements.hide()
        self.playlist_elements.hide()
        self.default_elements.hide()
        self.playlist_elements.hide()
        self.set_time.hide()
        self.set_time_format.hide()
        self.layout.update()
        return
    
    def clear_texts_mode(self):
        self.setting_mode.show()
        self.set_date.hide()
        self.set_day_of_week.hide()
        self.default_elements.hide()
        self.playlist_elements.hide()
        self.set_time.hide()
        self.set_time_format.hide()
        self.layout.update()
        return
    
    def clear_ram_mode(self):
        self.setting_mode.show()
        self.set_date.hide()
        self.set_day_of_week.hide()
        self.default_elements.hide()
        self.playlist_elements.hide()
        self.set_time.hide()
        self.set_time_format.hide()
        self.layout.update()
        return
    
    def clear_playlist_mode(self):
        self.setting_mode.show()
        self.set_date.hide()
        self.set_day_of_week.hide()
        self.default_elements.hide()
        self.playlist_elements.hide()
        self.set_time.hide()
        self.set_time_format.hide()
        self.layout.update()
        return
    
    def set_date_mode(self):
        self.setting_mode.show()
        self.set_date.show()
        self.set_day_of_week.hide()
        self.default_elements.hide()
        self.playlist_elements.hide()
        self.set_time.hide()
        self.set_time_format.hide()
        self.layout.update()
        return

    def set_day_of_week_mode(self):
        self.setting_mode.show()
        self.set_date.hide()
        self.set_day_of_week.show()
        self.default_elements.hide()
        self.playlist_elements.hide()
        self.set_time.hide()
        self.set_time_format.hide()
        self.layout.update()
        return
    
    def set_defaults_mode(self):
        self.setting_mode.show()
        self.set_date.hide()
        self.set_day_of_week.hide()
        self.default_elements.show()
        self.playlist_elements.hide()
        self.set_time.hide()
        self.layout.update()
        return
    
    def set_playlist_mode(self):
        self.setting_mode.show()
        self.set_date.hide()
        self.set_day_of_week.hide()
        self.default_elements.hide()
        self.playlist_elements.show()
        self.set_time.hide()
        self.layout.update()
        return
    
    def set_time_mode(self):
        self.setting_mode.show()
        self.set_date.hide()
        self.set_day_of_week.hide()
        self.default_elements.hide()
        self.playlist_elements.hide()
        self.set_time.show()
        self.set_time_format.hide()
        self.layout.update()
        return
    
    def set_time_format_mode(self):
        self.setting_mode.show()
        self.set_date.hide()
        self.set_day_of_week.hide()
        self.default_elements.hide()
        self.playlist_elements.hide()
        self.set_time.hide()
        self.set_time_format.show()
        self.layout.update()
        return
    
    def mode_select(self):
        """
        use for callback in SettingsSelect combobox
        """
        mode = self.setting_mode.value.currentText()
        if mode == "clear_flash_and_ram":
            self.clear_texts_mode()
            self.update_up()
            return
        if mode == "clear_ram":
            self.clear_ram_mode()
            self.update_up()
            return
        if mode == "clear_playlist":
            self.clear_playlist_mode()
            self.update_up()
            return
        if mode == "set_date":
            self.set_date_mode()
            self.update_up()
            return
        if mode == "set_day_of_week":
            self.set_day_of_week_mode()
            self.update_up()
            return
        if mode == "set_defaults":
            self.set_defaults_mode()
            self.update_up()
            return
        if mode == "set_playlist":
            self.set_playlist_mode()
            self.update_up()
            return
        if mode == "set_time":
            self.set_time_mode()
            self.update_up()
            return
        if mode == "set_time_format":
            self.set_time_format_mode()
            self.update_up()
            return
        return

    def hide(self):
        self.setting_mode.hide()
        self.set_date.hide()
        self.set_day_of_week.hide()
        self.default_elements.hide()
        self.playlist_elements.hide()
        self.set_time.hide()
        self.set_time_format.hide()
        self.layout.update()
        return
    
    def show(self):
        self.base_mode()
        self.layout.update()
        self.update_up()
        return

    def update_up(self):
        self.__update_constructed_element()
        self.host.update_up()
        return
    
    def __update_constructed_element(self):
        mode = self.setting_mode.value.currentText()
        text = SETTINGS_VALUES[mode]
        if mode == "clear_flash_and_ram":
            self.constructed_element.set_text(text)
            return        
        if mode == "clear_ram":
            self.constructed_element.set_text(text)
            return        
        if mode == "clear_playlist":
            self.constructed_element.set_text(text)
            return
        if mode == "set_date":
            text += self.set_date.constructed_element.text
            self.constructed_element.set_text(text)
            return
        if mode == "set_day_of_week":
            text += self.set_day_of_week.constructed_element.text
            self.constructed_element.set_text(text)
            return
        if mode == "set_defaults":
            text += self.default_elements.constructed_element.text
            self.constructed_element.set_text(text)
            return
        if mode == "set_playlist":
            text += self.playlist_elements.constructed_element.text
            self.constructed_element.set_text(text)
            return
        if mode == "set_time":
            text += self.set_time.constructed_element.text
            self.constructed_element.set_text(text)
            return
        if mode == "set_time_format":
            text += self.set_time_format.constructed_element.text
            self.constructed_element.set_text(text)
        return

    def __make_layout(self):
        layout = QHBoxLayout()
        layout.addLayout(self.setting_mode.layout)
        layout.addLayout(self.set_date.layout)
        layout.addLayout(self.set_time.layout)
        layout.addLayout(self.set_day_of_week.layout)
        layout.addLayout(self.set_time_format.layout)
        layout.addLayout(self.playlist_elements.layout)
        layout.addLayout(self.default_elements.layout)
        LayoutTools.shared_container_formatting(layout)
        return layout