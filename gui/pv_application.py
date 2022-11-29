
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QDockWidget

import sys
import logging
from gui.gui_functions.gui_slots import GUISlots
from gui.custom_widgets.central_window_widget import CentralWindowWidget
from gui.navbars.transform_toolbar import TransformToolBar, TabbedToolbar
from gui.navbars.transform_menubar import TransformMenuBar
from gui.custom_widgets.sidebar_queries import SidebarQueries
from gui.gui_functions.gui_actions import GUIActions
from controller.transform_controller import TransformController
from model.queries_list import QueriesList
from model.table_model import TableModel


class PyViewApplication(QMainWindow, GUISlots):
    def __init__(self, parent=None):
        self.log = logging.getLogger(__name__)

        QMainWindow.__init__(self)
        GUISlots.__init__(self)
        self.setWindowTitle("PythonView")
        self.AppName = "PythonView Application"

        # Get the actions specified in the GUI Actions and use them to populate the Menu and Tool Bar
        # Initialize the functions to build the UI ready for use
        self.dataframe_list = {}
        self.actions_obj = GUIActions(self).return_actions()
        self._initialize_menu_bar()
        self._initialize_toolbar()
        self._initialize_status_bar()
        self._initialize_window()

        # Create controller object that will be used for handling all the view <-> Model/Core interactions
        self.controller = TransformController(self, self.actions_obj, self.dataframe_list)

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
        # TODO: Connect the new dataframe init signal with the below slot to initialize queries list array
        self.queries_list_model = QueriesList(["Test"])
        self.dock_left_pane = SidebarQueries("Queries", self.queries_list_model)
        self.dock_left_pane.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock_left_pane)

        self.central_widget = CentralWindowWidget(parent=self)
        self.setCentralWidget(self.central_widget)

        self.log.info("Initialized Central Window")

    def update_table(self):
        data = self.dataframe_list['Sales_csv']
        table_model = TableModel(data)
        self.central_widget.data_table.setModel(table_model)

        self.log.info("Data read and set in table")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = PyViewApplication()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
