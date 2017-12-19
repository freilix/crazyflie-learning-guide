import time
from Backend.Elements.Element import Element
from Backend.GlobalPosition import GlobalPosition as GP

@Element.register
class IncrementXElement(Element):
    def __init__(self, offsetX):
        Element.__init__(self)
        self.positionX = offsetX
        self.time = 5

    def run(self, cf):
        GP.PositionX += self.positionX
        time.sleep(self.time)