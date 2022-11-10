from core.data_structures import TextStack


class PandasGenerator:
    transform_code = TextStack()

    def __init__(self, dataframe_name):
        self.table_script = ""
        self.dataframe_name = dataframe_name

    def generate_script(self, operation_type, operation_data):
        match operation_type:
            case "new_column_addition":
                self.table_script = self.dataframe_name + "[" + operation_data['new_column_name'] + "] = " + operation_data['operation']
            case "select_columns":
                self.table_script += self.dataframe_name + "[[" + operation_data['columns'] + "]]"
            case "read_csv":
                self.table_script += "pd.read_csv(" + operation_data['file_path'] + ")"

        self.transform_code.add_step(self.table_script)
