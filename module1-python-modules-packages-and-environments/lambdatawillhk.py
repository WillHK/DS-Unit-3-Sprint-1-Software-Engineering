import pandas as pd

def print_nulls(df):
    df = df.copy()
    nulls = df.isnull()
    if nulls.sum().sum() > 0:
        print('nulls')
    else:
        print('No nulls in this dataframe.')