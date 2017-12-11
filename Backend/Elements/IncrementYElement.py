import time

from Backend.Elements.Element import Element


@Element.register
class IncrementYElement(Element):
    def __init__(self, offsetY):
        Element.__init__(self)
        self.positionX = offsetY

    def run(self, crazyflie):
        cf = crazyflie

        for i in range(50):
            print(i)
            time.sleep(0.1)