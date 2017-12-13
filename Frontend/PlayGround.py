from PyQt5 import QtCore

from PyQt5.QtCore import QRect, Qt, QByteArray
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QListWidget, QFrame, QVBoxLayout, QGridLayout

from Frontend.ElementWidget import ElementWidget, IncXWidget
from Frontend.FrontendConfig import ElementMimeType, isElementMimeType, ElementWidgetType


class PlayGround(QWidget):
    def __init__(self, parent=None):
        super(PlayGround, self).__init__(parent)

        self.dropPosRect = QRect()

        self.ElementList = [ElementWidget(), ElementWidget()]
        self.setAcceptDrops(True)

        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignHCenter)

        self.insertElementWidget(3, ElementWidget())

    def insertElementWidget(self, index, element):
        self.layout.insertWidget(index, element)
        pass

    def dragEnterEvent(self, event):
        if isElementMimeType(event.mimeData()):
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if isElementMimeType(event.mimeData()):
            self.updateDropPosition(event.pos())
            event.accept()
        else:
            event.ignore()
        self.update()

    def updateDropPosition(self, position):
        pass

    def dropEvent(self, event):
        mime = event.mimeData()

        if isElementMimeType(mime):
            data = mime.data(ElementMimeType['INC_X'])


            self.insertElementWidget(1, IncXWidget())
            self.update()

            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.ignore()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.fillRect(event.rect(), Qt.white)

        painter.end()
