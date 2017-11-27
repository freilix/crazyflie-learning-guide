from Backend.Element import Element
from cflib.crazyflie import Crazyflie

@Element.register
class PositionMoverElement(Element):
    def __init__(self, pOffsetX, pOffsetY, pOffsetZ):
        Element.__init__(self)
        self.positionX = pOffsetX
        self.positionY = pOffsetY
        self.positionZ = pOffsetZ

    def run(self, crazyflie):
        cf = crazyflie
        cf.commander.send_setpoint(self.positionX, self.positionY, self.positionZ, 0)

    #Element.register