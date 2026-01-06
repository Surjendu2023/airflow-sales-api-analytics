
import requests
import pandas as pd

def data_extract(url):
    responce=requests.get(url)
    return responce.json()

def create_dataframe(url):
    df=pd.DataFrame(data_extract(url))
    return df
