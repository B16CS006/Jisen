# noinspection PyAttributeOutsideInit
class Box:
    def __init__(self, box, label=''):
        print(type(box))
        self.box = box
        self.label = label

    @property
    def x(self):
        return self.__x__

    @property
    def y(self):
        return self.__y__

    @property
    def length(self):
        return self.__length__

    @property
    def height(self):
        return self.__height__

    @property
    def label(self):
        return self.__label__

    @property
    def point(self):
        return self.x, self.y

    @property
    def dimension(self):
        return self.length, self.height

    @x.setter
    def x(self, x):
        if not isinstance(x, int) or x < 0:
            self.__x__ = 0
        else:
            self.__x__ = x

    @y.setter
    def y(self, y):
        if not isinstance(y, int) or y < 0:
            self.__y__ = 0
        else:
            self.__y__ = y

    @length.setter
    def length(self, length):
        if not isinstance(length, int) or length < 0:
            self.__length__ = 0
        else:
            self.__length__ = length

    @height.setter
    def height(self, height):
        if not isinstance(height, int) or height < 0:
            self.__height__ = 0
        else:
            self.__height__ = height

    @label.setter
    def label(self, label):
        if label is None:
            label = ''
        self.__label__ = str(label)

    @point.setter
    def point(self, point):
        try:
            point = tuple(point)
        except TypeError:
            print("TypeError: Expecting <class 'tuple'> but", type(point), 'provided')
        try:
            self.x = point[0]
        except IndexError:
            self.x = None

        try:
            self.y = point[1]
        except IndexError:
            self.y = None

    @dimension.setter
    def dimension(self, dimension):
        try:
            dimension = tuple(dimension)
        except TypeError:
            print("TypeError: Expecting <class 'tuple'> but", type(dimension), 'provided')
        try:
            self.length = dimension[0]
        except IndexError:
            self.length = None

        try:
            self.height = dimension[1]
        except IndexError:
            self.height = None

    def get_box(self):
        return self.x, self.y, self.length, self.height

    def set_box(self, box):
        try:
            box = tuple(box)
        except TypeError:
            print("TypeError: Expecting <class 'tuple'> but", type(box), 'provided')
            return
        try:
            self.x = box[0]
        except IndexError:
            self.x = None

        try:
            self.y = box[1]
        except IndexError:
            self.y = None

        try:
            self.length = box[2]
        except IndexError:
            self.length = None

        try:
            self.height = box[3]
        except IndexError:
            self.height = None

        try:
            self.label = box[4]
        except IndexError:
            pass

    box = property(get_box, set_box)
