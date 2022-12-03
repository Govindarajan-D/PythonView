from PySide6.QtWidgets import QTabWidget, QWidget, QVBoxLayout
from gui.custom_widgets.central_window_widget import CentralWindowWidget


class TabbedWindow(QWidget):
    """
    TabbedWindow class to make the dataframe transformation screen appear as set of tabs. This allows to switch easily
    between different dataframes and see data.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.central = CentralWindowWidget(self)
        self.tabs = QTabWidget()
        self.tabs.addTab(self.central, "test_tab")
        self.tabs_index = ["test_tab"]
        self.layout_tab = QVBoxLayout()
        self.layout_tab.addWidget(self.tabs)
        self.setLayout(self.layout_tab)

    def add_tab(self, tab_data):
        self.tabs.addTab(CentralWindowWidget(self), tab_data['dataframe_name'])
        self.tabs_index.append(tab_data['dataframe_name'])

    def remove_tab(self, tab_data):
        self.tabs.removeTab(self.tabs_index.index(tab_data['dataframe_name']))
