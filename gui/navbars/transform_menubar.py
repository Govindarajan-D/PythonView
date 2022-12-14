from PySide6.QtWidgets import QMenuBar, QMenu


class TransformMenuBar(QMenuBar):
    def __init__(self, parent, actions_list):
        super().__init__(parent)
        file_menu = QMenu("&File", self)
        file_menu.addAction(actions_list['open_action'])
        file_menu.addAction(actions_list['exit_app'])

        help_menu = QMenu("&Help", self)
        help_menu.addAction(actions_list['about_dlg'])
        self.addMenu(file_menu)
        self.addMenu(help_menu)