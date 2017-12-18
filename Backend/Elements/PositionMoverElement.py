import time

from Backend.Elements.Element import Element
from Backend.GlobalPosition import GlobalPosition as GP


@Element.register
class PositionMoverElement(Element):
    def __init__(self, pPositionX, pPositionY, pPositionZ, pYaw):
        Element.__init__(self)
        self.positionX = pPositionX
        self.positionY = pPositionY
        self.positionZ = pPositionZ
        self.yaw = pYaw
        self.time = 5

    def run(self, crazyflie):
        GP.PositionX = self.positionX
        GP.PositionY = self.positionY
        GP.PositionZ = self.positionZ
        GP.PositionYaw = self.yaw
        time.sleep(self.time)