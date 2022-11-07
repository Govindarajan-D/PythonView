from PySide6 import QtCore
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QAction, QIcon, QPixmap
import logging

import os
import resources.resources


class GUIActions:
    def __init__(self, parent=None):
        self.log = logging.getLogger(__name__)

        self.actions_list = None
        self.parent = parent
        self.new_action = QAction(QIcon(QPixmap(":/icons/open-file-icon.png")), "&Open PyView File", self.parent)
        self.read_csv = QAction(QIcon(QPixmap(":/icons/read-csv-icon.png")), "&Read CSV", self.parent)
        self.exit_app = QAction(QIcon(QPixmap(":/icons/exit-app-icon.png")), "&Exit App", self.parent)

        self.about_dlg = QAction("&About PyView", self.parent)
        self._initialize_actions()

    def _initialize_actions(self):
        self.new_action.setShortcut("Ctrl+O")
        self.new_action.setToolTip("Open PyView file")
        self.new_action.triggered.connect(self.parent.open_file)

        self.read_csv.setShortcut("Ctrl+R")
        self.read_csv.setToolTip("Read CSV file")
        self.read_csv.triggered.connect(self.parent.read_csv)

        self.exit_app.setShortcut("Ctrl+W")
        self.exit_app.setToolTip("Exit Application")
        self.exit_app.triggered.connect(self.parent.exit_app)

        self.about_dlg.setToolTip("About PyView")
        self.about_dlg.triggered.connect(self.parent.about_dialog)

        self.log.info("Initialized GUI actions")

    def return_actions(self):
        self.actions_list = {"new_action": self.new_action, "read_csv": self.read_csv, "exit_app": self.exit_app, "about_dlg": self.about_dlg}
        return self.actions_list
