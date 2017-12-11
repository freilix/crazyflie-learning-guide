import time
from Backend.Elements.Element import Element
from Backend.GlobalPosition import GlobalPosition as GP

@Element.register
class IncrementYawElement(Element):
    def __init__(self, offsetYaw):
        Element.__init__(self)
        self.positionYaw = offsetYaw

    def run(self, cf):
        GP.PositionYaw += self.positionYaw
        time.sleep(5)