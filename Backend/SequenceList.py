from Backend.Elements.Element import Element
from Backend.GlobalPosition import GlobalPosition as GP

sequenceList = []

class SequenceList():
    def add(self, element):
        if not isinstance(element, Element):
            raise AttributeError("Parameter element is no instance of Element")
        sequenceList.append(element)

    def addOnPosition(self, element, position):
        if not isinstance(element, Element):
            raise AttributeError("Parameter element is no instance of Element")
        sequenceList.insert(position, element)

    def removePosition(self, position):
        sequenceList.__delitem__(position) #TODO slice or remove only one element?

    def getSequence(self):
        return sequenceList

    def run(self, cf):
        for element in sequenceList:
            print("x: " + GP.PositionX.__str__() + ", y: "+ GP.PositionY.__str__() + ", z: "+ GP.PositionZ.__str__() + ", yaw: "+ GP.PositionYaw.__str__())
            element.run(cf)