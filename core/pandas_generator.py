from core.data_structures import TextStack


class PandasGenerator:
    def __init__(self, dataframe_name):
        self.transform_code = TextStack()
        self.final_dataframe_name = dataframe_name
        self.step_df_names = TextStack()

    def generate_script(self, operation_type, operation_data):
        current_df_name = self.step_df_names.peek()
        if current_df_name is None:
            current_df_name = self.final_dataframe_name
            self.step_df_names.add_step(current_df_name)
        match operation_type:
            case "new_column_addition":
                table_script = operation_type + "[" + operation_data['new_column_name'] + "] = " + operation_data['operation']
            case "select_columns":
                table_script = operation_type + " = " + current_df_name + "[[" + operation_data['columns'] + "]]"
            case "read_csv":
                table_script = operation_type + " = " + "pd.read_csv(" + operation_data['file_path'] + ")"

        self.step_df_names.add_step(operation_type)
        self.transform_code.remove_step()
        self.transform_code.add_step(table_script)

        last_step = self.final_dataframe_name + " = " + operation_type
        self.transform_code.add_step(last_step)
