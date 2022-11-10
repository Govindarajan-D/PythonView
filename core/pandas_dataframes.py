import pandas as pd
from core.pandas_generator import PandasGenerator
import ntpath


class DataFrame:
    def __init__(self, file_path, init_type):
        match init_type:
            case 'csv':
                self.pandas_df = pd.read_csv(file_path)
                dataframe_name = ntpath.basename(file_path).replace(".","_")
                self.gen_object = PandasGenerator(dataframe_name)
                operation_data = {'file_path': file_path}
                self.gen_object.generate_script("read_csv", operation_data)
