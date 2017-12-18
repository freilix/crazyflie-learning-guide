import json
import pickle

from PyQt5 import QtGui

from PyQt5.QtCore import QSize, QMimeData, QByteArray, Qt, QDataStream, QIODevice
from PyQt5.QtGui import QIcon, QBrush, QColor, QDrag, QPainter
from PyQt5.QtWidgets import QListWidget, QListView, QListWidgetItem, QStyle

import Frontend
from Frontend.ElementWidget import IncXWidget, IncYWidget, IncZWidget, IncYawWidget, PosSetWidget, LandWidget
from Frontend.FrontendConfig import ElementIconPath, ElementMimeType, ElementWidgetType
from Frontend.PlayGround import DraggedElement




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
        self.setStyleSheet("""QListWidget{ background: transparent; } """)

        self.mimeTypes()

    def addElements(self):
        for key in ElementIconPath.keys():
            item = QListWidgetItem(self)
            item.setIcon(QIcon(ElementIconPath[key]))
            item.setFlags(
                Qt.ItemIsEnabled |
                Qt.ItemIsSelectable |
                Qt.ItemIsDragEnabled)
            item.elementKey = key

    def startDrag(self, supportedActions):
        item = self.currentItem()

        # elementData = QByteArray()
        # dataStream = QDataStream(elementData,QIODevice.WriteOnly)
        # dataStream.writeQVariant(item.elementWidget)

        widgetClass = getattr(__import__('ElementWidget'), ElementWidgetType[item.elementKey])
        Frontend.PlayGround.DraggedElement = widgetClass()

        mimedata = QMimeData()
        mimedata.setData(ElementMimeType,QByteArray())

        drag = QDrag(self)
        drag.setMimeData(mimedata)

        drag.exec_(Qt.MoveAction)

