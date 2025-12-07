#FOR DATABASE WE USE ATLAS MONGODB
import os # for safety
from pymongo import MongoClient # adding mongo url

class DatabaseConfiguration:
    def __init__(self):
        """
        for safety cause in mongo url has username and password
        so, we use environment variables instead of hardcoding
        And also, for visibility we use Local and Atlas MongoDB
        """
        self.atlas_url = os.getenv("MONGO_URL")
        self.local_url = "mongodb://localhost:27017/"

        #Connect to Local MongoDB
        self.local_client = MongoClient(self.local_url)
        self.local_db = self.local_client["price_stock_tracker"]

        self.atlas_client = None
        self.atlas_db = None


        #Try connecting to Atlas
        if self.atlas_url:
            try:
                self.atlas_client = MongoClient(self.atlas_url)
                self.atlas_db = self.atlas_client["price_stock_tracker"]
                print("CONNECTED → Atlas MongoDB + Local MongoDB")
            except Exception as e:
                print("Atlas connection failed:", e)
                self.atlas_client = None
                self.atlas_db = None
                print("Falling back to local only.")
        else:
            self.atlas_client = None
            self.atlas_db = None
            print("Atlas URL not found → Using only Local MongoDB.")

    def test_connection(self):
        try:
            self.client.admin.command("ping")
            print("MongoDB connection OK")
        except Exception as e:
            print(f"MongoDB connection failed: {e}")

#Initialize DB
db_configuration = DatabaseConfiguration()
db_configuration.test_connection()

#Collections
PRODUCT_COLLECTION = "products"
PRICE_HISTORY_COLLECTION = "price_history"
#Export DB
local_DB = db_configuration.local_db
atlas_DB = db_configuration.atlas_db