#DATA ACCESS LAYER
"""
In this python file setting up "Repository" layer,
to communicate with MongoDB databases
"""

from typing import List, Optional
from datetime import datetime
from price_stock_tracker.tracker.models import Product
from price_stock_tracker.tracker.repositories import BaseProductRepository
from price_stock_tracker.tracker.configuration import local_DB, atlas_DB

class MongoProductRepository(BaseProductRepository):

    def __init__(self):
        """
        Initializes the repository and connects to the 'products' collection in MongoDB.
        """
        self.collection = local_DB['products'] #always connect to local
        self.atlas_collection = None
        if atlas_DB is not None:
          self.atlas_collection = atlas_DB['products']

    def create_product(self, product: Product) -> Product:
        """
        In this function add a new product and save it in MongoDB database.
        """
        self.collection.insert_one(product.__dict__)
        if self.atlas_collection is not None:
            self.atlas_collection.insert_one(product.__dict__)
        return product

    def list_products(self) -> List[Product]:
        """
        In this function stored a list of all products in MongoDB database.
        """
        products = self.collection.find()
        return [Product(**p) for p in products]

    def update_product(self, product_id: str, new_price: float, in_stock: bool) -> Optional[Product]:
        """
        In this function update a product's price and stock.
        If object not found return None.
        """
        data = self.collection.find_one({"id": product_id})
        if not data:
            return None
        updated_data = {
            **data,
            "current_price": new_price,
            "in_stock": in_stock,
            "updated_at": datetime.now()
        }
        self.collection.update_one({"id": product_id}, {"$set": updated_data})
        if self.atlas_collection is not None:
            self.atlas_collection.update_one({"id": product_id}, {"$set": updated_data})
        return Product(**updated_data)

    def remove_product(self, product_id: str) -> Optional[Product]:
        """
        In this function remove a product from MongoDB database.
        """
        data = self.collection.find_one({"id": product_id})
        if not data:
            return None
        self.collection.delete_one({"id": product_id})
        if self.atlas_collection is not None:
            self.atlas_collection.delete_one({"id": product_id})
        return Product(**data)