import abc

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QSpinBox, QDoubleSpinBox, QGridLayout

from Backend.Elements.IncrementXElement import IncrementXElement
from Backend.Elements.IncrementYElement import IncrementYElement
from Backend.Elements.IncrementYawElement import IncrementYawElement
from Backend.Elements.IncrementZElement import IncrementZElement
from Backend.Elements.LandingElement import LandingElement
from Backend.Elements.LoopElement import LoopElement
from Backend.Elements.PositionMoverElement import PositionMoverElement
from Backend.SequenceList import SequenceList


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

    @abc.abstractmethod
    def play(self):
        raise NotImplementedError("abstract method")


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

    def play(self):
        return IncrementXElement(self.spinboxX.value())


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

    def play(self):
        return IncrementYElement(self.spinboxY.value())


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

    def play(self):
        return IncrementZElement(self.spinboxZ.value())


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

    def play(self):
        return IncrementYawElement(self.spinboxYaw.value())


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

    def play(self):
        return PositionMoverElement(self.spinboxX.value(), self.spinboxY.value(), self.spinboxZ.value(),
                                    self.spinboxYaw.value())


class LandWidget(ElementWidget):
    def __init__(self):
        super().__init__()
        self.BackgroundColor = '#CCA55E'
        self.label = QLabel("Landing")
        self.layout.addWidget(self.label)

    def play(self):
        return LandingElement()


class LoopWidget(ElementWidget):
    def __init__(self):
        super().__init__()
        self.BackgroundColor = '#BBBBBB'
        from Frontend.PlayGround import PlayGround
        self.innerPlayground = PlayGround()

        self.label = QLabel("Loop times:")
        self.forSpinbox = QSpinBox()
        self.forSpinbox.setMinimum(1)

        self.layout.addWidget(self.innerPlayground, 1, 0, 1, 2)
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.forSpinbox, 0, 1)

    def play(self):
        list = SequenceList()
        playground = self.innerPlayground
        count = playground.layout.count()
        for i in range(0, count):
            c = playground.layout.itemAt(i).widget()
            element = c.play()
            list.add(element)
        return LoopElement(self.forSpinbox.value(), list)

    def setDefaultLayout(self):
        self.layout = QGridLayout()
