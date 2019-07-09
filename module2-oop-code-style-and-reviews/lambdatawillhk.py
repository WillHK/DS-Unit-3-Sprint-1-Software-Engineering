import pandas as pd

class LambData:
    
    def __init__(self):
        pass
    
    def get_numeric_column_labels(self):
        pass
    
    def get_categorical_column_labels(self, df: pd.DataFrame):
        column_labels = df.select_dtypes(exclude=["number","bool_","object_"]).columns.tolist()
        return column_labels
    
    def check_df_for_blanks(self, df: pd.DataFrame):
        df = df.copy()
        column_labels = self.get_categorical_column_labels(df)
        for col in column_labels:
            df[col] = df[col].apply(lambda x: True if x.strip(' ')=='' else False)

    def null_check(self, df):
        df = df.copy()
        nulls = df.isna()
        blanks = self.check_df_for_blanks(df)
        pass
    
    def add_column_to_df(self, df: pd.DataFrame, new_col: list, name: str):
        df = df.copy()
        new_col = pd.Series(new_col)
        df[name] = new_col
        return df