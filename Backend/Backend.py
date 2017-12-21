import time
import cflib.crtp
from threading import Thread
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from Backend.ResetEstimator import ResetEstimator
from Backend.GlobalPosition import GlobalPosition as GP
from cflib.crazyflie.log import LogConfig

def ScanInterfaces():
    cflib.crtp.init_drivers()
    time.sleep(1)
    available = cflib.crtp.scan_interfaces()
    return available

def ConnectToCrazyflie(interface):
    syncCrazyflie = SyncCrazyflie(interface)
    time.sleep(1)
    syncCrazyflie.open_link()
    #ResetEstimator.reset_estimator(syncCrazyflie)
    return syncCrazyflie

def PlayAndSendSequence(scf, list):
    if GP.IsPositionChangerRunning or GP.IsPositionChangerRunning:
        return

    GP.IsPositionChangerRunning = True
    GP.IsPositionSenderRunning = True
    ResetEstimator.reset_estimator(scf)
    ChangePositionCoordinates(list)
    SendCoordinatesToCrazyflie(scf)

def ChangePositionCoordinates(list):
    def runList(list):
        print('PositionCHANGERRunning')
        list.run(1) #todo remove 1
        time.sleep(1)
        GP.IsPositionChangerRunning = False
    #if GP.IsPositionChangerRunning:
    #    return
    #GP.IsPositionChangerRunning = True
    threadListRunner = Thread(target=runList, args=(list, ))
    threadListRunner.start()
    #return threadListRunner

def SendCoordinatesToCrazyflie(syncCrazyflie):
    def sendGlobalPosition(cf):
        print('PositionSENDERRunning')
        cf.param.set_value('flightmode.posSet', '1')
        while GP.IsPositionChangerRunning:
            cf.commander.send_setpoint(GP.PositionY, GP.PositionX, GP.PositionYaw, int(GP.PositionZ * 1000))
            print(GP.PositionX.__str__() + ", " + GP.PositionY.__str__() + ", " + GP.PositionZ.__str__() + ", " + GP.PositionYaw.__str__())
            time.sleep(0.1)
        cf.commander.send_setpoint(0, 0, 0, 0)
        GP.IsPositionSenderRunning = False
    #if GP.IsPositionSenderRunning:
    #    return
    #GP.IsPositionSenderRunning = True
    threadGlobalPosition = Thread(target=sendGlobalPosition, args=(syncCrazyflie.cf,))
    threadGlobalPosition.start()
    #return threadGlobalPosition

def start_position_printing(scf):
    def position_callback(timestamp, data, logconf):
        x = data['kalman.stateX']
        y = data['kalman.stateY']
        z = data['kalman.stateZ']
        print('pos: ({}, {}, {})'.format(x, y, z))
    log_conf = LogConfig(name='Position', period_in_ms=400)
    log_conf.add_variable('kalman.stateX', 'float')
    log_conf.add_variable('kalman.stateY', 'float')
    log_conf.add_variable('kalman.stateZ', 'float')

    scf.cf.log.add_config(log_conf)
    log_conf.data_received_cb.add_callback(position_callback)
    log_conf.start()