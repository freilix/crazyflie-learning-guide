from PyQt5.QtCore import QRect, Qt, QByteArray, QMimeData
from PyQt5.QtGui import QPainter, QDrag
from PyQt5.QtWidgets import QWidget, QVBoxLayout

import Frontend
from Frontend.ElementWidget import ElementWidget, LoopWidget
from Frontend.FrontendConfig import ElementMimeType


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

        self.dragStartPosition = None

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
        newSpaceIndex = self.calcInsertionIndex(pos)
        draggedElementIndex = self.layout.indexOf(DraggedElement)
        spaceIndex = self.layout.indexOf(self.spaceElement)

        # print("new " + newSpaceIndex.__str__())
        # print("drg " + draggedElementIndex.__str__())
        # print("spc " + spaceIndex.__str__())
        # print("------------------")

        spaceAlreadyAtCorrectIndex = newSpaceIndex -1 == spaceIndex
        oldElementDragged = draggedElementIndex != -1
        spaceIsNeigbourOfDraggedElement = oldElementDragged and (draggedElementIndex == newSpaceIndex or draggedElementIndex +1 == newSpaceIndex)
        noSpaceShown = spaceIndex == -1

        if noSpaceShown or not (spaceAlreadyAtCorrectIndex or spaceIsNeigbourOfDraggedElement):
            self.layout.insertWidget(newSpaceIndex, self.spaceElement)
            self.update()

    def dropEvent(self, event):
        mime = event.mimeData()

        if mime.hasFormat(ElementMimeType):
            spaceIndex = self.layout.indexOf(self.spaceElement)
            self.layout.removeWidget(self.spaceElement)
            self.insertElementWidget(spaceIndex, DraggedElement)
            Frontend.PlayGround.DraggedElement = None
            self.update()

            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.ignore()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.fillRect(event.rect(), Qt.darkGray)
        painter.end()

    def calcInsertionIndex(self, pos):
        middleXPos = int(self.sizeHint().width() / 2)

        childAtOriginalPos = self.childAt(middleXPos, pos.y())
        elementWidgetParentAtOriginalPos = self.getParentElementWidget(childAtOriginalPos)

        index = self.layout.indexOf(elementWidgetParentAtOriginalPos)

        if index is not -1:
            return index

        ManipulatedYPos = pos.y() + self.layout.spacing() * 4
        childAtManipuatedPos = self.childAt(middleXPos, ManipulatedYPos)
        elementWidgetParentAtManipulatedPos = self.getParentElementWidget(childAtManipuatedPos)
        index = self.layout.indexOf(elementWidgetParentAtManipulatedPos)

        if index == -1:
            index = self.layout.count()
        return index

    def mouseMoveEvent(self, event):
        if self.dragStartPosition is not None:
            childAtPos = self.childAt(self.dragStartPosition)
            parentElementWidget = self.getParentElementWidget(childAtPos)
            if issubclass(type(parentElementWidget), ElementWidget):
                drag = QDrag(self);
                mimeData = QMimeData();
                mimeData.setData(ElementMimeType, QByteArray())
                Frontend.PlayGround.DraggedElement = parentElementWidget
                self.dragStartPosition = None
                drag.setMimeData(mimeData);

                drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, event):
        childAtPos = self.childAt(event.pos())
        parentElementWidget = self.getParentElementWidget(childAtPos)
        if event.button() == Qt.LeftButton and issubclass(type(parentElementWidget), ElementWidget):
            self.dragStartPosition = event.pos()

    def getParentElementWidget(self, child):
        if child is None:
            return None

        if child is self:
            return None

        if issubclass(type(child), ElementWidget):
            return child

        parent = child.parent()
        while not issubclass(type(parent), ElementWidget):
            if parent is self:
                return None
            parent = parent.parent()
        return parent
