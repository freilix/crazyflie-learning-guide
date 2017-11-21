import Element
import LoopElement
import SimpleElement
import time
import cflib.crtp
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger
import SequenceList

uri = 'radio://0/80/2M' #TODO
sequenceList = SequenceList()

def reset_estimator(scf):
    cf = scf.cf

def run_sequence(scf, sequence):
    cf = scf.cf
    sList = sequenceList.getSequence()

cflib.crtp.init_drivers(enable_debug_driver=False)
#TODO available = cflib.crtp.scan_interfaces()
with SyncCrazyflie(uri) as scf:
    reset_estimator(scf)
    run_sequence(scf, sequenceList)