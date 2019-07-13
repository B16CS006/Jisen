import sys

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QRect

import application


class Window(QtWidgets.QMainWindow, application.Application):

    def __init__(self):
        super(Window, self).__init__()
        application.Application.__init__(self, 'database')

        self.init_window()

    def init_window(self):
        self.setWindowIcon(QtGui.QIcon('configuration/Logo.jpeg'))
        self.setWindowTitle('Jisen')
        self.setGeometry(QRect(100, 100, 600, 400))
        self.ui_components()
        self.show()

    def ui_components(self):
        button = QtWidgets.QPushButton('Show Image', self)
        button.setMinimumHeight(30)
        button.clicked.connect(self._show)


if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    Window = Window()
    sys.exit(App.exec_())
