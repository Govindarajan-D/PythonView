import pandas as pd
from core.pandas_generator import PandasGenerator
import ntpath
import pyodbc


class DataFrame:
    """
    Dataframe object initializes the pd dataframe based on the source type and build the corresponding
    generator object for displaying the steps being done in the UI.
    """
    def __init__(self, source_metadata, init_type):
        """
        Initializes the dataframe object by reading data from the source and populating the generator
        object with the initial steps
        :param source_metadata: Any metadata that will be passed for creating the dataframe
        :param init_type: Type of initialization of how Pandas dataframe will read the data from
        """
        match init_type:
            case 'csv':
                file_path = source_metadata['csv_file_name']
                self.pandas_df = pd.read_csv(file_path)
                self.dataframe_name = ntpath.basename(file_path).replace(".", "_")
                self.gen_object = PandasGenerator(self.dataframe_name)
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
                self.dataframe_name = source_metadata['table_name']
                self.gen_object = PandasGenerator(self.dataframe_name)
                operation_data = {'sql_table': source_metadata['table_name']}
                self.gen_object.generate_script("read_sql", operation_data)
