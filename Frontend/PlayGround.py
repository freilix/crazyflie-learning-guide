from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget

from Frontend.UiConfig import ElementMimeType


class PlayGround(QWidget):
    def __init__(self, parent=None):
        super(PlayGround, self).__init__(parent)

        self.listRects = []
        self.highlightedRect = QRect()

        self.UiElementList = []

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):

        if event.mimeData().hasFormat(ElementMimeType['INC_X']):
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat(ElementMimeType['INC_X']):
            self.updateDropPositionHighlighting(event.pos())
            event.accept()
        else:
            event.ignore()
        self.update()

    def updateDropPositionHighlighting(self, position):
        pass

    def dropEvent(self, event):
        mime = event.mimeData()
        if mime.hasFormat(ElementMimeType['INC_X']):
            print(ElementMimeType['INC_X'])

            self.highlightedRect = QRect(100,100,100,100)
            self.update(self.highlightedRect)

            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.ignore()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.fillRect(event.rect(),Qt.white)
        painter.end()
