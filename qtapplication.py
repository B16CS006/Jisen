import sys

import cv2
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QGridLayout, QLabel, QCheckBox, QPushButton, QSlider, QHBoxLayout, \
    QDialog, QLineEdit, QDialogButtonBox, QMessageBox

import application, excelHandler


# noinspection PyAttributeOutsideInit
class Window(QtWidgets.QWidget, application.Application):

    def __init__(self):
        super(Window, self).__init__()
        application.Application.__init__(self, 'database')

        self._excelHandler = excelHandler.ExcelHandler()

        self.boxes_visibility = True
        self.ctrl_pressed = False
        self.wants_to_confirm_reads = False
        self.main_grid_layout = QGridLayout()
        self.image_control_box = QGroupBox('Image Control Box')
        self.init_window()

    @property
    def boxes_visibility(self):
        return self._boxes_visibility

    @boxes_visibility.setter
    def boxes_visibility(self, visibility):
        if isinstance(visibility, bool):
            self._boxes_visibility = visibility
        else:
            self._boxes_visibility = True

    @property
    def is_ctrl_pressed(self):
        return self._ctrl_pressed

    @is_ctrl_pressed.setter
    def is_ctrl_pressed(self, value):
        if isinstance(value, bool):
            self._ctrl_pressed = value
        else:
            self._ctrl_pressed = False

    @property
    def wants_to_confirm_reads(self):
        return self._wants_to_confirm_reads

    @wants_to_confirm_reads.setter
    def wants_to_confirm_reads(self, value):
        if isinstance(value, bool):
            self._wants_to_confirm_reads = value
        else:
            self._wants_to_confirm_reads = False

    def init_window(self):
        self.setWindowIcon(QtGui.QIcon('configuration/Logo.jpeg'))
        self.setWindowTitle('Jisen')
        self.setGeometry(QRect(100, 100, 600, 400))
        self.ui_components()
        self.show()

    def ui_components(self):
        self.image_show = QLabel(self)
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
        self.ui_checkboxes_control()
        self.ui_change_box_control()
        self.ui_move_box_control()
        self.ui_change_box_dimension_control()
        self.ui_start_reading()
        self.set_image()

    def ui_change_box_rate_control(self):
        rate_group = QGroupBox('Rate')
        rate_group.setMaximumHeight(70)
        h_box_layout = QHBoxLayout()

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setFocusPolicy(Qt.NoFocus)
        self.slider.setMinimum(1)
        self.slider.setMaximum(200)
        self.slider.valueChanged[int].connect(self.change_box_rate)

        self.slider_value = QLabel(str(self.slider.value()))

        h_box_layout.addWidget(self.slider)
        h_box_layout.addWidget(self.slider_value)
        rate_group.setLayout(h_box_layout)
        self.main_control_layout.addWidget(rate_group)

    def ui_checkboxes_control(self):
        # Boxes visibility
        boxes_visibility_check_box = QCheckBox('Boxes Visibility')
        boxes_visibility_check_box.toggle()
        boxes_visibility_check_box.stateChanged.connect(self.set_boxes_visibility)
        self.main_control_layout.addWidget(boxes_visibility_check_box)

        # verify reads
        want_to_confirm_reads = QCheckBox('Wants to confirm reads')
        want_to_confirm_reads.stateChanged.connect(self.set_wants_to_confirm_reads)
        self.main_control_layout.addWidget(want_to_confirm_reads)

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

    def ui_start_reading(self):
        read_button = QPushButton('Read Images', self)
        read_button.clicked.connect(self.read_images)
        read_button.setMinimumHeight(30)
        read_button.setMaximumHeight(30)
        self.main_control_layout.addWidget(read_button)

    def set_image(self, image=None):
        self.main_grid_layout.addWidget(self.image_show, 0, 1)
        if image is None:
            image = self.image_handler.get_image()
            if image is None:
                self.image_show.setText('No Image Found')
                return
            else:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        elif isinstance(image, str):
            # pixmap = QtGui.QPixmap(image).scaledToHeight(700)
            image = cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2RGB)
            # self.image_show.setPixmap(pixmap)
            # return
        # print(image, '/////////////////////')
        if self.boxes_visibility:
            self.image_handler.draw_boxes(image)

        # pixmap = (QtGui.QPixmap.fromImage(image))
        image = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888).scaledToHeight(700)

        self.image_show.setPixmap(QPixmap.fromImage(image))

    def ui_correct_if_incorrect_dialog(self):
        self.dialog = QDialog(self)
        self.dialog.setMinimumWidth(250)
        self.dialog.setMinimumHeight(100)

        self.lines = []
        v_box_layout = QVBoxLayout()

        for i in range(self.image_handler.boxCount()):
            line = QLineEdit()
            line.setText(self.values[i])
            self.lines.append(line)
            v_box_layout.addWidget(line)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Close)
        v_box_layout.addWidget(button_box)

        button_box.accepted.connect(self.update_read_image_value)
        button_box.rejected.connect(self.dialog.close)

        self.dialog.setLayout(v_box_layout)
        self.dialog.setWindowTitle('Correct if incorrect')
        self.dialog.exec_()

    def ui_message_dialog(self, title, message):
         QMessageBox.about(self, str(title), str(message))

    def keyPressEvent(self, q_key_event):
        if q_key_event.key() == Qt.Key_W:
            self.dec_box_height()
        elif q_key_event.key() == Qt.Key_S:
            self.inc_box_height()
        elif q_key_event.key() == Qt.Key_A:
            self.dec_box_length()
        elif q_key_event.key() == Qt.Key_D:
            self.inc_box_length()
        elif q_key_event.key() == Qt.Key_H:
            self.move_box_left()
        elif q_key_event.key() == Qt.Key_L:
            self.move_box_right()
        elif q_key_event.key() == Qt.Key_J:
            self.move_box_down()
        elif q_key_event.key() == Qt.Key_K:
            self.move_box_up()
        elif q_key_event.key() == Qt.Key_N:
            self.select_next_box()
        elif q_key_event.key() == Qt.Key_Control:
            self.ctrl_pressed = True
        elif q_key_event.key() == Qt.Key_Q:
            if self.ctrl_pressed:
                sys.exit('Quit')
        elif q_key_event.key() == Qt.Key_Minus:
            self.slider.setValue(self.slider.value() - 1)
            self.slider_value.setText(str(self.slider.value()))
        elif q_key_event.key() == Qt.Key_Plus:
            self.slider.setValue(self.slider.value() + 1)
            self.slider_value.setText(str(self.slider.value()))
        super().keyPressEvent(q_key_event)

    def keyReleaseEvent(self, q_key_event):
        if q_key_event.key() == Qt.Key_Control:
            self.ctrl_pressed = False
        super().keyReleaseEvent(q_key_event)
    ################################################## Button functioning ##########################

    def change_box_rate(self, value):
        self.image_handler.rate = value
        self.slider_value.setText(str(self.slider.value()))

    def set_boxes_visibility(self, state):
        if state == Qt.Checked:
            self.boxes_visibility = True
            self.set_image()
        else:
            self.boxes_visibility = False
            self.set_image()

        print(self.image_handler.getBox(self.image_handler.selected_box).box)

    def select_next_box(self):
        self.image_handler.select_next_box()
        self.set_image()

    def move_box_left(self):
        self.image_handler.decX(self.image_handler.selected_box)
        self.set_image()

    def move_box_right(self):
        self.image_handler.incX(self.image_handler.selected_box)
        self.set_image()

    def move_box_up(self):
        self.image_handler.decY(self.image_handler.selected_box)
        self.set_image()

    def move_box_down(self):
        self.image_handler.incY(self.image_handler.selected_box)
        self.set_image()

    def inc_box_length(self):
        self.image_handler.incLength(self.image_handler.selected_box)
        self.set_image()

    def dec_box_length(self):
        self.image_handler.decLength(self.image_handler.selected_box)
        self.set_image()

    def inc_box_height(self):
        self.image_handler.incHeight(self.image_handler.selected_box)
        self.set_image()

    def dec_box_height(self):
        self.image_handler.decHeight(self.image_handler.selected_box)
        self.set_image()

    def set_wants_to_confirm_reads(self, state):
        if state == Qt.Checked:
            self.wants_to_confirm_reads = True
        else:
            self.wants_to_confirm_reads = False

    def read_images(self):

        import glob

        images = [image for image in glob.glob('database/images/*')]
        # print(images)

        for image in images:
            self.image_handler.set_image(image, False)
            self.set_image()
            self.read_image()

        self._excelHandler.save_workbook('database/default2.xls')
        self.ui_message_dialog('Message', 'Complete')

    def read_image(self):
        self._read_box_images()
        if self.wants_to_confirm_reads:
            self.ui_correct_if_incorrect_dialog()
        # print(self.values)
        values = {
            'name': self.values[1],
            'index': self.values[2].split('/')[0],
            'order': self.values[3],
            'santoor': self.values[4]
        }
        self._excelHandler.update_excel_file(values)

    def update_read_image_value(self):
        self.dialog.close()
        for i in range(self.image_handler.boxCount()):
            self.values[i] = self.lines[i].text()


if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    Window = Window()
    sys.exit(App.exec_())
