from PyQt5.QtWidgets import QHBoxLayout, QTextEdit, QSizePolicy
from PyQt5.QtCore import Qt
from typing import TYPE_CHECKING
from LabelSettings import LabelSettings
from TextAnimator import TextAnimator


if TYPE_CHECKING:
    from MainWindow import MainWindow


class ConstructedFrame:

    app: "MainWindow"
    frame: QTextEdit
    layout: QHBoxLayout
    settings: LabelSettings

    def __init__(self, app: "MainWindow"):
        self.app = app
        self.settings = LabelSettings()
        self.settings.colors.background = "255,255,255"
        self.settings.colors.foreground = "0,0,0"
        self.__make_layout()
        self.__make_controls()
        self.animator = TextAnimator(self.frame)
        return
    
    def __make_layout(self):
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(5)
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        return
    
    def __make_controls(self):
        self.frame = self.__frame()
        self.layout.addWidget(self.frame)
        return
    
    def __frame_style(self):
        style =  f"""
            background-color: rgb({self.settings.colors.background});
            border: 2px solid black;
            border-radius: 5px;
            color: rgb({self.settings.colors.foreground});
            font: {self.settings.font.size}px "{self.settings.font.family}";
            font-weight: {self.settings.font.weight};
            padding: 5px;
        """
        return style
    
    def __frame(self):
        frame = QTextEdit()
        frame.setText("\\X01\\X04")
        frame.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )
        frame.setFixedHeight(46)
        frame.setAlignment(Qt.AlignCenter)
        frame.setStyleSheet(self.__frame_style())
        # frame.textChanged.connect(self.__adjust_height)
        return frame
    
    def __adjust_height(self):
        line_count = max(1, self.frame.document().blockCount())
        new_height = 19 * line_count + 30
        self.frame.setFixedHeight(new_height)
        return

    def update(self):
        return
    
    def construct(self):
        
        return
    
    def change_text(self, new_text):
        old_text = self.frame.toPlainText()
        if new_text == old_text:
            return
        self.frame.setText(new_text)
        # self.__adjust_height()
        self.frame.setAlignment(Qt.AlignCenter)
        new_text_ = self.convert_to_bytes(new_text)
        old_text = self.convert_to_bytes(old_text)
        diff = self._diff_checker(old_text, new_text_)
        max = diff[-1]
        min = diff[0]
        diff = [x for x in range(min, max+1)]
        diff = [x for x in diff if x < len(new_text) - 4]
        self.animator.start(diff)
        return
    
    def convert_to_bytes(self, input_string):
        import re    
        def replace_match(match):
            return int(match.group(1), 16).to_bytes(1, byteorder='big').decode("utf-8")
        pattern = r'\\X([0-9A-Fa-f]{2})'
        byte_array = re.sub(pattern, replace_match, input_string)
        byte_array.encode("utf-8")
        return byte_array
    
    def _diff_checker(self, a, b):
        def inc_c(c, x):
            if x.isprintable():
                return c+1
            return c+4
        len_a = len(a)
        len_b = len(b)
        if len_a >= len_b:
            l = a
            s = b
        if len_b > len_a:
            l = b
            s = a
        r = []
        c = 0
        while len(l) > 0:
            x = l[0]
            if len(s) == 0:
                l = l[1:]
                r.append(c)
                c = inc_c(c, x)
                continue
            if l[0] == s[0]:
                l = l[1:]
                s = s[1:]
                c = inc_c(c, x)
                continue
            if len(l) == len(s):
                s = s[1:]
            l = l[1:]
            r.append(c)
            c = inc_c(c, x)
        return r