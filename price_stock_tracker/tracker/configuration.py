#FOR DATABASE WE USE ATLAS MONGODB
from pymongo import MongoClient # adding mongo url

class DatabaseConfiguration:
    def __init__(self):
        self.atlas_url = "mongodb+srv://tracker_user:tracker_user123@cluster0.jax27jp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
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
            if self.local_client:
                self.local_client.admin.command("ping")
                print("Local MongoDB connection OK")
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