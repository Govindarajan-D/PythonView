import sys
from gui import PyViewApplication
from PySide6 import QtWidgets


class PythonView:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.widget = PyViewApplication()
        self.widget.showMaximized()
        self.widget.show()

        sys.exit(self.app.exec())


if __name__ == "__main__":
    pv_instance = PythonView()
