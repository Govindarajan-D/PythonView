import sys
from gui.pv_application import PVApplication
from PySide6 import QtWidgets


class PythonView:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.widget = PVApplication()
        self.widget.resize(800,800)
        self.widget.show()

        sys.exit(self.app.exec())


if __name__ == "__main__":
    pv_instance = PythonView()
