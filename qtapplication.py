import sys

import cv2
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QGridLayout, QLabel, QCheckBox, QPushButton, QSlider

import application


# noinspection PyAttributeOutsideInit
class Window(QtWidgets.QWidget, application.Application):

    def __init__(self):
        super(Window, self).__init__()
        application.Application.__init__(self, 'database')

        self.show_boxes = True
        self.boxes_visibility = True
        self.main_grid_layout = QGridLayout()
        self.image_control_box = QGroupBox('Image Control Box')
        self.image_show = QLabel(self)
        self.init_window()

    def init_window(self):
        self.setWindowIcon(QtGui.QIcon('configuration/Logo.jpeg'))
        self.setWindowTitle('Jisen')
        self.setGeometry(QRect(100, 100, 600, 400))
        self.ui_components()
        self.show()

    def ui_components(self):
        self.ui_image_control()
        self.image_control_box.setLayout(self.main_grid_layout)

        v_box_layout = QVBoxLayout()
        v_box_layout.addWidget(self.image_control_box)
        self.setLayout(v_box_layout)

    def ui_image_control(self):
        self.main_control_layout = QVBoxLayout()
        controller_group = QGroupBox('Controller')
        controller_group.setLayout(self.main_control_layout)
        self.main_grid_layout.addWidget(controller_group, 0, 0)

        self.ui_change_box_rate_control()
        self.ui_image_box_visibility_control()
        self.ui_change_box_control()
        self.ui_move_box_control()
        self.ui_change_box_dimension_control()
        self.set_image()

    def ui_change_box_rate_control(self):
        slider = QSlider()
        slider.setOrientation(Qt.Horizontal)
        slider.setFocusPolicy(Qt.NoFocus)
        slider.valueChanged[int].connect(self.change_box_rate)
        self.main_control_layout.addWidget(slider)

    def ui_image_box_visibility_control(self):
        # Boxes visibility
        boxes_visibility_check_box = QCheckBox('Boxes Visibility')
        boxes_visibility_check_box.toggle()
        boxes_visibility_check_box.stateChanged.connect(self.set_boxes_visibility)
        self.main_control_layout.addWidget(boxes_visibility_check_box)

    def ui_change_box_control(self):
        # change Boxes
        select_next_box_button = QtWidgets.QPushButton('Select Next Box', self)
        select_next_box_button.clicked.connect(self.select_next_box)
        select_next_box_button.setMinimumHeight(30)
        select_next_box_button.setMinimumHeight(30)
        self.main_control_layout.addWidget(select_next_box_button)

    def ui_move_box_control(self):
        # Boxes controller
        box_movement_group = QGroupBox('Box Movement')
        v_box_layout = QVBoxLayout()

        box_move_up_button = QPushButton('Up')
        box_move_left_button = QPushButton('Left')
        box_move_right_button = QPushButton('Right')
        box_move_down_button = QPushButton('Down')

        box_move_up_button.setMinimumHeight(30)
        box_move_up_button.setMaximumHeight(30)

        box_move_left_button.setMinimumHeight(30)
        box_move_left_button.setMaximumHeight(30)

        box_move_right_button.setMinimumHeight(30)
        box_move_right_button.setMaximumHeight(30)

        box_move_down_button.setMinimumHeight(30)
        box_move_down_button.setMaximumHeight(30)

        box_move_up_button.clicked.connect(self.move_box_up)
        box_move_down_button.clicked.connect(self.move_box_down)
        box_move_left_button.clicked.connect(self.move_box_left)
        box_move_right_button.clicked.connect(self.move_box_right)

        v_box_layout.addWidget(box_move_up_button)
        v_box_layout.addWidget(box_move_left_button)
        v_box_layout.addWidget(box_move_right_button)
        v_box_layout.addWidget(box_move_down_button)

        box_movement_group.setLayout(v_box_layout)
        self.main_control_layout.addWidget(box_movement_group)

    def ui_change_box_dimension_control(self):

        box_dimension_group = QGroupBox('Box Dimensions Control')
        v_box_layout = QVBoxLayout()

        box_inc_length = QPushButton('Length ^')
        box_dec_length = QPushButton('Length v')
        box_inc_height = QPushButton('Height ^')
        box_dec_height = QPushButton('Height v')

        box_inc_length.setMinimumHeight(30)
        box_inc_length.setMaximumHeight(30)

        box_dec_length.setMinimumHeight(30)
        box_dec_length.setMaximumHeight(30)

        box_inc_height.setMinimumHeight(30)
        box_inc_height.setMaximumHeight(30)

        box_dec_height.setMinimumHeight(30)
        box_dec_height.setMaximumHeight(30)

        box_inc_length.clicked.connect(self.inc_box_length)
        box_dec_length.clicked.connect(self.dec_box_length)
        box_inc_height.clicked.connect(self.inc_box_height)
        box_dec_height.clicked.connect(self.dec_box_height)

        v_box_layout.addWidget(box_inc_length)
        v_box_layout.addWidget(box_dec_length)
        v_box_layout.addWidget(box_inc_height)
        v_box_layout.addWidget(box_dec_height)

        box_dimension_group.setLayout(v_box_layout)
        self.main_control_layout.addWidget(box_dimension_group)

    def set_image(self, image=None):
        self.main_grid_layout.addWidget(self.image_show, 0, 1)
        if image is None:
            image = self.__image_handler__.image()
            if image is None:
                self.image_show.setText('No Image Found')
                return
        elif isinstance(image, str):
            image = cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2RGB)

        if self.boxes_visibility:
            self.__image_handler__.drawBoxes(image)

        image = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
        self.image_show.setPixmap(QPixmap.fromImage(image))

    ################################################## Button functioning ##########################

    def change_box_rate(self, value):
        self.__image_handler__.setRate(value)

    def set_boxes_visibility(self, state):
        if state == Qt.Checked:
            self.boxes_visibility = True
            self.set_image()
        else:
            self.boxes_visibility = False
            self.set_image()

        print(self.__image_handler__.getBoxes())

    def select_next_box(self):
        self.__image_handler__.select_next_box()
        self.set_image()

    def move_box_left(self):
        self.__image_handler__.decX(self.__image_handler__.get_selected_box())
        self.set_image()

    def move_box_right(self):
        self.__image_handler__.incX(self.__image_handler__.get_selected_box())
        self.set_image()

    def move_box_up(self):
        self.__image_handler__.decY(self.__image_handler__.get_selected_box())
        self.set_image()

    def move_box_down(self):
        self.__image_handler__.incY(self.__image_handler__.get_selected_box())
        self.set_image()

    def inc_box_length(self):
        self.__image_handler__.incLength(self.__image_handler__.get_selected_box())
        self.set_image()

    def dec_box_length(self):
        self.__image_handler__.decLength(self.__image_handler__.get_selected_box())
        self.set_image()

    def inc_box_height(self):
        self.__image_handler__.incHeight(self.__image_handler__.get_selected_box())
        self.set_image()

    def dec_box_height(self):
        self.__image_handler__.decHeight(self.__image_handler__.get_selected_box())
        self.set_image()


if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    Window = Window()
    sys.exit(App.exec_())
