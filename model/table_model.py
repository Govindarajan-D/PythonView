from PySide6.QtCore import QAbstractTableModel, Qt


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data.iloc[index.row(), index.column()]

    def rowCount(self):
        return len(self._data)

    def columnCount(self):
        return len(self._data[0])
