from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow, QMenuBar, QMenu, QFileDialog, QToolBar, QDockWidget, QLabel

import sys
import os
import os.path as path

from core import PandasGenerator
import resources.resources


class PyViewApplication(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PythonView")
        self.AppName = "PythonView Application"
        self.svg_resource_path = path.abspath(path.join(__file__, os.pardir, os.pardir, "icons"))
        self._initialize_actions()
        self._initialize_menu_bar()
        self._initialize_toolbar()
        self._connect_actions()
        self._initialize_status_bar()

        self.pandas_gen = PandasGenerator()
        self.pandas_gen.generate_script("new_column_addition", "df1", "5")

    def _initialize_menu_bar(self):
        main_menu_bar = QMenuBar(self)

        file_menu = QMenu("&File", self)
        file_menu.addAction(self.new_action)

        help_menu = QMenu("&Help", self)

        main_menu_bar.addMenu(file_menu)
        main_menu_bar.addMenu(help_menu)

        self.setMenuBar(main_menu_bar)

    def _initialize_actions(self):
        self.new_action = QAction(QIcon(QPixmap(":/icons/open-file-icon.png")), "&Open", self)
        self.new_action.setShortcut("Ctrl+O")
        self.new_action.setToolTip("Open existing file")

    def _connect_actions(self):
        self.new_action.triggered.connect(self.open_file)

    def _initialize_toolbar(self):
        self.main_toolbar = QToolBar()
        self.main_toolbar.setFixedHeight(50)
        self.main_toolbar.setMovable(False)
        self.addToolBar(Qt.TopToolBarArea, self.main_toolbar)
        self.main_toolbar.addAction(self.new_action)

    def _initialize_status_bar(self):
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Ready")

    def _initialize_window(self):
        self.dock_left_pane = QDockWidget("queries", self)
        self.test_text = QLabel("test", self)
        self.dock_left_pane.setWidget(self.test_text)

    @QtCore.Slot()
    def open_file(self):
        open_selected_file_name = QFileDialog.getOpenFileNames(self, "Open PyView file", os.path.expanduser("~"),
                                                               'PyView (*.pyv)')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = PyViewApplication()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
