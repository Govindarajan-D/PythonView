
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow, QMenuBar, QMenu, QFileDialog, QToolBar, QDockWidget, QLabel

import sys
import os
import os.path as path

from core import PandasGenerator
import resources.resources
from gui.gui_functions.gui_slots import GUISlots
from gui.central_window_widget import CentralWindowWidget
from gui.navbars.transform_toolbar import TransformToolBar
from gui.navbars.transform_menubar import TransformMenuBar
from gui.gui_functions.gui_actions import GUIActions


class PyViewApplication(QMainWindow, GUISlots):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        GUISlots.__init__(self)
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
        self.main_toolbar = TransformToolBar(self, self.actions_obj)
        self.addToolBar(Qt.TopToolBarArea, self.main_toolbar)

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


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = PyViewApplication()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
