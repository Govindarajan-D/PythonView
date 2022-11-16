from PySide6.QtWidgets import QDockWidget, QListView


class SidebarQueries(QDockWidget):
    def __init__(self, title, queries_list_model):
        super().__init__()
        self.setWindowTitle(title)
        self.setFloating(False)
        self.list_queries = QListView()
        self.list_queries.setModel(queries_list_model)
        self.setWidget(self.list_queries)
