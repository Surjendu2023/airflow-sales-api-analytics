import pandas as pd
import logging
from utils.api_connection import data_extract,create_dataframe,base_path
from config.config import *

def user_data_fetch():      
    user_data=data_extract(user_data_api)['users']
    print(f'data extracting started from {user_data_api}')
    # user data base :
    users_database=[]
    for users in user_data:
        content={'customer_id':users.get('id'),
                    'firstname':users.get('firstName'),
                    'lastname':users.get('lastName'),
                    'middlename':users.get('maidenName'),
                    'age':users.get('age'),
                    'gender':users.get('gender'),
                    'email':users.get('email'),
                    'phone':users.get('phone'),
                    'username':users.get('username'),
                    'password':users.get('password'),
                    'birthdate':users.get('birthDate'),
                    'address':users.get('address').get('address'),
                    'city':users.get('address').get('city'),
                    'state':users.get('address').get('state'),
                    'statecode':users.get('address').get('stateCode'),
                    'postalcode':users.get('address').get('postalCode'),
                    'latitude':users.get('address').get('coordinates').get('lat'),
                    'longititude':users.get('address').get('coordinates').get('lng'),
                    'country':users.get('address').get('country'),
                    'card_expiry_date':users.get('bank').get('cardExpire'),
                    'cardnumber':users.get('bank').get('cardNumber'),
                    'cardType':users.get('bank').get('cardType'),
                    'currency':users.get('bank').get('currency'),
                    'iban':users.get('bank').get('iban'),
                    'department':users.get('company').get('department'),
                    'company':users.get('company').get('name'),
                    'designation':users.get('company').get('title'),
                    'role':users.get('role'),
                    'userAgent':users.get('userAgent')}
        users_database.append(content)
    return users_database

def product_data_fetch():
    product_data=data_extract(product_data_api)['products']
    print(f'data extracting started from {product_data_api}')
    #product data base:
    product_database=[]
    for products in product_data:
            product_content={'customer_id':products.get('id'),
                            'title':products.get('title'),
                            'description':products.get('description'),
                            'category':products.get('category'),
                            'price':products.get('price'),
                            'discountpercentage':products.get('discountPercentage'),
                            'rating':products.get('rating'),
                            'stock':products.get('stock'),
                            'tags':products.get('tags',[]),
                            'brand':products.get('brand'),
                            'sku':products.get('sku'),
                            'warranty':products.get('warrantyInformation'),
                            'shippinginfo':products.get('shippingInformation'),
                            'availability':products.get('availabilityStatus'),
                            'review_list':products.get('reviews',{}),
                            'return_policy':products.get('returnPolicy'),
                            'minimumorderqty':products.get('minimumOrderQuantity'),
                            'posted_on':products.get('meta').get('createdAt'),
                            'lastmodify_date':products.get('meta').get('updatedAt')
                            }
            product_database.append(product_content)
    return product_database


def cart_data_fetch():
    cart_data=data_extract(cart_data_api)['carts']
    print(f'data extracting started from {cart_data_api}')
    # cart data base:
    cart_database=[]
    for each_customer in cart_data:
        for each_product in each_customer.get('products'):
            content={'customer_id':each_customer.get('id'),
                       'product_id':each_product.get('id'),
                       'title':each_product.get('title'),
                       'quantity':each_product.get('quantity'),
                       'total':each_product.get('total'),
                       'discount':each_product.get('discountPercentage'),
                       'discountedTotal':each_product.get('discountedTotal')
                        }
            cart_database.append(content)
    return cart_database


## dataframe creating

user_df=create_dataframe(user_data_fetch())
product_df=create_dataframe(product_data_fetch())
cart_df=create_dataframe(cart_data_fetch())

#storing the data to locally/cloud


user_df.to_csv(base_path('user'),index=False)

product_df.to_csv(base_path('product'),index=False)

cart_df.to_csv(base_path('cart'),index=False)

print('all set...')