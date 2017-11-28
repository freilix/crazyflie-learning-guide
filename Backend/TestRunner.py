import time
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from Backend.SequenceList import SequenceList
from Backend.PositionMoverElement import PositionMoverElement
import cflib.crtp
from Backend.ResetEstimator import ResetEstimator

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
    syncCrazyflie.param.set_value('flightmode.posSet', '1')
    print("flightmode set")

    moveElement1 = PositionMoverElement(0.5, 0.5, 1)
    sList = SequenceList()
    sList.add(moveElement1)
    sList.run(syncCrazyflie)