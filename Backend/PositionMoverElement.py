import time
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

        for i in range(50):
            cf.commander.send_setpoint(self.positionY, self.positionX, 0, int(self.positionZ * 1000))
            print(i)
            time.sleep(0.1)

    #Element.register