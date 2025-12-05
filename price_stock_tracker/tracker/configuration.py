#FOR DATABASE WE USE ATLAS MONGODB

#adding mongo url
from pymongo import MongoClient
"""We install pymongo library in terminal(pip3 install pymongo). 
*What is pymongo? -> It's library to 
   After that we get connection string for Python from Atlas"""

Mongo_Url = "mongodb+srv://tracker_user:tracker_user123@cluster0.jax27jp.mongodb.net/?appName=Cluster0"
client = MongoClient(Mongo_Url)
db = client['price_stock_tracker']
