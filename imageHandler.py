import cv2
import numpy as np
from pytesseract import image_to_string

import basic_functions
from boxes import Boxes


def show_image(image, title='showImage'):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    return


def destroy():
    cv2.destroyAllWindows()
    return


class ImageHandler(Boxes):
    __selected_box__: int
    __selected_box_color__: tuple
    __unselected_box_color__: tuple

    def __init__(self, database_dir='database', selected_box_color=(225, 0, 0), unselected_box_color=(0, 255, 0),
                 boxes=None, rate=2):
        if boxes is None:
            boxes = []

        Boxes.__init__(self, boxes, rate)

        self.__current_image__ = None
        self.__selected_box__ = 0
        self.select_box()
        self.set_selected_box_color(selected_box_color)
        self.set_unselected_box_color(unselected_box_color)
        self.__change_database_dir__(database_dir)
        self.change_image('1.jpg')
        return

    def get_selected_box(self):
        return self.__selected_box__

    def select_box(self, box_number=0):
        if 0 <= box_number < self.boxCount():
            self.__selected_box__ = box_number

    def select_next_box(self):
        if self.boxCount() > 0:
            if 0 <= self.get_selected_box() < self.boxCount():
                self.select_box((self.get_selected_box() + 1) % self.boxCount())
            else:
                self.select_box(0)

    def set_unselected_box_color(self, color):
        self.__unselected_box_color__ = color

    def set_selected_box_color(self, color):
        self.__selected_box_color__ = color
        return

    def get_unselected_box_color(self):
        return self.__unselected_box_color__

    def get_selected_box_color(self):
        return self.__selected_box_color__

    def __change_database_dir__(self, database_dir):
        self.__database_dir__ = basic_functions.check_dir(database_dir)
        return

    def __complete_filename__(self, filename):
        return self.__database_dir__ + filename

    def original_image(self):
        return self.__current_image__

    def image(self):
        return self.__current_image__.copy()

    def image_at_box(self, position):
        x, y, length, height = self.getBox(position)
        return self.original_image()[y:y + height, x:x + length].copy()

    def change_image(self, image_name, from_database=True):
        if from_database:
            image_name = self.__complete_filename__(image_name)
        self.__current_image__ = cv2.cvtColor(cv2.imread(image_name), cv2.COLOR_BGR2RGB)
        return

    def show(self, title='image'):
        image = self.image()
        self.drawBoxes(image)
        show_image(image, title)
        return

    def drawBoxes(self, img):
        for i in range(self.boxCount()):
            pt = self.getPoint(i)
            dim = self.getDimen(i)
            if i == self.get_selected_box():
                color = self.get_selected_box_color()
            else:
                color = self.get_unselected_box_color()
            cv2.rectangle(img, pt, tuple(np.array(pt) + np.array(dim)), color, self.getBoxWidth())

    def read_image(self, image=None):
        if image is None:
            image = self.image()
        elif isinstance(image, int):
            image = self.image_at_box(image)

        if image is None or isinstance(image, str):
            return None
        return image_to_string(image)
