# from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QMainWindow, QApplication
from ui import Ui_MainWindow

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
