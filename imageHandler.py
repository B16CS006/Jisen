import pytesseract, numpy as np, cv2
from PIL import Image
import basic_functions
from boxes import Boxes

class Handler(Boxes):
    def __init__(self, database_dir='database', boxes=[[0,0,10,10],[10,10,10,10]], rate=2):
        Boxes.__init__(self, boxes, rate)
        self.__change_database_dir__(database_dir)
        self.change_image('1.jpg')
        return
   
    def __change_database_dir__(self, database_dir):
        self.__database_dir__ = basic_functions.check_dir(database_dir)
        return
    
    def __complete_filename__(self, filename):
        return self.__database_dir__ + filename

    def originalImage(self):
        return self.__current_image__

    def image(self):
        return self.__current_image__.copy()

    def imageAt(self, position):
        x, y = self.getPoint(position)
        length, height = self.getDimen(position)

        return self.originalImage()[x:x+length, y:y+height].copy()

    def change_image(self, image_name, from_database=True):
        if from_database:
            image_name = self.__complete_filename__(image_name)
        self.__current_image__ = cv2.imread(image_name)
        return

    def show(self, title='image'):
        image = self.image()
        self.draw(image)
        cv2.imshow(title, image)
        cv2.waitKey(0)
        return

    def showImage(self, image, title='showImage'):
        cv2.imshow(title, image)
        cv2.waitKey(0)
        return

    def destroy(self):
        cv2.destroyAllWindows()
        return

    def draw(self, img):
        for i in range(self.boxCount()):
            pt = self.getPoint(i)
            dim = self.getDimen(i)
            cv2.rectangle(img, pt, tuple(np.array(pt) + np.array(dim)), (255,0,0), 3)       
