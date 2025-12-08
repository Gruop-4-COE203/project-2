#   DEFINING MODELS

#importing necessary modules
from dataclasses import dataclass     #for data classes
from datetime import datetime        #for date and time
from typing import Optional

#tracked product information
@dataclass
class Product:
    """
    Represents product that is being tracked.
    """
    id: str     #id of product
    name: str   #name of product
    url: str     #product page link
    current_price: Optional[float]  #Optional cause can be missing on first scrape
    in_stock: bool   #stock status
    created_at: datetime   #the date the product was added 
    updated_at: Optional[datetime] = None #Starts as None until first update

#price history recording of the product
@dataclass
class PriceRecord:
    """
    Represents price record for a product.
    """
    product_id: str    #we determine which product it belongs to with the ID
    price: float       #price of product
    timestamp: Optional[datetime] = None   #registration time