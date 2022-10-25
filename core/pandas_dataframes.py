import pandas as pd


class PandasDataFrame:
    def __init__(self, file_name, init_type):
        match init_type:
            case 'csv':
                self.pandas_df = pd.read_csv(file_name)
