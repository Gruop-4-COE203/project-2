from typing import List
from price_stock_tracker.tracker.configuration import local_DB, atlas_DB
from price_stock_tracker.tracker.models import PriceRecord

class MongoPriceRecordRepo:
    """
    storing and retrieving price records
    """
    def __init__(self):
        self.local_collection = local_DB["price_records"]
        self.atlas_collection = atlas_DB["price_records"] if atlas_DB is not None else None


    def add_record(self, record: PriceRecord) -> PriceRecord:
        """
        save a price history record.
        """
        data = record.__dict__
        self.local_collection.insert_one(data)

        if self.atlas_collection is not None:
            self.atlas_collection.insert_one(data)

        return record

    def get_history(self, product_id: str) -> List[PriceRecord]:
        """
        return all history records
        """
        cursor = self.local_collection.find({"product_id": product_id}, ).sort([("timestamp", 1)])

        history= []
        for record in cursor:
            record.pop("_id", None)
            history.append(PriceRecord(**record))
        return history