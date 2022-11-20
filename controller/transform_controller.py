from PySide6 import QtCore
from PySide6.QtWidgets import QFileDialog, QMessageBox
from core import DataFrame
from gui.custom_widgets.sql_connection import SQLConnection
import os


class TransformController:
    def __init__(self, pyview_object, actions, dataframe_list):
        self.open_selected_file_name = None
        self.open_csv_file_name = None
        self.actions_obj = actions
        self.object = pyview_object
        self.dataframe_list = dataframe_list

        self.actions_obj["read_csv"].triggered.connect(self.read_csv)
        self.actions_obj["open_action"].triggered.connect(self.open_file)
        self.actions_obj["read_sql"].triggered.connect(self.open_sql_connection)

    @QtCore.Slot()
    def set_queries_controller(self, text):
        self.object.queries_list_model.insertRow(text)

    @QtCore.Slot()
    def open_file(self):
        self.open_selected_file_name = QFileDialog.getOpenFileNames(self.object, "Open PyView file", os.path.expanduser("~"),
                                                                    'PyView (*.pyv)')

    @QtCore.Slot()
    def read_csv(self):
        self.open_csv_file_name, _ = QFileDialog.getOpenFileName(self.object, "Open CSV file", os.path.expanduser("~"),
                                                                 'CSV file (*.csv)')
        if self.open_csv_file_name is not None and self.open_csv_file_name:
            pandas_df = DataFrame(self.open_csv_file_name, 'csv')
            self.set_queries_controller(self.open_csv_file_name)
            self.dataframe_list.append(pandas_df)
            self.object.update_table()

    @QtCore.Slot()
    def open_sql_connection(self):
        sql_connection = SQLConnection(self.object)
        sql_connection.show()
        sql_connection.ok_button.clicked.connect(lambda: self.read_sql(sql_connection))

    @QtCore.Slot()
    def read_sql(self, sql_conn):
        sql_conn.close()
        selected_sql_server = sql_conn.combobox_db_connectors.currentText()
        print(selected_sql_server)

def set_side_bar_list():
    pass

def set_dataframe_table():
    pass

def call_operation():
    pass

def set_steps():
    pass