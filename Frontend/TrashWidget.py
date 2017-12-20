import sip
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QIcon
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QWidget

from Frontend.FrontendConfig import TrashIconPath, ElementMimeType


class TrashWidget(QSvgWidget):
    def __init__(self):
        super().__init__(TrashIconPath)
        self.setFixedSize(70,70)
        self.setAcceptDrops(True)


    def dragEnterEvent(self,event):
        mime = event.mimeData()
        if mime.hasFormat(ElementMimeType):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):

        mime = event.mimeData()
        if mime.hasFormat(ElementMimeType):
            import Frontend

            if Frontend.PlayGround.DraggedElement is None:
                return

            parentPlayGround = Frontend.PlayGround.DraggedElement.parent()

            if parentPlayGround is None:
                return

            print(Frontend.PlayGround.DraggedElement)
            parentPlayGround.layout.removeWidget(Frontend.PlayGround.DraggedElement)
            sip.delete(Frontend.PlayGround.DraggedElement)
            Frontend.PlayGround.DraggedElement = None

            event.accept()
