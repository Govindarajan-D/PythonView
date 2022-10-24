from PySide6.QtWidgets import QFileDialog
import os


class GUISlots:
    def __init__(self):
        self.open_selected_file_name = None

    def open_file(self):
        self.open_selected_file_name = QFileDialog.getOpenFileNames(self, "Open PyView file", os.path.expanduser("~"),
                                                                    'PyView (*.pyv)')
