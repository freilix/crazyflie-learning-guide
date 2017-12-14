import time
import cflib.crtp
from Backend.Elements.PositionMoverElement import PositionMoverElement
from Backend.Elements.IncrementXElement import IncrementXElement
from Backend.Elements.IncrementYElement import IncrementYElement
from Backend.Elements.IncrementZElement import IncrementZElement
from Backend.Elements.LoopElement import LoopElement
from Backend.Elements.IncrementYawElement import IncrementYawElement
from Backend.ResetEstimator import ResetEstimator
from Backend.SequenceList import SequenceList
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from Backend.GlobalPosition import GlobalPosition as GP
from threading import Thread

class TestRunner():
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

    loopList = SequenceList()
    loopList.add(IncrementXElement(0.5))
    loopList.add(IncrementYElement(0.5))
    loopList.add(IncrementXElement(-0.5))
    loopList.add(IncrementYElement(-0.5))

    testList = SequenceList()
    testList.add(PositionMoverElement(1,2.5,1,0))
    testList.add(LoopElement(3, loopList))
    testList.add(IncrementYawElement(-30))
    testList.add(IncrementXElement(0.5))
    testList.add(IncrementYElement(-1))
    testList.add(IncrementXElement(-0.5))
    testList.add(IncrementZElement(0.5))
    testList.add(IncrementYElement(0.5))
    testList.add(IncrementYawElement(0))

    cflib.crtp.init_drivers()
    available = cflib.crtp.scan_interfaces()
    syncCrazyflie = SyncCrazyflie(available[0][0])
    syncCrazyflie.open_link()
    ResetEstimator.reset_estimator(syncCrazyflie)
    syncCrazyflie.cf.param.set_value('flightmode.posSet', '1')

    threadListRunner = Thread(target=runList, args=(testList, ))
    threadListRunner.start()

    threadGlobalPosition = Thread(target=sendGlobalPosition, args=(syncCrazyflie.cf,))
    threadGlobalPosition.start()

