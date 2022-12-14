from core.data_structures import TextStack
from collections import Counter


class PandasGenerator:
    """
    PandasGenerator generates code to display in the steps screen. Each step in the UI
    is recorded.
    """
    def __init__(self, dataframe_name):
        """"
        Initializes the text stack for recording steps and the step df names
        :param dataframe_name: Get the dataframe name which be used as the final step dataframe name
        """
        self.transform_code = TextStack()
        self.final_dataframe_name = dataframe_name
        self.step_df_names = TextStack()
        self.operations_list = []

    def generate_script(self, operation_type, operation_data):
        """
        Generates script for each step done in the UI and adds it to the existing list of steps
        :param operation_type: Operation done in the UI that needs to be converted as step
        :param operation_data: Data that will be used to generate the script
        """
        # Maintain a list of dataframe names in the transform code window
        current_df_name = self.step_df_names.peek()
        count_operations = Counter(self.operations_list)
        table_script = None

        # If the list is empty, then add the filename as the last step in the code
        if current_df_name is None:
            current_df_name = self.final_dataframe_name
            self.step_df_names.add_step(current_df_name)

        # If an operation is being performed more than once, append number to the end of the dataframe to keep it unique
        step_df_name = operation_type
        if len(self.operations_list) > 0:
            if count_operations[operation_type] > 0:
                step_df_name = operation_type + "_" + count_operations[operation_type]

        # Match the operation type and generate the corresponding operation pandas code
        match operation_type:
            case "new_column_addition":
                table_script = operation_type + "[" + operation_data['new_column_name'] + "] = " \
                               + operation_data['operation']
            case "select_columns":
                table_script = step_df_name + " = " + current_df_name + "[[" + operation_data['columns'] + "]]"
            case "read_csv":
                table_script = step_df_name + " = " + "pd.read_csv('" + operation_data['file_path'] + "')"
            case "read_sql":
                table_script = step_df_name + " = " + "pd.read_sql('SELECT * FROM " + operation_data['sql_table'] +\
                               "', connection) "

        # Add the operations to the list to maintain the steps that had been done
        self.operations_list.append(operation_type)
        self.step_df_names.add_step(operation_type)
        self.transform_code.remove_step()
        self.transform_code.add_step(table_script)

        # Reassign the final dataframe to the dataframe with the filename
        last_step = self.final_dataframe_name + " = " + step_df_name
        self.transform_code.add_step(last_step)
