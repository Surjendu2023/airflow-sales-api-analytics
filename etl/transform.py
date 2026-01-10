from utils.api_connection import read_file
from utils.api_connection import base_path

user_raw=read_file(base_path('user'))

# print(user_raw["address"][0]['address'])

# product_raw=read_file(base_path('product'))

# cart_raw=read_file(base_path('cart'))

#transforming raw data into meaningfull dataset



user_info={'id':user_raw['id'],
           "firstName": user_raw["firstName"],
            "lastName": user_raw["lastName"],
            "maidenName":user_raw["maidenName"],
            "age": user_raw["age"],
            "gender": user_raw["gender"],
            "email": user_raw["email"],
            "phone": user_raw["phone"],
            "username": user_raw["username"],
            "password": user_raw["password"],
            "birthDate": user_raw["birthDate"],
            "address": user_raw["address"][0]["address"],
            "city":user_raw["address"][0]["city"],
            "state":user_raw["address"][0]["state"],
            "stateCode":user_raw["address"][0]["stateCode"],
            "postalCode":user_raw["address"][0]["postalCode"],
            "latitude":user_raw["address"][0]["coordinates"]["lat"],
            "longitude":user_raw["address"][0]["coordinates"]["lng"],
            "country":user_raw['address'][0]["country"]
            }

print(user_info)