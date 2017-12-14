import time

from Backend.Elements.Element import Element


@Element.register
class IncrementXElement(Element):
    def __init__(self):
        Element.__init__(self)

    def run(self, crazyflie):
        cf = crazyflie

        for i in range(50):
            print(i)
            time.sleep(0.1)