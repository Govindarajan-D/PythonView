from PySide6 import QtCore
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QAction, QIcon, QPixmap

import os
import resources.resources


class GUIActions:
    def __init__(self, parent=None):
        self.actions_list = None
        self.parent = parent
        self.new_action = QAction(QIcon(QPixmap(":/icons/open-file-icon.png")), "&Open PyView File", self.parent)
        self.read_csv = QAction(QIcon(QPixmap(":/icons/read-csv-icon.png")), "&Read CSV", self.parent)
        self._initialize_actions()

    def _initialize_actions(self):
        self.new_action.setShortcut("Ctrl+O")
        self.new_action.setToolTip("Open PyView file")
        self.new_action.triggered.connect(self.parent.open_file)

        self.read_csv.setShortcut("Ctrl+R")
        self.read_csv.setToolTip("Read CSV file")
        self.read_csv.triggered.connect(self.parent.read_csv)

    def return_actions(self):
        self.actions_list = {"new_action": self.new_action, "read_csv": self.read_csv}
        return self.actions_list
