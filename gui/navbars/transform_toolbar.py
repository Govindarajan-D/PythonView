from PySide6.QtWidgets import QToolBar


class TransformToolBar(QToolBar):
    def __init__(self, parent, actions_list):
        super().__init__(parent)
        self.setFixedHeight(50)
        self.setMovable(False)
        self.addAction(actions_list['read_csv'])
        self.addAction(actions_list['read_sql'])