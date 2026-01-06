
# api setup
source_data_base_api="https://dummyjson.com/"
cart_data_api=source_data_base_api+"carts"
product_data_api=source_data_base_api+"products"
user_data_api=source_data_base_api+"users"


#db setup
database_name='surjendu'
host_name='localhost'
user_name='postgres'
password='admin'
table_name={'customers':'dim_customers',
            'products':'dim_products',
            'analytical_table':'fact_sales_orders'
            }
engine=r"postgresql+psycopg2://{}:{}@{}/{}".format(user_name,password,host_name,database_name)

#messaging app setup(telegram)
token='6653752665:AAGeGEqnSaraeY1dHNGjGLY-GEyyhDfCxgU'
chat_id='1702937489'
message="Testing"
telegram_bot_api=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"