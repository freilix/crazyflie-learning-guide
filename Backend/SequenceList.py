from Backend.Elements.Element import Element

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
            element.run(cf)