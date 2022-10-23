from PySide6.QtWidgets import QToolBar


class TransformToolBar(QToolBar):
    def __int__(self, parent=None):
        super.__init__(parent)
        self.setFixedHeight(50)
        self.setMovable(False)
