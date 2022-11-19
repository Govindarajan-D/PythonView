from PySide6.QtWidgets import QWidget, QVBoxLayout, QComboBox


class SQLConnection(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()

        self.combobox = QComboBox()
        self.combobox.addItems([])

        layout.addWidget(self.combobox)