from PyQt5.QtWidgets import QMainWindow, QFrame, QHBoxLayout
from Frontend.PlayGround import PlayGround
from Frontend.ToolBox import ToolBox


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # Setup Widgets
        self.playground = PlayGround()
        self.toolbox = ToolBox()

        #
        frame = QFrame()
        frameLayout = QHBoxLayout(frame)

        frameLayout.addWidget(self.toolbox)
        frameLayout.addWidget(self.playground)
        self.setCentralWidget(frame)


