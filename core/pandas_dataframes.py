import pandas as pd
from core.pandas_generator import PandasGenerator
import ntpath
import pyodbc


class DataFrame:
    def __init__(self, source_metadata, init_type):
        match init_type:
            case 'csv':
                file_path = source_metadata['csv_file_name']
                self.pandas_df = pd.read_csv(file_path)
                dataframe_name = ntpath.basename(file_path).replace(".", "_")
                self.gen_object = PandasGenerator(dataframe_name)
                operation_data = {'file_path': file_path}
                self.gen_object.generate_script("read_csv", operation_data)
            case 'sql':
                match source_metadata['server_type']:
                    case 'Microsoft SQL-Server':
                        # TODO: Change this to SQLAlchemy instead of pyodbc. Need to change this to ask username and
                        #  password
                        connection_info = pyodbc.connect('DRIVER={SQL Server}; SERVER=' + source_metadata['server_url']
                                                         + ';DATABASE=' + source_metadata['database']
                                                         + ';Trusted_Connection=yes')
                self.pandas_df = pd.read_sql('SELECT * FROM ' + source_metadata['table_name'], connection_info)
                dataframe_name = source_metadata['table_name']
                self.gen_object = PandasGenerator(dataframe_name)
                operation_data = {'sql_table': source_metadata['table_name']}
                self.gen_object.generate_script("read_sql", operation_data)
