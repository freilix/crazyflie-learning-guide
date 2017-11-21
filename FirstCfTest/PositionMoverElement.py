from FirstCfTest import SimpleElement
from cflib.crazyflie import Crazyflie

@SimpleElement.register
class PositionMoverElement(SimpleElement):
    def __init__(self, pOffsetX, pOffsetY, pOffsetZ):
        self.offsetX = pOffsetX
        self.offsetY = pOffsetY
        self.offsetZ = pOffsetZ

    def run(self, crazyflie):
        cf = crazyflie
        cf.commander.send_setpoint()