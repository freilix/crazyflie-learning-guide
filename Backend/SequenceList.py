from Backend.Elements.Element import Element
from Backend.GlobalPosition import GlobalPosition as GP

#sequenceList = []

class SequenceList():
    def __init__(self):
        self.sequenceList = []

    def add(self, element):
        if not isinstance(element, Element):
            raise AttributeError("Parameter element is no instance of Element")
        self.sequenceList.append(element)

    def addOnPosition(self, element, position):
        if not isinstance(element, Element):
            raise AttributeError("Parameter element is no instance of Element")
            self.sequenceList.insert(position, element)

    def removePosition(self, position):
        self.sequenceList.__delitem__(position)  # TODO slice or remove only one element?

    def getSequence(self):
        return self.sequenceList

    def run(self, cf):
        for element in self.sequenceList:
            print("x: " + GP.PositionX.__str__() + ", y: "+ GP.PositionY.__str__() + ", z: "+ GP.PositionZ.__str__() + ", yaw: "+ GP.PositionYaw.__str__())
            element.run(cf)