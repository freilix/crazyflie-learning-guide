from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QIcon
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QWidget

from Frontend.FrontendConfig import TrashIconPath


class TrashWidget(QSvgWidget):
    def __init__(self):
        super().__init__(TrashIconPath)
        self.setFixedSize(70,70)




