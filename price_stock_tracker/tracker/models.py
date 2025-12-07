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
    current_price: Optional[float]  #Optional cause can be missing on first scrape
    in_stock: bool
    created_at: datetime
    updated_at: Optional[datetime] = None #Starts as None until first update

@dataclass
class PriceRecord:
    """
    Represents price record for a product.
    """
    product_id: str
    price: float
    date: Optional[str] = None
    timestamp: Optional[datetime] = None