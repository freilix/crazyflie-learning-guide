from PyQt5 import QtCore

from PyQt5.QtCore import QRect, Qt, QByteArray, QDataStream, QIODevice, QMimeData
from PyQt5.QtGui import QPainter, QPalette, QDrag
from PyQt5.QtWidgets import QWidget, QListWidget, QFrame, QVBoxLayout, QGridLayout, QWidgetItem, QSpacerItem

import Frontend
from Frontend.ElementWidget import ElementWidget, LoopWidget
from Frontend.FrontendConfig import ElementMimeType, ElementWidgetType

DraggedElement = None


def isDraggedElementSuperElement(selfPlayGround):
    if not issubclass(type(DraggedElement), LoopWidget):
        return False

    parent = selfPlayGround.parent()

    while issubclass(type(parent), (LoopWidget, PlayGround)):
        if issubclass(type(parent), PlayGround):
            parent = parent.parent()
        else:
            if parent is DraggedElement:
                return True
            parent = parent.parent()
    return False


class PlayGround(QWidget):
    def __init__(self, parent=None):
        super(PlayGround, self).__init__(parent)

        self.dropPosRect = QRect()

        self.setAcceptDrops(True)

        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.spaceElement = QWidget(self)
        self.spaceElement.setFixedHeight(10)

    def insertElementWidget(self, index, element):
        self.layout.insertWidget(index, element)
        pass

    def dragEnterEvent(self, event):
        mime = event.mimeData()
        if mime.hasFormat(ElementMimeType) and not isDraggedElementSuperElement(self):
            event.accept()
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        self.layout.removeWidget(self.spaceElement)

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
        if index != -1 and self.layout.indexOf(self.spaceElement) != index - 1:
            self.layout.insertWidget(index, self.spaceElement)
            self.update()

    def dropEvent(self, event):
        mime = event.mimeData()

        if mime.hasFormat(ElementMimeType):
            self.insertElementWidget(self.layout.indexOf(self.spaceElement), DraggedElement)
            self.layout.removeWidget(self.spaceElement)
            Frontend.PlayGround.DraggedElement = None
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

    def CalcInsertionIndex(self, pos):
        index = self.layout.indexOf(self.childAt(pos.x(), pos.y()))
        if index == -1:
            index = self.layout.indexOf(self.childAt(int(self.width() / 2), pos.y() + 10))
            if index == -1:
                index = self.layout.count()
        return index

    def mousePressEvent(self, event):
        childAtPos = self.childAt(event.pos())
        parentElementWidget = self.getParentElementWidget(childAtPos)

        if event.button() == Qt.LeftButton and issubclass(type(parentElementWidget), ElementWidget):
            drag = QDrag(self);
            mimeData = QMimeData();
            mimeData.setData(ElementMimeType, QByteArray())
            Frontend.PlayGround.DraggedElement = parentElementWidget
            drag.setMimeData(mimeData);

            drag.exec_(Qt.MoveAction)

    def getParentElementWidget(self,qwidget):
        if self is qwidget:
            return None

        if issubclass(type(qwidget), ElementWidget):
            return qwidget

        parent = qwidget.parent()
        while not issubclass(type(parent), ElementWidget):
            if parent is self:
                return None
        return parent


