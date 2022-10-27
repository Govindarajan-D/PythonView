from PySide6.QtWidgets import QWidget, QTextEdit, QTableWidget, QVBoxLayout,  QAbstractItemView


class CentralWindowWidget(QWidget):
    def __init__(self, data="", parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        self.script_text = QTextEdit(data, self)
        layout.addWidget(self.script_text, 2)

        self.data_table = QTableWidget(50, 15, self)
        self.data_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        layout.addWidget(self.data_table, 98)

        self.setLayout(layout)
