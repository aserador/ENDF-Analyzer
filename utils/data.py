import pandas as pd
from io import StringIO
import re

def parse_data(file_path):
    """
    Parses data from a file and returns a pandas DataFrame.

    Args:
        file_path (str): The path to the file containing the data.

    Returns:
        pandas.DataFrame: The parsed data as a DataFrame.

    """
    dfs = {}
    data = ''
    category = None
    y_value = None

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#  [JENDL-5'):
                if data:
                    df = pd.read_csv(StringIO(data), sep='\s+', header=None)
                    df.columns = column_names
                    df['category'] = category 
                    dfs[category] = df
                category = line.strip()
                data = ''
            elif line.startswith('#'):
                column_names = re.split(r'\s{2,}', line.strip('# ').rstrip())
                print(column_names)
                y_value = column_names[1]
            elif not line.startswith('#'):
                data += line

    if data:
        df = pd.read_csv(StringIO(data), sep='\s+', header=None)
        df.columns = column_names
        df['category'] = category
        dfs[category] = df

    df = pd.concat(dfs.values(), keys=dfs.keys(), names=['category', 'original_index'])
    df.to_csv('data/output.csv')
    df = pd.read_csv('data/output.csv', index_col=[0, 1])
    return {'data': df, 'y-value': y_value}