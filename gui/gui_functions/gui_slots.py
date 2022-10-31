from PySide6 import QtCore
from PySide6.QtWidgets import QFileDialog, QMessageBox
import os

from core.pandas_dataframes import DataFrame


class GUISlots:
    def __init__(self):
        self.dataframe_list = []
        self.open_csv_file_name = None
        self.open_selected_file_name = None

    @QtCore.Slot()
    def open_file(self):
        self.open_selected_file_name = QFileDialog.getOpenFileNames(self, "Open PyView file", os.path.expanduser("~"),
                                                                    'PyView (*.pyv)')

    @QtCore.Slot()
    def read_csv(self):
        self.open_csv_file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV file", os.path.expanduser("~"),
                                                                 'CSV file (*.csv)')
        if self.open_csv_file_name is not None and self.open_csv_file_name:
            pandas_df = DataFrame(self.open_csv_file_name, 'csv')
            self.dataframe_list.append(pandas_df)
            self.update_table()

    @QtCore.Slot()
    def about_dialog(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("PyView About")
        dialog.setText("Application to analyze and visualize data using Python Libraries")
        dialog.exec()
    def update_table(self):
        pass
