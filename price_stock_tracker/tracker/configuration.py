#FOR DATABASE WE USE ATLAS MONGODB
import os # for safety
from pymongo import MongoClient # adding mongo url

class DatabaseConfiguration:
    def __init__(self):
        """
        for safety cause in mongo url has username and password
        so, we use environment variables instead of hardcoding
        """
        self.mongo_url = os.getenv("MONGO_URL")

        if not self.mongo_url:
           raise EnvironmentError("MONGO_URL environment variable is not set!")

        self.client = MongoClient(self.mongo_url)
        self.db = self.client["price_stock_tracker"]

    def test_connection(self):
        try:
            self.client.admin.command("ping")
            print("MongoDB connection OK")
        except Exception as e:
            print(f"MongoDB connection failed: {e}")

#Initialize DB
db_configuration = DatabaseConfiguration()
db_configuration.test_connection()
db = db_configuration.db

#Collections
PRODUCT_COLLECTION = "products"
PRICE_HISTORY_COLLECTION = "price_history"
