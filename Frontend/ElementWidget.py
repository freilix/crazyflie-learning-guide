from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget


class ElementWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 40)
        self.BackgroundColor = '#AAAAAA'

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.fillRect(self.rect(), QColor(self.BackgroundColor))
        painter.end()


class IncXWidget(ElementWidget):
    def __init__(self):
        super().__init__()
        self.BackgroundColor = '#EACF56'


class IncYWidget(ElementWidget):
    def __init__(self):
        super().__init__()
        self.BackgroundColor = '#88C363'


class IncZWidget(ElementWidget):
    def __init__(self):
        super().__init__()
        self.BackgroundColor = '#98CFEA'


class IncYawWidget(ElementWidget):
    def __init__(self):
        super().__init__()
        self.BackgroundColor = '#F07E30'


class PosSetWidget(ElementWidget):
    def __init__(self):
        super().__init__()
        self.BackgroundColor = '#C6B6E4'


class LandWidget(ElementWidget):
    def __init__(self):
        super().__init__()
        self.BackgroundColor = '#A8A8A8'
