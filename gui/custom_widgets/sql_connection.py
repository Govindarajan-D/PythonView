from PySide6.QtWidgets import QDialog, QVBoxLayout, QComboBox, QLineEdit, QHBoxLayout, QPushButton
from gui.custom_widgets import config


class SQLConnection(QDialog):
    """
    SQLConnection creates a dialog box for getting the input for connecting with the various types of SQL servers
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Connect SQL Database")
        dialog_layout = QVBoxLayout()
        sql_db_connectors = config['CONNECTORS']['SupportSQLDB'].split(',')
        self.combobox_db_connectors = QComboBox()
        self.combobox_db_connectors.addItems(sql_db_connectors)

        self.line_edit_server_url = QLineEdit()
        self.line_edit_server_url.setPlaceholderText("Database Server name")
        self.line_edit_db_name = QLineEdit()
        self.line_edit_db_name.setPlaceholderText("Database name")
        self.line_edit_table_name = QLineEdit()
        self.line_edit_table_name.setPlaceholderText("Table name")

        buttons_layout = QHBoxLayout()
        self.ok_button = QPushButton("Ok")
        self.cancel_button = QPushButton("Cancel")

        buttons_layout.addWidget(self.ok_button)
        buttons_layout.addWidget(self.cancel_button)

        for widgets in [self.combobox_db_connectors, self.line_edit_server_url, self.line_edit_db_name,
                        self.line_edit_table_name]:
            dialog_layout.addWidget(widgets)
        dialog_layout.addLayout(buttons_layout)

        self.setLayout(dialog_layout)
        self.resize(500, 240)
