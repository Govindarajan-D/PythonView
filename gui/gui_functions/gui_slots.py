from PySide6 import QtCore
from PySide6.QtWidgets import QFileDialog, QMessageBox
import os

from core.pandas_dataframes import DataFrame


class GUISlots:
    def __init__(self):
        self.dataframe_list = []
        self.queries_list_model= None

    @QtCore.Slot()
    def exit_app(self):
        pass

    @QtCore.Slot()
    def about_dialog(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("PyView About")
        dialog.setText("Application to analyze and visualize data using Python Libraries")
        dialog.exec()

    def update_table(self):
        pass
