import time

from Backend.Elements.Element import Element


@Element.register
class IncrementZElement(Element):
    def __init__(self, offsetZ):
        Element.__init__(self)
        self.positionX = offsetZ

    def run(self, crazyflie):
        cf = crazyflie

        for i in range(50):
            print(i)
            time.sleep(0.1)