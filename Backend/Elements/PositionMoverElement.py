import time

from Backend.Elements.Element import Element


@Element.register
class PositionMoverElement(Element):
    def __init__(self, pPositionX, pPositionY, pPositionZ, pYaw):
        Element.__init__(self)
        self.positionX = pPositionX
        self.positionY = pPositionY
        self.positionZ = pPositionZ
        self.yaw = pYaw

    def run(self, crazyflie):
        cf = crazyflie

        for i in range(50):
            cf.commander.send_setpoint(self.positionY, self.positionX, self.yaw, int(self.positionZ * 1000))
            print(i)
            time.sleep(0.1)