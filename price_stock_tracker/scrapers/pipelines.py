# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from price_stock_tracker.tracker.configuration import db, PRODUCT_COLLECTION

class MongoPipeline:
    def __init__(self):
        # connect to MongoDB collection
        self.collection = db[PRODUCT_COLLECTION]

    def process_item(self, item, spider):
        if not item:
            return item
            
        # add item as a dictionary
        self.collection.insert_one(dict(item))
        print(f"Saved item: {item.get('title')}")
       
        return item
