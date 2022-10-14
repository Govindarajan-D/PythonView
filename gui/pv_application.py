import os

from PySide6 import QtCore, QtWidgets
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QMenuBar, QMenu, QFileDialog
import sys
import os.path as path


class PVApplication(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PythonView")
        self.AppName = "PythonView Application"
        self.svg_resource_path = path.abspath(path.join(__file__, os.pardir, os.pardir, "icons"))
        self._create_actions()
        self._menu_bar_init()
        self._connect_actions()

    def _menu_bar_init(self):
        main_menu_bar = QMenuBar(self)

        file_menu = QMenu("&File", self)
        file_menu.addAction(self.new_action)

        help_menu = QMenu("&Help", self)

        main_menu_bar.addMenu(file_menu)
        main_menu_bar.addMenu(help_menu)

        self.setMenuBar(main_menu_bar)

    def _create_actions(self):
        self.new_action = QAction(QIcon(self.svg_resource_path), "&Open", self)
        self.new_action.setShortcut("Ctrl+O")
        self.new_action.setToolTip("Open existing file")

    def _connect_actions(self):
        self.new_action.triggered.connect(self.open_file)

    @QtCore.Slot()
    def open_file(self):
        open_selected_file_name = QFileDialog.getOpenFileNames(self, "Open PyView file", os.path.expanduser("~"),
                                                               'PyView (*.pyv)')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = PVApplication()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
