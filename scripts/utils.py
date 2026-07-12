import os

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def list_csv(folder):
    return [f for f in os.listdir(folder) if f.endswith(".csv")]

def list_parquet(folder):
    return [f for f in os.listdir(folder) if f.endswith(".parquet")]