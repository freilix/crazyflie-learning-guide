from threading import Thread
import sys
from PyQt5.QtWidgets import QApplication
from Frontend.MainWindow import MainWindow


def initMainWindowApplication():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


uiThread = Thread(target=initMainWindowApplication)
uiThread.start()
