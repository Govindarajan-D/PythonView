from PySide6.QtWidgets import QDockWidget, QListWidget


class SidebarQueries(QDockWidget):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.setFloating(False)
        self.list_queries = QListWidget()
        self.list_queries.insertItem(0, "Test")
        self.setWidget(self.list_queries)
