from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout,  QAbstractItemView, QHBoxLayout
from gui.custom_widgets.query_table import TableWidget
from gui.custom_widgets.sidebar_queries import SidebarQueries


class CentralWindowWidget(QWidget):
    def __init__(self, data="", parent=None, sidebarmodel=None):
        super().__init__(parent)

        sidebar_steps = SidebarQueries("Steps", sidebarmodel)
        layout_left_container = QVBoxLayout(self)
        layout_left_container.addWidget(sidebar_steps)

        layout_right_container = QVBoxLayout(self)

        self.script_text = QTextEdit(data, self)
        self.data_table = TableWidget()
        self.data_table.setGeometry(0, 0, 50, 15)
        self.data_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        layout_right_container.addWidget(self.script_text, 2)
        layout_right_container.addWidget(self.data_table, 98)

        # layout_main = QHBoxLayout(self)
        # layout_main.addLayout(layout_left_container, 10)
        #layout_main.addLayout(layout_right_container)

        self.setLayout(layout_right_container)
