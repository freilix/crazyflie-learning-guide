from Backend.Element import Element
from cflib.crazyflie import Crazyflie

@Element.register
class PositionMoverElement(Element):
    def __init__(self, pPositionX, pPositionY, pPositionZ):
        Element.__init__(self)
        self.positionX = pPositionX
        self.positionY = pPositionY
        self.positionZ = pPositionZ

    def run(self, crazyflie):
        cf = crazyflie
        cf.commander.send_setpoint(self.positionX, self.positionY, self.positionZ, 0)

    #Element.register