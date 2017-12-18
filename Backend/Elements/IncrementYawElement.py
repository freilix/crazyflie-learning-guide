import time
from Backend.Elements.Element import Element
from Backend.GlobalPosition import GlobalPosition as GP

@Element.register
class IncrementYawElement(Element):
    def __init__(self, offsetYaw):
        Element.__init__(self)
        self.positionYaw = offsetYaw
        self.time = 5

    def run(self, cf):
        hilf = GP.PositionYaw
        hilf += self.positionYaw
        hilf = hilf % 360
        GP.PositionYaw = hilf
        time.sleep(self.time)