class Boxes:
    __rate__: int
    __box_width__: int

    def __init__(self, boxes=None, rate=2):
        if boxes is None:
            boxes = []
        self.__boxes__ = boxes
        self.setBoxWidth(2)
        self.setRate(rate)
        return

    def getBoxWidth(self):
        return self.__box_width__

    def setBoxWidth(self, width):
        self.__box_width__ = width

    def addBox(self, box=None):
        if box is None:
            box = [0, 0, 0, 0]
        self.__boxes__.append(box)
        return

    def boxCount(self):
        return len(self.__boxes__)

    def getBoxes(self):
        return self.__boxes__.copy()

    def setBoxes(self, boxes=None):
        if boxes is None:
            boxes = []
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
        self.__rate__ -= value
        return

    def getBox(self, position):
        if self.boxCount() > position >= 0:
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
        if x is None:
            x, _ = self.getPoint(position)
        if y is None:
            _, y = self.getPoint(position)
        if length is None:
            length, _ = self.getDimen(position)
        if height is None:
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
        if by is None:
            by = self.getRate()
        old_value, _ = self.getPoint(position)
        self.setPoint(position, old_value + by, None)

    def decX(self, position, by=None):
        if by is None:
            by = self.getRate()
        old_value, _ = self.getPoint(position)
        new_value = old_value - by
        if new_value < 0:
            new_value = 0
        self.setPoint(position, new_value, None)

    def incY(self, position, by=None):
        if by is None:
            by = self.getRate()
        _, old_value = self.getPoint(position)
        self.setPoint(position, None, old_value + by)

    def decY(self, position, by=None):
        if by is None:
            by = self.getRate()
        _, old_value = self.getPoint(position)
        new_value = old_value - by
        if new_value < 0:
            new_value = 0
        self.setPoint(position, None, new_value)

    def incLength(self, position, by=None):
        if by is None:
            by = self.getRate()
        old_value, _ = self.getDimen(position)
        self.setDimen(position, old_value + by, None)

    def decLength(self, position, by=None):
        if by is None:
            by = self.getRate()
        old_value, _ = self.getDimen(position)
        new_value = old_value - by
        if new_value < 0:
            new_value = 0
        self.setDimen(position, new_value, None)

    def incHeight(self, position, by=None):
        if by is None:
            by = self.getRate()
        _, old_value = self.getDimen(position)
        self.setDimen(position, None, old_value + by)

    def decHeight(self, position, by=None):
        if by is None:
            by = self.getRate()
        _, old_value = self.getDimen(position)
        new_value = old_value - by
        if new_value < 0:
            new_value = 0
        self.setDimen(position, None, new_value)
