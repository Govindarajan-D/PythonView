from PySide6 import QtCore
from PySide6.QtWidgets import QFileDialog, QMessageBox
from core import DataFrame
from gui.custom_widgets.sql_connection import SQLConnection
import os


class TransformController:
    """
    TransformController provides functions that connects view with the model/core functions
    The python view object is passed to the controller which it uses to call the various updates/refreshes it needs
    to do on the UI
    """
    def __init__(self, pyview_object, actions, dataframe_list):
        self.open_selected_file_name = None
        self.open_csv_file_name = None
        self.actions_obj = actions
        self.object = pyview_object
        self.dataframe_list = dataframe_list

        # Signals are connected to the corresponding to their corresponding slots
        # (Views connected to Model/Core functions)
        self.actions_obj["read_csv"].triggered.connect(self.read_csv)
        self.actions_obj["open_action"].triggered.connect(self.open_file)
        self.actions_obj["read_sql"].triggered.connect(self.open_sql_connection)

    @QtCore.Slot()
    def set_queries_controller(self, text):
        self.object.queries_list_model.insertRow(text)

    @QtCore.Slot()
    def open_file(self):
        self.open_selected_file_name = QFileDialog.getOpenFileNames(self.object, "Open PyView file",
                                                                    os.path.expanduser("~"),
                                                                    'PyView (*.pyv)')

    @QtCore.Slot()
    def read_csv(self):
        # Read CSV file and create a dataframe object and pandas generator object for it
        # Add the dataframe name to the sidebar and then update the table in the centre to show the data
        self.open_csv_file_name, _ = QFileDialog.getOpenFileName(self.object, "Open CSV file", os.path.expanduser("~"),
                                                                 'CSV file (*.csv)')
        if self.open_csv_file_name is not None and self.open_csv_file_name:
            source_metadata = {'csv_file_name': self.open_csv_file_name}
            pandas_df = DataFrame(source_metadata, 'csv')
            self.set_queries_controller(self.open_csv_file_name)
            self.object.dock_left_pane.update()
            self.dataframe_list.append(pandas_df)
            self.object.update_table()

        self.object.central_widget.script_text.setText(pandas_df.gen_object.transform_code.get_text())

    @QtCore.Slot()
    def open_sql_connection(self):
        sql_connection = SQLConnection(self.object)
        sql_connection.show()
        sql_connection.ok_button.clicked.connect(lambda: self.read_sql(sql_connection))

    @QtCore.Slot()
    def read_sql(self, sql_conn_obj):
        # Closes the dialog box after input is done. Get the values entered in the fields
        # Pass the input to create Dataframe object and Pandas Generator object
        sql_conn_obj.close()
        selected_sql_server = sql_conn_obj.combobox_db_connectors.currentText()
        server_url = sql_conn_obj.line_edit_server_url.text()
        database_name = sql_conn_obj.line_edit_db_name.text()
        table_name = sql_conn_obj.line_edit_table_name.text()

        # Required information is passed as a dictionary for the functions to read them
        source_metadata = {'server_type': selected_sql_server, 'server_url': server_url, 'database': database_name,
                           'table_name': table_name}
        pandas_df = DataFrame(source_metadata, 'sql')
        self.dataframe_list.append(pandas_df)
