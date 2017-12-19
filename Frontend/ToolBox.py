from PyQt5.QtCore import QSize, QMimeData, QByteArray, Qt
from PyQt5.QtGui import QIcon, QDrag
from PyQt5.QtWidgets import QListWidget, QListView, QListWidgetItem

import Frontend
from Frontend.FrontendConfig import ElementIconPath, ElementMimeType, ElementWidgetType


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
        for key, value in sorted(ElementIconPath.items()):
            print(key, value)

            item = QListWidgetItem(self)
            item.setIcon(QIcon(ElementIconPath[key]))
            item.setFlags(
                Qt.ItemIsEnabled |
                Qt.ItemIsSelectable |
                Qt.ItemIsDragEnabled)
            item.elementKey = key


    def startDrag(self, supportedActions):
        item = self.currentItem()

        module = my_import("Frontend.ElementWidget")
        widgetClass = getattr(module, ElementWidgetType[item.elementKey])
        Frontend.PlayGround.DraggedElement = widgetClass()

        mimedata = QMimeData()
        mimedata.setData(ElementMimeType, QByteArray())

        drag = QDrag(self)
        drag.setMimeData(mimedata)

        drag.exec_(Qt.MoveAction)

def my_import(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod