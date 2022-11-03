from PySide6.QtWidgets import QTableView
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt


class TableWidget(QTableView):
    def __init__(self):
        QTableView.__init__(self)

    def contextMenuEvent(self, event):
        index = self.indexAt(event.pos())
        self.setContextMenuPolicy(Qt.ActionsContextMenu)

        add_action = QAction("Hide", self)
        add_action.triggered.connect(self.hideRow(10))
        self.addAction(add_action)

        refresh_action = QAction("Select", self)
        refresh_action.triggered.connect(self.selectRow(5))
        self.addAction(refresh_action)

