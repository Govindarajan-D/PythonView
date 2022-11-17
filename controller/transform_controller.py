from PySide6 import QtCore


class TransformController:
    def __init__(self, pyview_object):
        self.object = pyview_object

    @QtCore.Slot()
    def set_queries_controller(self, text):
        self.object.queries_list_model.insertRow(text)


def set_side_bar_list():
    pass

def set_dataframe_table():
    pass

def call_operation():
    pass

def set_steps():
    pass