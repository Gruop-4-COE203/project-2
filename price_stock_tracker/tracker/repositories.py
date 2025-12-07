
#importing necessary modules
from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Product, PriceRecord

#Defining Base Product Class
class BaseProductRepository(ABC):
    """It's abstract repository for products. """
    @abstractmethod
    def create_product(self, product_id: str, price: float) -> Product:
        """Saving a new product and return it."""
        raise NotImplementedError
    @abstractmethod
    def get_product(self, product_id: str) -> Optional[Product]:
        """Returning product id, and it's optional so can be None if not found."""
        raise NotImplementedError
    @abstractmethod
    def list_products(self) -> List[Product]:
        """Returning all products."""
        raise NotImplementedError
    @abstractmethod
    def update_product(self, product_id: str, price: float) -> Product:
        """Updating product with new price and given id."""
        raise NotImplementedError
    @abstractmethod
    def delete_product(self, product_id: str) -> Optional[Product]:
        """Delete product with given id."""
        raise NotImplementedError

#Defineding Base Price Class
class BasePriceRepository(ABC):
    """It's abstract repository for prices. """
    @abstractmethod
    def add_price(self, record: PriceRecord) -> PriceRecord:
        """Adding new price to product with given id."""
        raise NotImplementedError
    @abstractmethod
    def get_price(self, product_id: str) -> List[PriceRecord]:
        """Returning all prices for product."""
        raise NotImplementedError
