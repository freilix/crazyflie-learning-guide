from Backend import Element
from Backend import LoopElement
from Backend import SimpleElement
import time
import cflib.crtp
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger
from Backend import SequenceList

uri = 'radio://0/80/250K' #TODO available = cflib.crtp.scan_interfaces()
sequenceList = SequenceList()

def run_sequence(scf, sequence):
    cf = scf.cf
    sList = sequenceList.getSequence()
    for element in sList:
        element.run(cf)

cflib.crtp.init_drivers(enable_debug_driver=False)
with SyncCrazyflie(uri) as scf:
    run_sequence(scf, sequenceList)