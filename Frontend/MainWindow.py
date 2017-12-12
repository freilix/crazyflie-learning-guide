from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QFrame, QHBoxLayout, QWidget, QGridLayout

from Frontend.MenuBar import MenuBar
from Frontend.PlayGround import PlayGround
from Frontend.ToolBox import ToolBox


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # Setup Widgets
        self.playground = PlayGround()
        self.toolbox = ToolBox()
        self.menuBar = MenuBar()
        #
        mainWidget = QWidget()
        layout = QGridLayout(mainWidget)

        layout.addWidget(self.menuBar,0,0,1,2)
        layout.addWidget(self.toolbox,1,0)
        layout.addWidget(self.playground,1,1)
        self.setCentralWidget(mainWidget)


