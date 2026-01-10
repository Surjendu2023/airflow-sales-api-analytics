
import requests
import pandas as pd

def data_extract(url):
    responce=requests.get(url)
    return responce.json()

def create_dataframe(url):
    df=pd.DataFrame(data_extract(url))
    return df

def read_file(path):
    df=pd.read_csv(path)
    return df

def base_path(file_name):
    return f"./dataset/raw/{file_name}_data.csv"
