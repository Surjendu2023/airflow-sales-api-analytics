
import requests
import pandas as pd

def data_extract(url):
    try:
        responce=requests.get(url)
        return responce.json()  #ensure data loaded to be json only
    except Exception as e:
        print('error while fetching information from API with error message :',e)

def create_dataframe(source_data):
    return pd.DataFrame(source_data)

def read_file(path):
    df=pd.read_json(path)
    return df

def base_path(file_name):
    return f"./dataset/raw/{file_name}_data.csv"
