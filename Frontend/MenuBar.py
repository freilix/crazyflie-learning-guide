from threading import Thread

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QComboBox
from Backend.Backend import ScanInterfaces, ConnectToCrazyflie, SendCoordinatesToCrazyflie, ChangePositionCoordinates, PlayAndSendSequence
from Backend.SequenceList import SequenceList

class MenuBar(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.mainWindow = parent

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
        self.playing = False
        self.scf = None

    def buttonPlayPressed(self):
        if (not self.scf) or self.playing:
            pass

        list = SequenceList()
        playground = self.mainWindow.playground
        count = playground.layout.count()
        for i in range(0, count):
            c = playground.layout.itemAt(i).widget()
            element = c.play()
            list.add(element)

        backendThread = Thread(target=PlayAndSendSequence, args=(self.scf, list,))
        backendThread.start()

        # PlayAndSendSequence(self.scf, list)
        # ChangePositionCoordinates(list)
        # SendCoordinatesToCrazyflie(self.scf)
        self.playing = True

        # threadListRunner.start()
        #threadGlobalPosition.start()
        #check = Thread(target=self.checkIfThreadFinished, args=(threadListRunner, threadGlobalPosition,))
        #check.start()


    def buttonConnectPressed(self):
        currentAdress = self.comboBoxAdresses.currentText()
        #if currentAdress.isspace():
        if self.scf:
            return
        self.scf = ConnectToCrazyflie(currentAdress) # todo own thread

    def buttonSearchPressed(self):
        threadGlobalPosition = Thread(target=self.SetComboBoxAdresses, args=())
        threadGlobalPosition.start()

    def SetComboBoxAdresses(self):
        available = ScanInterfaces()
        if available: # todo and self.comboBoxAdresses.count() > 0:
            self.comboBoxAdresses.addItem(available[0][0])

    def checkIfThreadFinished(self, threadListRunner, threadGlobalPosition):
        while threadListRunner.is_alive():
            pass
        threadGlobalPosition._stop()
        self.playing = False