import pandas as pd


class PandasGenerator:
    data_frame_names = ["data_frame"]

    def __init__(self):
        self.table_script = ""

    def generate_script(self, operation_type, dataframe_name, operation_data):
        match operation_type:
            case "new_column_addition":
                self.table_script += dataframe_name + "[" + operation_data.column_name + "] = " + operation_data.operation
