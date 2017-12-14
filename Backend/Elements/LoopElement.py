from Backend.Elements.Element import Element

@Element.register
class LoopElement(Element):
    def __init__(self, rounds, list):
        self.elementList = list
        self.counts = rounds

    def run(self, crazyflie):
        for x in range(0, self.counts):
            for e in self.elementList:
                e.run(crazyflie)