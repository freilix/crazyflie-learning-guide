import time
import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from Backend.ResetEstimator import ResetEstimator

def ScanInterfaces():
    cflib.crtp.init_drivers()
    time.sleep(1)
    available = cflib.crtp.scan_interfaces()
    return available

def ConnectToCrazyflie(interface):
    syncCrazyflie = SyncCrazyflie(interface)
    time.sleep(1)
    syncCrazyflie.open_link()
    ResetEstimator.reset_estimator(syncCrazyflie)
    return syncCrazyflie