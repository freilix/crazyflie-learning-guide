from threading import Thread
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QComboBox, QLabel
from Backend.Backend import ScanInterfaces, ConnectToCrazyflie, PlayAndSendSequence
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

        self.connectedElement = QLabel()
        self.connectedElement.setText('not connected')
        self.layout.addWidget(self.connectedElement)

        self.setLayout(self.layout)
        self.scf = None

    def buttonPlayPressed(self):
        if not self.scf:
            return

        list = SequenceList()
        playground = self.mainWindow.playground
        count = playground.layout.count()
        for i in range(0, count):
            c = playground.layout.itemAt(i).widget()
            element = c.play()
            list.add(element)

        backendThread = Thread(target=PlayAndSendSequence, args=(self.scf, list,))
        backendThread.start()

    def buttonConnectPressed(self):
        def crazyflie_connection_lost(aa, a):
            self.scf = None
            self.connectedElement.setText('not connected')

        currentAdress = self.comboBoxAdresses.currentText()
        if self.scf or not currentAdress:
            return
        self.scf = ConnectToCrazyflie(currentAdress)
        self.scf.cf.connection_lost.add_callback(crazyflie_connection_lost)
        self.connectedElement.setText('connected')

    def buttonSearchPressed(self):
        threadGlobalPosition = Thread(target=self.SetComboBoxAdresses, args=())
        threadGlobalPosition.start()

    def SetComboBoxAdresses(self):
        self.comboBoxAdresses.clear()
        interfaces = ScanInterfaces()
        formatted_interfaces = []
        for i in interfaces:
            if len(i[1]) > 0:
                interface = "%s - %s" % (i[0], i[1])
            else:
                interface = i[0]
            formatted_interfaces.append(interface)
        self.comboBoxAdresses.addItems(formatted_interfaces)