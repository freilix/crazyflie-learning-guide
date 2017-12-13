from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QWidget


class MenuBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(30)

