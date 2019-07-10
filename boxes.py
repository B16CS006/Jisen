
class Boxes:
    def __init__(self, boxes=[], rate=2):
        self.__boxes__ = boxes
        self.rate = rate
        return

    def addBox(self, box=[0,0,0,0]):
        self.__boxes__.append(box)
        return

    def boxCount(self):
        return len(self.__boxes__)

    def getBoxes(self):
        return self.__boxes__.copy()

    def setBoxes(self, boxes):
        self.__boxes__ = boxes
        return

    def getRate(self):
        return self.__rate__

    def setRate(self, rate):
        self.__rate__ = rate
        return

    def incRate(self, value=1):
        self.__rate__ += value 
        return

    def decRate(self, value=1):
        self.__rate__ += value
        return

    def getBox(self, position):
        if position < self.boxCount() and position >= 0:
            box = self.__boxes__[position]
            return box[0], box[1], box[2], box[3]
        else:
            return None, None, None, None

    def getPoint(self, position):
        x, y, _, _ = self.getBox(position)
        return x, y

    def getDimen(self, position):
        _, _, length, height = self.getBox(position)
        return length, height
    
    def setBox(self, position, x=None, y=None, length=None, height=None):
        if x == None:
            x, _ = self.getPoint(position)
        if y == None:
            _, y = self.getPoint(position)
        if length == None:
            length, _ = self.getDimen(position)
        if height == None:
            _, height = self.getDimen(position)

        self.__boxes__[position] = [x, y, length, height]
        return

    def setPoint(self, position, x=None, y=None):
        self.setBox(position, x, y, None, None)
        return

    def setDimen(self, position, length=None, height=None):
        self.setBox(position, None, None, length, height)
        return

    def incX(self, position, by=None):
        if by == None:
            by = self.rate
        oldValue, _ = self.getPoint(position)
        self.setPoint(position, oldValue + by, None)

    def decX(self, position, by=None):
        if by == None:
            by = self.rate
        oldValue, _ = self.getPoint(position)
        self.setPoint(position, oldValue - by, None)

    def incY(self, position, by=None):
        if by == None:
            by = self.rate
        _, oldValue = self.getPoint(position)
        self.setPoint(position, None, oldValue + by)

    def decY(self, position, by=None):
        if by == None:
            by = self.rate
        _, oldValue = self.getPoint(position)
        self.setPoint(position, None, oldValue - by)

    def incLength(self, position, by=None):
        if by == None:
            by = self.rate
        oldValue, _ = self.getDimen(position)
        self.setDimen(position, oldValue + by, None)

    def decLength(self, position, by=None):
        if by == None:
            by = self.rate
        oldValue, _ = self.getDimen(position)
        self.setDimen(position, oldValue - by, None)

    def incHeight(self, position, by=None):
        if by == None:
            by = self.rate
        _, oldValue = self.getDimen(position)
        self.setDimen(position, None, oldValue + by)

    def decHeight(self, position, by=None):
        if by == None:
            by = self.rate
        _, oldValue = self.getDimen(position)
        self.setDimen(position, None, oldValue - by)
