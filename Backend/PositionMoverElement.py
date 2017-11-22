from Backend import Element
from cflib.crazyflie import Crazyflie

@Element.register
class PositionMoverElement(Element):
    def __init__(self, pOffsetX, pOffsetY, pOffsetZ):
        self.offsetX = pOffsetX
        self.offsetY = pOffsetY
        self.offsetZ = pOffsetZ

    def run(self, crazyflie):
        cf = crazyflie
        cf.commander.send_setpoint()