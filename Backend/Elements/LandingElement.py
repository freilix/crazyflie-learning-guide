import time
from Backend.GlobalPosition import GlobalPosition as GP
from Backend.Elements.Element import Element


@Element.register
class LandingElement(Element):
    def __init__(self):
        Element.__init__(self)

    def run(self, crazyflie):
        cf = crazyflie
        for i in range(50):
            GP.PositionZ *= 0.95
            time.sleep(0.1)
        GP.PositionZ = 0