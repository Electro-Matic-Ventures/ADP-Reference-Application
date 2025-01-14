from PyQt5.QtGui import QTextCharFormat, QColor
from PyQt5.QtCore import QTimer


class TextAnimator:

    def __init__(self, text_edit):
        self.text_edit = text_edit
        self.duration = 2000
        self.steps = 180
        self.current_step = 0
        self.timer = QTimer()
        self.timer.setInterval(self.duration // self.steps)
        self.timer.timeout.connect(self._animate_step)
        return

    def start(self, indices):
        self.indices = indices
        self.timer.start()
        return

    def _animate_step(self):
        ratio = self.current_step / self.steps
        bg_color = QColor(
            255, int(255 * ratio), int(255 * ratio)
        )
        text_color = QColor(
            255 - int(255 * ratio), 255 - int(255 * ratio), 255 - int(255 * ratio)
        ) 
        cursor = self.text_edit.textCursor()
        format = QTextCharFormat()
        format.setBackground(bg_color)
        format.setForeground(text_color)
        for index in self.indices:
            cursor.setPosition(index)
            cursor.movePosition(cursor.NextCharacter, cursor.KeepAnchor)
            cursor.setCharFormat(format)
        self.current_step += 1
        if self.current_step > self.steps:
            self.timer.stop()
            self._reset_formatting()
            self.current_step = 0
        return
    
    def _reset_formatting(self):
        cursor = self.text_edit.textCursor()
        default_format = QTextCharFormat()
        for index in self.indices:
            cursor.setPosition(index)
            cursor.movePosition(cursor.NextCharacter, cursor.KeepAnchor)
            cursor.setCharFormat(default_format)
        return