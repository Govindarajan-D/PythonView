from PySide6.QtWidgets import QMenuBar, QMenu


class TransformMenu(QMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        file_menu = QMenu("&File", self)
        file_menu.addAction(self.new_action)

        help_menu = QMenu("&Help", self)

        self.addMenu(file_menu)
        self.addMenu(help_menu)

    def new_action(self):
        pass
