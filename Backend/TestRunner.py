import time

import cflib.crtp
from Backend.Elements.PositionMoverElement import PositionMoverElement
from Backend.Elements.IncrementXElement import IncrementXElement
from Backend.Elements.IncrementYElement import IncrementYElement
from Backend.Elements.IncrementZElement import IncrementZElement
from Backend.Elements.IncrementYawElement import IncrementYawElement
from Backend.ResetEstimator import ResetEstimator
from Backend.SequenceList import SequenceList
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from Backend.GlobalPosition import GlobalPosition as GP
from threading import Thread

class TestRunner():
    def run_sequence(scf, sequence):
        cf = scf.cf
        cf.param.set_value('flightmode.posSet', '1')

        for position in sequence:
            print('Setting position {}'.format(position))
            for i in range(50):
                cf.commander.send_setpoint(position[1], position[0],
                                           position[3],
                                           int(position[2] * 1000))
                time.sleep(0.1)

        cf.commander.send_setpoint(0, 0, 0, 0)
        # Make sure that the last packet leaves before the link is closed
        # since the message queue is not flushed before closing
        time.sleep(0.1)

    print("start")

    cflib.crtp.init_drivers()
    available = cflib.crtp.scan_interfaces()
    print(available)

    syncCrazyflie = SyncCrazyflie(available[0][0])
    syncCrazyflie.open_link()

    ResetEstimator.reset_estimator(syncCrazyflie)

    print("set flightmode")
    syncCrazyflie.cf.param.set_value('flightmode.posSet', '1')
    print("flightmode set")

    moveElement1 = PositionMoverElement(1, 1, 1)
    moveElement2 = PositionMoverElement(1, 2, 1)
    sList = SequenceList()
    sList.add(moveElement1)
    sList.add(moveElement2)
    sList.run(syncCrazyflie.cf)