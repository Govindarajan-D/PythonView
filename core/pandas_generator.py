from core.data_structures import TextStack


class PandasGenerator:
    data_frame_names = ["data_frame"]
    transform_code = TextStack()

    def __init__(self):
        self.table_script = ""

    def generate_script(self, operation_type, dataframe_name, operation_data):
        match operation_type:
            case "new_column_addition":
                self.table_script = dataframe_name + "[" + "test" + "] = " + operation_data
            case "select_columns":
                self.table_script += dataframe_name + "[[" + operation_data + "]]"
            case "read_csv":
                self.table_script += "pd.read_csv(" + operation_data['file_name'] + ")"

        self.transform_code.add_step(self.table_script)
