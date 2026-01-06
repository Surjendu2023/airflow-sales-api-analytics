import pandas as pd
import logging
from utils.api_connection import *
from config.config import *

print('data extracting started................')

user_data=create_dataframe(user_data_api)

product_data=create_dataframe(product_data_api)

cart_data=create_dataframe(cart_data_api)

print('data extracted successfully !!....')

user_data.to_csv("./dataset/raw/user_data.csv",index=False)
product_data.to_csv("./dataset/raw/product_data.csv",index=False)
cart_data.to_csv("./dataset/raw/cart_data.csv",index=False)