import sys
from gui import PyViewApplication
from PySide6 import QtWidgets
import logging

logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s-%(name)s-%(levelname)s-%(message)s', level=logging.INFO)


class PythonView:
    def __init__(self):
        self.log = logging.getLogger(__name__)

        self.app = QtWidgets.QApplication([])
        self.widget = PyViewApplication()
        self.widget.showMaximized()
        self.widget.show()
        self.log.info("Application Initialized")
        sys.exit(self.app.exec())


if __name__ == "__main__":
    pv_instance = PythonView()
