from PySide6 import QtCore
from PySide6.QtCore import Signal, QObject, QRunnable, QThreadPool
from PySide6.QtWidgets import QFileDialog, QMessageBox
from core import DataFrame
from gui.custom_widgets.sql_connection import SQLConnection
import os
import logging


class TransformController(QObject):
    """
    TransformController provides functions that connects view with the model/core functions
    The python view object is passed to the controller which it uses to call the various updates/refreshes it needs
    to do on the UI
    """
    update_transform_text_signal = Signal(str)

    def __init__(self, pyview_object, actions, dataframe_list):
        super().__init__()
        self.open_selected_file_name = None
        self.open_csv_file_name = None
        self.thread_pool = QThreadPool()

        self.actions_obj = actions
        self.object = pyview_object
        self.dataframe_list = dataframe_list

        self.log = logging.getLogger(__name__)

        # Signals are connected to the  corresponding slots
        # (Views connected to Model/Core functions)
        self.actions_obj["read_csv"].triggered.connect(self.read_csv)
        self.actions_obj["open_action"].triggered.connect(self.open_file)
        self.actions_obj["read_sql"].triggered.connect(self.open_sql_connection_widget)
        self.update_transform_text_signal.connect(self.update_transform_text)

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
            df = DataFrame(source_metadata, 'csv')
            self.set_queries_controller(df.dataframe_name)
            self.object.dock_left_pane.list_queries.repaint()
            self.dataframe_list[df.dataframe_name] = df
            self.object.update_table()

            self.log.info("File read from:" + self.open_csv_file_name)

            self.update_transform_text_signal.emit(df.dataframe_name)

    @QtCore.Slot()
    def open_sql_connection_widget(self):
        sql_connection = SQLConnection(self.object)
        sql_connection.show()
        sql_connection.ok_button.clicked.connect(lambda: self.get_sql_details(sql_connection))

    @QtCore.Slot()
    def get_sql_details(self, sql_conn_obj):
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

        # Create thread pool and run in a separate thread to not affect GUI
        worker = RunThread(self.read_sql, source_metadata)
        self.thread_pool.start(worker)

    def read_sql(self, source_metadata):
        try:
            df = DataFrame(source_metadata, 'sql')
            self.log.info("SQL Data Read from:" + source_metadata.table_name)
            self.dataframe_list[df.dataframe_name] = df
            self.update_transform_text_signal.emit(df.dataframe_name)

        except:
            error_dialog_sql = QMessageBox()
            error_dialog_sql.setIcon(QMessageBox.Critical)
            error_dialog_sql.setWindowTitle("SQL connection error")
            error_dialog_sql.setText("Invalid SQL connection information provided")
            error_dialog_sql.exec()

    @QtCore.Slot()
    def update_transform_text(self, dataframe_name):
        self.object.central_widget.script_text.setText(
            self.dataframe_list[dataframe_name].gen_object.transform_code.get_text())


class RunThread(QRunnable):
    def __init__(self, function, *args, **kwargs):
        super().__init__()

        self.function = function
        self.args = args
        self.kwargs = kwargs

    @QtCore.Slot()
    def run(self) -> None:
        result = self.function(*self.args, **self.kwargs)
