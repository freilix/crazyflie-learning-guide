from PyQt5.QtCore import QSize, Qt, QMimeData, QByteArray
from PyQt5.QtGui import QIcon, QBrush, QColor, QDrag
from PyQt5.QtWidgets import QListWidget, QListView, QListWidgetItem

from Frontend.UiConfig import ElementIconPath, ElementMimeType


class ToolBox(QListWidget):
    def __init__(self, parent=None):
        super(ToolBox, self).__init__(parent)

        self.setDragEnabled(True)
        self.setViewMode(QListView.ListMode)
        self.setIconSize(QSize(140, 60))
        self.setSpacing(0)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setMaximumWidth(140)

        self.addElements()

    def addElements(self):
        qPositionMoverItem = QListWidgetItem(self)
        qPositionMoverItem.setIcon(
            QIcon(ElementIconPath['INC_X']))
        qPositionMoverItem.setBackground(QBrush(QColor().black()))
        qPositionMoverItem.setFlags(
            Qt.ItemIsEnabled |
            Qt.ItemIsSelectable |
            Qt.ItemIsDragEnabled)

    def startDrag(self, supportedActions):
        item = self.currentItem()

        mimedata = QMimeData()
        mimedata.setData(ElementMimeType['INC_X'], QByteArray())

        drag = QDrag(self)
        drag.setMimeData(mimedata)

        drag.exec_(Qt.MoveAction)
