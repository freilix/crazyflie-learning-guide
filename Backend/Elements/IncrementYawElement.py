import time

from Backend.Elements.Element import Element


@Element.register
class IncrementYawElement(Element):
    def __init__(self, offsetYaw):
        Element.__init__(self)
        self.positionX = offsetYaw

    def run(self, crazyflie):
        cf = crazyflie

        for i in range(50):
            print(i)
            time.sleep(0.1)