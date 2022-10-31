
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QDockWidget, QLabel

import sys
import logging
from core import PandasGenerator
import resources.resources
from gui.gui_functions.gui_slots import GUISlots
from gui.central_window_widget import CentralWindowWidget
from gui.navbars.transform_toolbar import TransformToolBar
from gui.navbars.transform_menubar import TransformMenuBar
from gui.gui_functions.gui_actions import GUIActions
from model.table_model import TableModel



class PyViewApplication(QMainWindow, GUISlots):
    def __init__(self, parent=None):
        self.log = logging.getLogger(__name__)

        QMainWindow.__init__(self)
        GUISlots.__init__(self)
        self.setWindowTitle("PythonView")
        self.AppName = "PythonView Application"

        self.actions_obj = GUIActions(self).return_actions()
        self._initialize_menu_bar()
        self._initialize_toolbar()
        self._initialize_status_bar()
        self._initialize_window()

    def _initialize_menu_bar(self):
        main_menu_bar = TransformMenuBar(self, self.actions_obj)
        self.setMenuBar(main_menu_bar)

        self.log.info("Initialized MenuBar")

    def _initialize_toolbar(self):
        self.main_toolbar = TransformToolBar(self, self.actions_obj)
        self.addToolBar(Qt.TopToolBarArea, self.main_toolbar)

        self.log.info("Initialized ToolBar")

    def _initialize_status_bar(self):
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Ready")

        self.log.info("Initialized StatusBar")

    def _initialize_window(self):
        self.dock_left_pane = QDockWidget("Queries")
        self.dock_left_pane.setFloating(False)

        self.test_text = QLabel("Test", self)
        self.dock_left_pane.setWidget(self.test_text)
        self.dock_left_pane.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock_left_pane)

        self.central_widget = CentralWindowWidget(parent=self)
        self.setCentralWidget(self.central_widget)

        self.log.info("Initialized Central Window")

    def update_table(self):
        data = self.dataframe_list[0]
        table_model = TableModel(data)
        self.central_widget.data_table.setModel(table_model)

        self.log.info("Data read and set in table")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = PyViewApplication()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
