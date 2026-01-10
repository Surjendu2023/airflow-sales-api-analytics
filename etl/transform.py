from utils.api_connection import read_file
from utils.api_connection import base_path
import json

user_raw=read_file(base_path('user'))

product_raw=read_file(base_path('product'))

cart_raw=read_file(base_path('cart'))

#transforming raw data into meaningfull dataset

print(user_raw['users'][0]['id'])

# user_info={'id':user_raw['users'][0]['id'],
#            "firstName": user_raw['users']["firstName"],
#             "lastName": user_raw['users']["lastName"],
#             "maidenName":user_raw['users']["maidenName"],
#             "age": user_raw['users']["age"],
#             "gender": user_raw['users']["gender"],
#             "email": user_raw['users']["email"],
#             "phone": user_raw['users']["phone"],
#             "username": user_raw['users']["username"],
#             "password": user_raw['users']["password"],
#             "birthDate": user_raw['users']["birthDate"],
#             "address": user_raw['users']["address"]["address"],
#             "city":user_raw['users']["address"]["city"],
#             "state":user_raw['users']["address"]["state"],
#             "stateCode":user_raw['users']["address"]["stateCode"],
#             "postalCode":user_raw['users']["address"]["postalCode"],
#             "latitude":user_raw['users']["address"]["coordinates"]["lat"],
#             "longitude":user_raw['users']["address"]["coordiates"]["lng"],
#             "country":user_raw['users']["country"]
#             }

# print(user_info)