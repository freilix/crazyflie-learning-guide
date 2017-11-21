from FirstCfTest import Element

sequenceList = []

class sequenceList():
    def add(element):
        if not isinstance(element, Element):
            raise AttributeError("Parameter element is no instance of Element")
        sequenceList.append(element)

    def addOnPosition(element, position):
        if not isinstance(element, Element):
            raise AttributeError("Parameter element is no instance of Element")
        sequenceList.insert(position, element)

    def removePosition(position):
        sequenceList.__delitem__(position) #TODO slice or remove only one element?

    def getSequence(self):
        return sequenceList