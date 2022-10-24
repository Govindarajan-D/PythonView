from PySide6 import QtCore
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QAction, QIcon, QPixmap

import os
import resources.resources


class GUIActions:
    def __init__(self, parent=None):
        self.actions_list = None
        self.parent = parent
        self.new_action = QAction(QIcon(QPixmap(":/icons/open-file-icon.png")), "&Open", self.parent)
        self._initialize_actions()

    def _initialize_actions(self):
        self.new_action.setShortcut("Ctrl+O")
        self.new_action.setToolTip("Open existing file")
        self.new_action.triggered.connect(self.parent.open_file)

    def return_actions(self):
        self.actions_list = {"new_action": self.new_action}
        return self.actions_list





