from Backend.Elements.Element import Element

@Element.register
class LoopElement(Element):
    def __init__(self):
        self.elementList = []
        self.counts = 0

    def run(self, crazyflie):
        for e in self.elementList:
            e.run(crazyflie)