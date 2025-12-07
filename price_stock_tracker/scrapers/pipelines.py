# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from price_stock_tracker.tracker.configuration import local_DB, atlas_DB

class MongoPipeline:
    def __init__(self):
        self.local = local_DB
        self.atlas = atlas_DB

    def process_item(self, item, spider):
        if not item:
            return item
    # add item as a dictionary
    self.collection.insert_one(dict(item))
    print(f"Saved item: {item.get('title')}")

    # save local
    self.local["products"].insert_one(dict(item))
    #save atlas if exist
    if self.atlas is not None:
        self.atlas["products"].insert_one(dict(item))
    return item

