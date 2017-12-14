import time
from Backend.Elements.Element import Element
from Backend.GlobalPosition import GlobalPosition as GP

@Element.register
class IncrementZElement(Element):
    def __init__(self, offsetZ):
        Element.__init__(self)
        self.positionZ = offsetZ

    def run(self, cf):
        GP.PositionZ += self.positionZ
        time.sleep(5)