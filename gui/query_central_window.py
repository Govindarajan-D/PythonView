from PySide6.QtWidgets import QWidget, QLayout, QTextEdit

class QueryCentralWindow(QWidget):
    def __init__(self, data, parent=None,):
        super().__init__(parent)
        self.layout = QLayout()
        self.layout.addWidget(QTextEdit(data.table_script, self))
        self.setLayout(self.layout)