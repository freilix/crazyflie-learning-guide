from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QMainWindow, QFrame, QHBoxLayout, QWidget, QGridLayout, QScrollArea

from Frontend.MenuBar import MenuBar
from Frontend.PlayGround import PlayGround
from Frontend.ToolBox import ToolBox
from Frontend.TrashWidget import TrashWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # Setup Widgets
        self.playground = PlayGround()

        self.toolbox = ToolBox()
        self.menuBar = MenuBar(self)
        self.trash = TrashWidget()
        self.setWindowTitle("Crazyflie flight")

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.frameStyle()
        self.scrollArea.setWidget(self.playground)

        # setup layout
        mainWidget = QWidget()
        layout = QGridLayout(mainWidget)
        layout.setContentsMargins(10,10,10,10)
        layout.addWidget(self.menuBar, 0, 0, 1, 2)
        layout.addWidget(self.toolbox, 1, 0)
        layout.addWidget(self.trash, 2, 0)
        layout.addWidget(self.scrollArea, 1, 1, 2, 1)

        self.setCentralWidget(mainWidget)
