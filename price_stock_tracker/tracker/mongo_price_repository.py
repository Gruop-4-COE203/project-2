#This file manages the insertion and retrieval of product price history records in MongoDB.
from typing import List
from price_stock_tracker.tracker.configuration import local_DB, atlas_DB
from price_stock_tracker.tracker.models import PriceRecord

class MongoPriceRecordRepo:
    """
    storing and retrieving price records
    """
    def __init__(self):
        #Local MongoDB collection
        self.local_collection = local_DB["price_records"]
        #Atlas MongoDB collection
        self.atlas_collection = atlas_DB["price_records"] if atlas_DB is not None else None


    def add_record(self, record: PriceRecord) -> PriceRecord:
        """
        save a price history record.
        """
        data = record.__dict__      #convert PriceRecord to dict
        self.local_collection.insert_one(data)     #add it to LocalDB

        if self.atlas_collection is not None:    #add AtlasDB
            self.atlas_collection.insert_one(data)

        return record

    def get_history(self, product_id: str) -> List[PriceRecord]:
        """
        return all history records
        """
        #get records by product_id and sort by timestamp
        cursor = self.local_collection.find({"product_id": product_id}, ).sort([("timestamp", 1)])

        history= []
        for record in cursor:
            record.pop("_id", None) 
            history.append(PriceRecord(**record))   #convert dict to PriceRecord
        return history