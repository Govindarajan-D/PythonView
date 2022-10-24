from .data_structures import TextStack


class PandasGenerator:
    data_frame_names = ["data_frame"]
    transform_code = []

    def __init__(self):
        self.table_script = ""

    def generate_script(self, operation_type, dataframe_name, operation_data):
        match operation_type:
            case "new_column_addition":
                self.table_script += dataframe_name + "[" + "test" + "] = " + operation_data
            case "select_columns":
                self.table_script += dataframe_name + "[[" + operation_data + "]]"
