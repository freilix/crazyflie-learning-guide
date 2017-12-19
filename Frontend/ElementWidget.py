from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QSpinBox, QDoubleSpinBox, QGridLayout, QLayout
from copy import deepcopy


class ElementWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.BackgroundColor = '#AAAAAA'
        self.setDefaultLayout()
        self.setLayout(self.layout)

    def setDefaultLayout(self):
        self.layout = QHBoxLayout()


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
        self.spinboxX.setMinimum(-5)
        self.spinboxX.setMaximum(5)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.spinboxX)


class IncYWidget(ElementWidget):
    def __init__(self):
        super().__init__()
        self.BackgroundColor = '#88C363'
        self.label = QLabel("Increment Y:")
        self.spinboxY = QDoubleSpinBox()
        self.spinboxY.setSingleStep(0.1)
        self.spinboxY.setMinimum(-5)
        self.spinboxY.setMaximum(5)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.spinboxY)


class IncZWidget(ElementWidget):
    def __init__(self):
        super().__init__()
        self.BackgroundColor = '#98CFEA'
        self.label = QLabel("Increment Z:")
        self.spinboxZ = QDoubleSpinBox()
        self.spinboxZ.setSingleStep(0.1)
        self.spinboxZ.setMinimum(-5)
        self.spinboxZ.setMaximum(5)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.spinboxZ)


class IncYawWidget(ElementWidget):
    def __init__(self):
        super().__init__()
        self.BackgroundColor = '#F07E30'
        self.label = QLabel("Increment Yaw:")
        self.spinboxYaw = QDoubleSpinBox()
        self.spinboxYaw.setSingleStep(1)
        self.spinboxYaw.setMaximum(180)
        self.spinboxYaw.setMinimum(-180)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.spinboxYaw)


class PosSetWidget(ElementWidget):
    def __init__(self):
        super().__init__()
        self.BackgroundColor = '#C6B6E4'
        self.label = QLabel("Position")

        self.labelX = QLabel("X:")
        self.labelY = QLabel("Y:")
        self.labelZ = QLabel("Z:")
        self.labelYaw = QLabel("Yaw:")

        self.spinboxX = QDoubleSpinBox()
        self.spinboxY = QDoubleSpinBox()
        self.spinboxZ = QDoubleSpinBox()
        self.spinboxYaw = QDoubleSpinBox()

        self.spinboxX.setSingleStep(0.1)
        self.spinboxY.setSingleStep(0.1)
        self.spinboxZ.setSingleStep(0.1)
        self.spinboxYaw.setSingleStep(1)

        self.spinboxX.setMinimum(0)
        self.spinboxY.setMinimum(0)
        self.spinboxZ.setMinimum(0.1)
        self.spinboxYaw.setMinimum(0)

        self.spinboxX.setMaximum(5)
        self.spinboxY.setMaximum(5)
        self.spinboxZ.setMaximum(5)
        self.spinboxYaw.setMaximum(359)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.labelX)
        self.layout.addWidget(self.spinboxX)
        self.layout.addWidget(self.labelY)
        self.layout.addWidget(self.spinboxY)
        self.layout.addWidget(self.labelZ)
        self.layout.addWidget(self.spinboxZ)
        self.layout.addWidget(self.labelYaw)
        self.layout.addWidget(self.spinboxYaw)


class LandWidget(ElementWidget):
    def __init__(self):
        super().__init__()
        self.BackgroundColor = '#CCA55E'
        self.label = QLabel("Landing")
        self.layout.addWidget(self.label)


class LoopWidget(ElementWidget):
    def __init__(self):
        super().__init__()
        self.BackgroundColor = '#AAAAAA'
        from Frontend.PlayGround import PlayGround
        self.innerPlayground = PlayGround()

        self.label = QLabel("Loop n-times:")
        self.forSpinbox = QSpinBox()
        self.forSpinbox.setMinimum(1)


        self.layout.addWidget(self.innerPlayground, 1, 0, 1, 2)
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.forSpinbox, 0, 1)

    def setDefaultLayout(self):
        self.layout = QGridLayout()

