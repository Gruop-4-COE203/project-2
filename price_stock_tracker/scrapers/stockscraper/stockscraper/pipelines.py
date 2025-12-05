# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class MongoPipeline:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://tracker_user:tracker_user123@cluster0.jax27jp.mongodb.net/")
        self.db = self.client["price_stock_tracker"]
        self.collection = self.db["products"]
    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
