from box import Box


class Boxes:

    def __init__(self, rate=2, box_width=2):
        self.boxes = []
        self.box_width = box_width
        self.rate = rate

    def _get_box_width(self):
        return self._box_width

    def _set_box_width(self, width):
        self._box_width = width

    def _get_rate(self):
        return self._rate

    def _set_rate(self, rate):
        if not isinstance(rate, int) or rate <= 0:
            self._rate = 1
        else:
            self._rate = rate

    def _get_boxes(self):
        return self._boxes

    def _set_boxes(self, boxes):
        if boxes is None:
            boxes = []
        elif not isinstance(boxes, list):
            boxes = []
        self._boxes = boxes

    box_width = property(_get_box_width, _set_box_width)
    rate = property(_get_rate, _set_rate)
    boxes = property(_get_boxes, _set_boxes)

    def addBox(self, box=None):
        if box is None:
            box = []
        self.boxes.append(Box(box))

    def boxCount(self):
        return len(self._boxes)

    def incRate(self, value=1):
        self.rate += value
        return

    def decRate(self, value=1):
        self.rate -= value
        return

    def getBox(self, position):
        if self.boxCount() > position >= 0:
            return self.boxes[position]
        else:
            print('Index Out of Range')

    def setBox(self, position, x=None, y=None, length=None, height=None):
        self.getBox(position).box = x, y, length, height

    def setPoint(self, position, x=None, y=None):
        self.getBox(position).point = x, y

    def setDimen(self, position, length=None, height=None):
        self.getBox(position).dimension = length, height

    def incX(self, position, by=None):
        if by is None:
            by = self.rate
        self.getBox(position).inc_x(by)

    def decX(self, position, by=None):
        if by is None:
            by = self.rate
        self.getBox(position).dec_x(by)

    def incY(self, position, by=None):
        if by is None:
            by = self.rate
        self.getBox(position).inc_y(by)

    def decY(self, position, by=None):
        if by is None:
            by = self.rate
        self.getBox(position).dec_y(by)

    def incLength(self, position, by=None):
        if by is None:
            by = self.rate
        self.getBox(position).inc_length(by)

    def decLength(self, position, by=None):
        if by is None:
            by = self.rate
        self.getBox(position).dec_length(by)

    def incHeight(self, position, by=None):
        if by is None:
            by = self.rate
        self.getBox(position).inc_height(by)

    def decHeight(self, position, by=None):
        if by is None:
            by = self.rate
        self.getBox(position).dec_height(by)
