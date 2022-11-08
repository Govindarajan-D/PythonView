import pandas as pd
from core.pandas_generator import PandasGenerator


class DataFrame:
    def __init__(self, file_name, init_type):
        match init_type:
            case 'csv':
                self.pandas_df = pd.read_csv(file_name)
                self.gen_object = PandasGenerator()
                operation_data = {'file_name': file_name}
                self.gen_object.generate_script("read_csv", file_name, operation_data)
