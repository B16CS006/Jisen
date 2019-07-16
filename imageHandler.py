import cv2
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
    def __init__(self, database_dir='database', selected_box_color=(225, 0, 0), unselected_box_color=(0, 255, 0),
                 rate=2):

        Boxes.__init__(self, rate)
        self.selected_box = 0
        self.set_select_box = 0
        self.selected_box_color = selected_box_color
        self.unselected_box_color = unselected_box_color
        self.database_dir = database_dir
        self.set_image('2.jpeg')

    @property
    def selected_box(self):
        return self._selected_box

    @selected_box.setter
    def selected_box(self, box_number):
        if 0 <= box_number < self.boxCount():
            self._selected_box = box_number
        else:
            self._selected_box = 0

    @property
    def unselected_box_color(self):
        return self._unselected_box_color

    @property
    def selected_box_color(self):
        return self._selected_box_color

    @unselected_box_color.setter
    def unselected_box_color(self, color):
        if isinstance(color, tuple):
            self._unselected_box_color = color

    @selected_box_color.setter
    def selected_box_color(self, color):
        if isinstance(color, tuple):
            self._selected_box_color = color

    @property
    def database_dir(self):
        return self.__database_dir__

    @database_dir.setter
    def database_dir(self, database_dir):
        self.__database_dir__ = basic_functions.check_dir(database_dir)

    @property
    def _image(self):
        return self._current_image

    @_image.setter
    def _image(self, image_name):
        if isinstance(image_name, str):
            self._current_image = cv2.imread(image_name)
            self._current_image_name = image_name
        else:
            pass
            # self._current_image = image_name

    def get_image(self):
        return self._image.copy()

    def get_image_name(self):
        return self._current_image_name

    def set_image(self, image_name, from_database=True):
        if from_database:
            image_name = self.__complete_filename__(image_name)
        self._image = image_name

    def image_at_box(self, position):
        x, y, length, height = self.getBox(position).box
        return self._image[y:y + height, x:x + length].copy()

    def select_next_box(self):
        if self.boxCount() > 0:
            if 0 <= self.selected_box < self.boxCount():
                self.selected_box += 1
                self.selected_box %= self.boxCount()
            else:
                self.selected_box = 0

    def __complete_filename__(self, filename):
        return self.database_dir + filename

    def show_image(self, title='image'):
        image = self.get_image()
        self.draw_boxes(image)
        show_image(image, title)
        return

    def draw_boxes(self, img):
        for i in range(self.boxCount()):
            box = self.getBox(i)
            if i == self.selected_box:
                color = self.selected_box_color
            else:
                color = self.unselected_box_color
            cv2.rectangle(img, box.point, (box.x + box.length, box.y + box.height), color, self.box_width)

    def read_image(self, image=None):
        if image is None:
            image = self.get_image()
        elif isinstance(image, int):
            image = self.image_at_box(image)

        if image is None or isinstance(image, str):
            return None

        # destroy()
        # show_image(image, 'Box')

        return image_to_string(image)
