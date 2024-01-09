import json
import pandas as pd


def read_data_from_csv(filename, **kwargs):
    with open(filename, 'rb') as f:
        df = pd.read_csv(f)
    return df


def read_data_from_json(filename, **kwargs):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def read_data_from_file(filename, **kwargs):
    file_suffix = filename.split('.')[-1]
    if file_suffix == 'csv':
        return read_data_from_csv(filename, **kwargs)
    elif file_suffix == 'json':
        return read_data_from_json(filename, **kwargs)
    return None
