from PyQt5 import QtGui

from PyQt5.QtCore import QSize, Qt, QMimeData, QByteArray
from PyQt5.QtGui import QIcon, QBrush, QColor, QDrag, QPainter
from PyQt5.QtWidgets import QListWidget, QListView, QListWidgetItem, QStyle

from Frontend.FrontendConfig import ElementIconPath, ElementMimeType


class ToolBox(QListWidget):
    def __init__(self, parent=None):
        super(ToolBox, self).__init__(parent)

        self.setDragEnabled(True)
        self.setViewMode(QListView.ListMode)
        self.setIconSize(QSize(66, 40))
        self.setSpacing(0)
        self.setFixedWidth(70)
        self.addElements()

        self.setMinimumHeight((self.count() + 1) * 40 - 12)
        self.setFrameStyle(0)
        self.setStyleSheet("""QListWidget{ background: transparent; } """ )

    def addElements(self):
        for key in ElementIconPath:
            qPositionMoverItem = QListWidgetItem(self)
            qPositionMoverItem.setIcon(QIcon(ElementIconPath[key]))
            qPositionMoverItem.setFlags(
                Qt.ItemIsEnabled |
                Qt.ItemIsSelectable |
                Qt.ItemIsDragEnabled)

    def startDrag(self, supportedActions):
        item = self.currentItem()

        mimedata = QMimeData()
        bytes = QByteArray().append("INC_X")

        mimedata.setData(ElementMimeType['INC_X'], bytes)

        drag = QDrag(self)
        drag.setMimeData(mimedata)


        drag.exec_(Qt.MoveAction)
