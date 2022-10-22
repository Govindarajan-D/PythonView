from PySide6.QtWidgets import QWidget, QLayout, QTextEdit, QTableWidget, QVBoxLayout


class QueryCentralWindow(QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QTextEdit(data.table_script, self), 2)
        layout.addWidget(QTableWidget(50, 15, self), 98)
        self.setLayout(layout)