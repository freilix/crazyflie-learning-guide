from threading import Thread
import time
import socket
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append("/Elements/PositionMoverElement")
sys.path.append("/Elements/")
sys.path.append("../Elements/")
sys.path.append("/Backend/")
sys.path.append("/Backend/Elements")
sys.path.append("C:/Users/Felix/Documents/Git/crazyflie-learning/Backend")
sys.path.append("C:/Users/Felix/Documents/Git/crazyflie-learning/Backend/Elements/PositionMoverElement")
sys.path.append("C:/Users/Felix/Documents/Git/crazyflie-learning/Backend/Elements/")
sys.path.append("/Backend/Elements/PositionMoverElement")
from Backend.Elements.PositionMoverElement import PositionMoverElement
from Backend.Elements.IncrementXElement import IncrementXElement
from Backend.Elements.IncrementYElement import IncrementYElement
from Backend.Elements.IncrementZElement import IncrementZElement
from Backend.Elements.IncrementYawElement import IncrementYawElement
from Backend.ResetEstimator import ResetEstimator
import cflib.crtp
from Backend.SequenceList import SequenceList
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from Backend.GlobalPosition import GlobalPosition as GP


class PythonRunner():
    def sendGlobalPosition(cf):
        cf.param.set_value('flightmode.posSet', '1')
        while True:
            cf.commander.send_setpoint(GP.PositionY, GP.PositionX, GP.PositionYaw, int(GP.PositionZ * 1000))
            time.sleep(0.1)
        cf.commander.send_setpoint(0, 0, 0, 0)

    def runList(list):
        print("thread")
        list.run(1)


    print("start")
    HOST = "localhost"
    PORT = 9050
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        print(data.decode('utf-8'))


    cflib.crtp.init_drivers()
    time.sleep(1)
    available = cflib.crtp.scan_interfaces()
    time.sleep(2)
    syncCrazyflie = SyncCrazyflie(available[0][0])
    syncCrazyflie.open_link()
    ResetEstimator.reset_estimator(syncCrazyflie)
    syncCrazyflie.cf.param.set_value('flightmode.posSet', '1')

    threadListRunner = Thread(target=runList, args=(testList, ))
    threadListRunner.start()

    threadGlobalPosition = Thread(target=sendGlobalPosition, args=(syncCrazyflie.cf,))
    threadGlobalPosition.start()

