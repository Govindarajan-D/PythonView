from PySide6.QtCore import QAbstractListModel, Qt


class QueriesList(QAbstractListModel):
    def __init__(self, queries=None):
        super().__init__()
        self.queries_list = queries or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            text = self.queries_list[index.row()]
            return text

    def rowCount(self, index):
        return len(self.queries_list)

    def insertRow(self, text, row: int = 0) -> bool:
        if row == 0:
            self.queries_list.append(text)
        else:
            self.queries_list[row] = text
