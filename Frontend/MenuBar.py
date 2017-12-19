from threading import Thread

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QComboBox
from Backend.Backend import ScanInterfaces, ConnectToCrazyflie

class MenuBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumHeight(30)
        self.layout = QHBoxLayout()

        self.buttonSearch = QPushButton("Search")
        self.buttonSearch.clicked.connect(self.buttonSearchPressed)
        self.layout.addWidget(self.buttonSearch)

        self.comboBoxAdresses = QComboBox()
        self.layout.addWidget(self.comboBoxAdresses)

        self.buttonConnect = QPushButton("Connect")
        self.buttonConnect.clicked.connect(self.buttonConnectPressed)
        self.layout.addWidget(self.buttonConnect)

        self.buttonPlay = QPushButton("Play")
        self.buttonPlay.clicked.connect(self.buttonPlayPressed)
        self.layout.addWidget(self.buttonPlay)

        self.setLayout(self.layout)

    def buttonPlayPressed(self):
        pass

    def buttonConnectPressed(self):
        currentAdress = self.comboBoxAdresses.currentText()
        if currentAdress.isspace():
            ConnectToCrazyflie(currentAdress)

    def buttonSearchPressed(self):
        threadGlobalPosition = Thread(target=self.SetComboBoxAdresses, args=())
        threadGlobalPosition.start()

    def SetComboBoxAdresses(self):
        available = ScanInterfaces()
        if available:
            self.comboBoxAdresses.addItem(available[0][0]) #todo: iterate over complete list