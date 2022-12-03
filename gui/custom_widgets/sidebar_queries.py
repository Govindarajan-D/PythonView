from PySide6.QtWidgets import QWidget, QListView, QVBoxLayout


class SidebarQueries(QWidget):
    def __init__(self, title, queries_list_model):
        super().__init__()
        self.setWindowTitle(title)
        layout = QVBoxLayout()
        self.list_queries = QListView()
        self.list_queries.setModel(queries_list_model)
        layout.addWidget(self.list_queries)
        self.setLayout(layout)
