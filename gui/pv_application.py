
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow, QMenuBar, QMenu, QFileDialog, QToolBar, QDockWidget, QLabel

import sys
import os
import os.path as path

from core import PandasGenerator
import resources.resources
from .central_window_widget import CentralWindowWidget
from .navbars.transform_toolbar import TransformToolBar
from .navbars.transform_menubar import TransformMenuBar
from .gui_functions import GUIActions


class PyViewApplication(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PythonView")
        self.AppName = "PythonView Application"

        self.actions_obj = GUIActions(self).return_actions()
        self._initialize_menu_bar()
        self._initialize_toolbar()
        self._initialize_status_bar()

        self.pandas_gen = PandasGenerator()
        self.pandas_gen.generate_script("new_column_addition", "df1", "5")

        self._initialize_window()

    def _initialize_menu_bar(self):
        main_menu_bar = TransformMenuBar(self, self.actions_obj)
        self.setMenuBar(main_menu_bar)

    def _initialize_toolbar(self):
        self.main_toolbar = TransformToolBar(self)
        self.addToolBar(Qt.TopToolBarArea, self.main_toolbar)
#        self.main_toolbar.addAction(self.new_action)

    def _initialize_status_bar(self):
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Ready")

    def _initialize_window(self):
        self.dock_left_pane = QDockWidget("Queries")
        self.dock_left_pane.setFloating(False)

        self.test_text = QLabel("Test", self)
        self.dock_left_pane.setWidget(self.test_text)
        self.dock_left_pane.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock_left_pane)

        self.central_widget = CentralWindowWidget(data=self.pandas_gen, parent=self)
        self.setCentralWidget(self.central_widget)

    def open_file(self):
        open_selected_file_name = QFileDialog.getOpenFileNames(self, "Open PyView file", os.path.expanduser("~"),
                                                               'PyView (*.pyv)')

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = PyViewApplication()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
