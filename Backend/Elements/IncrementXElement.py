import time

from Backend.Elements.Element import Element


@Element.register
class IncrementXElement(Element):
    def __init__(self, offsetX):
        Element.__init__(self)
        self.positionX = offsetX

    def run(self, crazyflie):
        cf = crazyflie

        for i in range(50):
            print(i)
            time.sleep(0.1)