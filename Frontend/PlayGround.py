from PyQt5 import QtCore

from PyQt5.QtCore import QRect, Qt, QByteArray, QDataStream, QIODevice
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QListWidget, QFrame, QVBoxLayout, QGridLayout, QWidgetItem

from Frontend.ElementWidget import ElementWidget, IncXWidget, LandWidget
from Frontend.FrontendConfig import ElementMimeType, ElementWidgetType

DraggedElement = None


class PlayGround(QWidget):
    def __init__(self, parent=None):
        super(PlayGround, self).__init__(parent)

        self.dropPosRect = QRect()

        self.ElementList = [ElementWidget(), ElementWidget()]
        self.setAcceptDrops(True)

        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        self.insertElementWidget(3, LandWidget())


    def insertElementWidget(self, index, element):
        self.layout.insertWidget(index, element)
        pass


    def dragEnterEvent(self, event):
        mime = event.mimeData()
        if mime.hasFormat(ElementMimeType):
            event.accept()
        else:
            event.ignore()


    def dragMoveEvent(self, event):
        mime = event.mimeData()
        if mime.hasFormat(ElementMimeType):
            self.updateDropPosition(event.pos())
            event.accept()
        else:
            event.ignore()
        self.update()


    def updateDropPosition(self, position):
        pass


    def dropEvent(self, event):
        mime = event.mimeData()

        if mime.hasFormat(ElementMimeType):
            self.insertElementWidget(self.CalcInsertionIndex(event.pos()), DraggedElement)

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

    def CalcInsertionIndex(self,pos):




        return 1
