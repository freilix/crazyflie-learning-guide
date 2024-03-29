import time
import cflib.crtp
from Backend.Elements.PositionMoverElement import PositionMoverElement
from Backend.Elements.IncrementXElement import IncrementXElement
from Backend.Elements.IncrementYElement import IncrementYElement
from Backend.Elements.LandingElement import LandingElement
from Backend.Elements.IncrementZElement import IncrementZElement
from Backend.Elements.LoopElement import LoopElement
from Backend.Elements.IncrementYawElement import IncrementYawElement
from Backend.ResetEstimator import ResetEstimator
from Backend.SequenceList import SequenceList
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.log import LogConfig
from Backend.GlobalPosition import GlobalPosition as GP
from threading import Thread

class TestRunner():
    def sendGlobalPosition(cf):
        cf.param.set_value('flightmode.posSet', '1')
        while True:
            cf.commander.send_setpoint(GP.PositionY, GP.PositionX, GP.PositionYaw, int(GP.PositionZ * 1000))
            print(GP.PositionX.__str__() +", "+ GP.PositionY.__str__() + ", "+GP.PositionZ.__str__()  +", "+GP.PositionYaw.__str__() )
            time.sleep(0.1)
        cf.commander.send_setpoint(0, 0, 0, 0)

    def runList(list):
        print("thread")
        list.run(1)

    def position_callback(timestamp, data, logconf):
        x = data['kalman.stateX']
        y = data['kalman.stateY']
        z = data['kalman.stateZ']
        print('pos: ({}, {}, {})'.format(x, y, z))

    def start_position_printing(self, scf):
        log_conf = LogConfig(name='Position', period_in_ms=400)
        log_conf.add_variable('kalman.stateX', 'float')
        log_conf.add_variable('kalman.stateY', 'float')
        log_conf.add_variable('kalman.stateZ', 'float')

        scf.cf.log.add_config(log_conf)
        log_conf.data_received_cb.add_callback(self.position_callback)
        log_conf.start()

    print("start")

    innerLoop = SequenceList()
    innerLoop.add(IncrementZElement(0.5))
    innerLoop.add(IncrementZElement(-0.5))

    loopList = SequenceList()
    loopList.add(IncrementXElement(0.5))
    loopList.add(IncrementYawElement(90))
    loopList.add(IncrementYElement(0.5))
    loopList.add(IncrementYawElement(90))
    loopList.add(LoopElement(1, innerLoop))

    loopList.add(IncrementXElement(-0.5))
    loopList.add(IncrementYawElement(90))
    loopList.add(IncrementYElement(-0.5))
    loopList.add(IncrementYawElement(90))

    testList = SequenceList()
    testList.add(PositionMoverElement(1,2.5,1,0))

    testList.add(LoopElement(2, loopList))
    testList.add(IncrementYawElement(45))
    testList.add(IncrementXElement(0.5))
    testList.add(IncrementYElement(-1))
    testList.add(IncrementXElement(-0.5))
    testList.add(LandingElement())
    testList.add(IncrementZElement(0.5))
    testList.add(PositionMoverElement(1, 1, 1, 0))
    testList.add(LandingElement())
    #testList.add(IncrementZElement(0.5))
    #testList.add(IncrementYElement(0.5))
    #testList.add(IncrementYawElement(+30))

    cflib.crtp.init_drivers()
    time.sleep(1)
    available = cflib.crtp.scan_interfaces()
    time.sleep(1)
    syncCrazyflie = SyncCrazyflie(available[0][0])
    time.sleep(1)
    syncCrazyflie.open_link()
    ResetEstimator.reset_estimator(syncCrazyflie)

    start_position_printing(syncCrazyflie)

    syncCrazyflie.cf.param.set_value('flightmode.posSet', '1')

    threadListRunner = Thread(target=runList, args=(testList, ))
    threadListRunner.start()

    threadGlobalPosition = Thread(target=sendGlobalPosition, args=(syncCrazyflie.cf,))
    threadGlobalPosition.start()

