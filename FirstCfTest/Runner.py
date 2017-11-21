import time
from cflib.crazyflie import Crazyflie
from cflib.crazyflie import Commander
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.log import LogConfig
import cflib.crtp

class Runner():
    def crazyflie_disconnected(a):
        print("cf disconnected")
    def crazyflie_connected(a):
        print("cf connected")
    def crazyflie_connection_lost(aa,a):
        print("cf connection_lost")
    def crazyflie_packet_received (a):
        print("cf packet_received")
    def crazyflie_connection_failed(a,aa):
        print("cf connection_failed")
    def crazyflie_packet_sent(a):
        print("cf packet_sent")

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
    #firstInterface = available[0][0]
    crazyflie = Crazyflie()
    crazyflie.connected.add_callback(crazyflie_connected)
    crazyflie.disconnected.add_callback(crazyflie_disconnected)
    crazyflie.connection_lost.add_callback(crazyflie_connection_lost)
    crazyflie.connection_failed.add_callback(crazyflie_connection_failed)
    crazyflie.packet_received.add_callback(crazyflie_packet_received)
    crazyflie.packet_sent.add_callback(crazyflie_packet_sent)
    crazyflie.open_link(available[0][0])
    status = crazyflie.state
    #crazyflie.console

    commander = Commander(crazyflie)
    commander.send_setpoint(0.0,0.0,0,30000)
    commander.send_setpoint(0.0,0.0,0,30000)
    commander.send_setpoint(0.0,0.0,0,30000)
    commander.send_setpoint(0.0,0.0,0,30000)
    commander.send_setpoint(0.0,0.0,0,50000)
    commander.send_setpoint(0.0,0.0,0,60000)
    commander.send_setpoint(0.0,0.0,0,60000)
    commander.send_setpoint(0.0,0.0,0,30000)
    commander.send_setpoint(0.0,0.0,0,40000)

    sequence = [
        (2.5, 2.5, 1.2, 0),
        (1.5, 2.5, 1.2, 0),
        (2.5, 2.0, 1.2, 0),
        (3.5, 2.5, 1.2, 0),
        (2.5, 3.0, 1.2, 0),
        (2.5, 2.5, 1.2, 0),
        (2.5, 2.5, 0.4, 0),
    ]
    syncCrazyflie = SyncCrazyflie()
    run_sequence(syncCrazyflie, sequence)