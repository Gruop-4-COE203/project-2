#   DEFINING MODELS

#importing necessary modules
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Product:
    """
    Represents product that is being tracked.
    """
    id: str
    name: str
    url: str
    site: str
    current_price: Optional[float]  #Optional cause can be missing on first scrape
    in_stock: bool
    created_at: datetime
    updated_at: Optional[datetime] = None #Starts as None until first update

    def is_price_changed(self, new_price: float):
        return self.current_price != new_price


@dataclass
class PriceRecord:
    """
    Represents price record for a product.
    """
    product_id: str
    price: float
    in_stock: bool
    timestamp: datetime

    def is_discount(self, old_price: float):
        return self.price < old_price


