from PyQt5 import QtCore

from PyQt5.QtCore import QRect, Qt, QByteArray, QDataStream, QIODevice
from PyQt5.QtGui import QPainter, QPalette
from PyQt5.QtWidgets import QWidget, QListWidget, QFrame, QVBoxLayout, QGridLayout, QWidgetItem, QSpacerItem

from Frontend.FrontendConfig import ElementMimeType, ElementWidgetType

DraggedElement = None


class PlayGround(QWidget):
    def __init__(self, parent=None):
        super(PlayGround, self).__init__(parent)

        self.dropPosRect = QRect()

        self.setAcceptDrops(True)

        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        self.spaceElement = QWidget(self)
        self.spaceElement.setFixedHeight(10)


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


    def updateDropPosition(self, pos):
        index = self.CalcInsertionIndex(pos)
        if index != -1 and self.layout.indexOf(self.spaceElement) != index-1:
            self.layout.insertWidget(index,self.spaceElement)


    def dropEvent(self, event):
        mime = event.mimeData()

        if mime.hasFormat(ElementMimeType):
            self.insertElementWidget(self.layout.indexOf(self.spaceElement), DraggedElement)
            self.layout.removeWidget(self.spaceElement)
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
        index = self.layout.indexOf(self.childAt(pos.x(),pos.y()))
        if index == -1:
            index = self.layout.indexOf(self.childAt(int(self.width()/2),pos.y()+10))
            if index == -1:
                index = self.layout.count()
        return index
