from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QSpinBox, QDoubleSpinBox
from copy import deepcopy


class ElementWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 40)
        self.BackgroundColor = '#AAAAAA'
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.fillRect(self.rect(), QColor(self.BackgroundColor))
        painter.end()



class IncXWidget(ElementWidget):
    def __init__(self):
        super().__init__()
        self.BackgroundColor = '#EACF56'
        self.label = QLabel("Increment X:")
        self.spinboxX = QDoubleSpinBox()
        self.spinboxX.setSingleStep(0.1)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.spinboxX)


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
        self.label = QLabel("Landing")
        self.layout.addWidget(self.label)

class LoopWidget(ElementWidget):
    def __init__(self):
        super().__init__()
        self.BackgroundColor = '#37A2D7'
        from Frontend.PlayGround import PlayGround
        self.innerPlayground = PlayGround()
        self.layout.addWidget(self.innerPlayground)
