from PySide6.QtGui import QAction, QIcon, QPixmap
import logging

# Do not delete below line, it contains the resources (icons) for actions
import resources.resources


class GUIActions:
    def __init__(self, parent=None):
        self.log = logging.getLogger(__name__)

        self.actions_list = None
        self.parent = parent
        self.open_action = QAction(QIcon(QPixmap(":/icons/open-file-icon.png")), "&Open PyView File", self.parent)

        self.read_csv = QAction(QIcon(QPixmap(":/icons/read-csv-icon.png")), "&Read CSV", self.parent)
        self.read_sql = QAction(QIcon(QPixmap(":/icons/read-sql-icon.png")), "Read SQL", self.parent)
        self.exit_app = QAction(QIcon(QPixmap(":/icons/exit-app-icon.png")), "&Exit App", self.parent)

        self.about_dlg = QAction("&About PyView", self.parent)
        self._initialize_actions()

    def _initialize_actions(self):
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.setToolTip("Open PyView file")

        self.read_csv.setShortcut("Ctrl+R")
        self.read_csv.setToolTip("Read CSV file")

        self.read_sql.setToolTip("Read SQL data")

        self.exit_app.setShortcut("Ctrl+W")
        self.exit_app.setToolTip("Exit Application")
        self.exit_app.triggered.connect(self.parent.exit_app)

        self.about_dlg.setToolTip("About PyView")
        self.about_dlg.triggered.connect(self.parent.about_dialog)

        self.log.info("Initialized GUI actions")

    def return_actions(self):
        self.actions_list = {"open_action": self.open_action, "read_csv": self.read_csv, "exit_app": self.exit_app,
                             "about_dlg": self.about_dlg, "read_sql": self.read_sql}
        return self.actions_list
