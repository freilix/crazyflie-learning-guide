import sys

from PyQt5.QtCore import QSize, Qt, QMimeData, QByteArray, QRect
from PyQt5.QtGui import QBrush, QColor, QCursor, QIcon, QPainter, QIconEngine, QPixmap, QDrag
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QHBoxLayout, QListWidget, QListView, QListWidgetItem, \
    QWidget

# Configuration
MIMEDATA_MOVE_X = 'cf-element/MoveX'
ICONPATH_MOVE_X = 'D:\Studium\AMS SourceCode\crazyflie-learning-guide\Frontend\Icons\moveX.png'
app = QApplication(sys.argv)

# Element Pool
class ToolBox(QListWidget):
    def __init__(self, parent=None):
        super(ToolBox, self).__init__(parent)

        self.setDragEnabled(True)
        self.setViewMode(QListView.ListMode)
        self.setIconSize(QSize(60, 60))
        self.setSpacing(0)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setMaximumWidth(140)

        self.addElements()

    def addElements(self):
        qPositionMoverItem = QListWidgetItem(self)
        qPositionMoverItem.setIcon(
            QIcon(ICONPATH_MOVE_X))
        qPositionMoverItem.setBackground(QBrush(QColor().black()))
        qPositionMoverItem.setFlags(
            Qt.ItemIsEnabled |
            Qt.ItemIsSelectable |
            Qt.ItemIsDragEnabled)

    def startDrag(self, supportedActions):
        item = self.currentItem()

        mimedata = QMimeData()
        mimedata.setData(MIMEDATA_MOVE_X, QByteArray())

        drag = QDrag(self)
        drag.setMimeData(mimedata)

        drag.exec_(Qt.MoveAction)

# Frame to put Elements in and reorganisize them
class PlayGround(QWidget):
    def __init__(self, parent=None):
        super(PlayGround, self).__init__(parent)

        self.setAcceptDrops(True)
        self.setMinimumSize(600, 600)
        self.setMaximumWidth(600)

    def dragEnterEvent(self, event):

        if event.mimeData().hasFormat(MIMEDATA_MOVE_X):
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        self.updateDropPositionHighlighting(event.pos())
        if event.mimeData().hasFormat(MIMEDATA_MOVE_X):
            event.accept()
        else:
            event.ignore()
        self.update()

    def updateDropPositionHighlighting(self, position):
        pass

    def dropEvent(self, event):
        mime = event.mimeData()
        if mime.hasformat(MIMEDATA_MOVE_X):
            rectWidget = QWidget(100, 100, 100, 100)
            rectWidget.setMinimumSize(100, 100)

            rectWidget.setParent(self)
            self.update(rectWidget)
            event.setDropAction(Qt.MoveAction)
        else:
            event.ignore()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupWidgets()

    def setupWidgets(self):
        frame = QFrame()

        frameLayout = QHBoxLayout(frame)
        toolbox = ToolBox()
        playground = PlayGround()

        frameLayout.addWidget(toolbox)
        frameLayout.addWidget(playground)
        self.setCentralWidget(frame)


window = MainWindow()
window.show()
sys.exit(app.exec_())
