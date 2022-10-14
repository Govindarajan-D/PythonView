from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QMainWindow, QMenuBar, QMenu
import sys


class PVApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.AppName = "PythonView Application"
        self.__menu_bar_init()

    def __menu_bar_init(self):
        main_menu_bar = QMenuBar(self)
        file_menu = QMenu("&File", self)
        help_menu = QMenu("&Help", self)
        main_menu_bar.addMenu(file_menu)
        main_menu_bar.addMenu(help_menu)

        self.setMenuBar(main_menu_bar)

    @QtCore.Slot()
    def magic(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = PVApplication()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
