import time
from Backend.Elements.Element import Element
from Backend.GlobalPosition import GlobalPosition as GP

@Element.register
class IncrementYElement(Element):
    def __init__(self, offsetY):
        Element.__init__(self)
        self.positionY = offsetY
        self.time = 5

    def run(self, cf):
        GP.PositionY += self.positionY
        time.sleep(self.time)