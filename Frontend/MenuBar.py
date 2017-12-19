from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton


class MenuBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(30)
        self.layout = QHBoxLayout()

        self.layout.addWidget(QLabel("Test1"))
        #self.layout.addWidget(QPushButton("Test"))

        self.setLayout(self.layout)

