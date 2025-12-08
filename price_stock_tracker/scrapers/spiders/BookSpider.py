import scrapy
import re
from datetime import datetime

class BookSpider(scrapy.Spider):
    name = "book"

    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url]

    def parse(self, response, **kwargs):
        title = response.css("div.product_main h1::text").get()
        price = response.css("p.price_color::text").get()
        title = self.clean_text(title)

        stock_raw = response.css("p.instock.availability::text").getall()
        stock_clean = " ".join(stock_raw).strip()

        match = re.search(r"\((\d+)\s+available\)", stock_clean)
        stock_count = int(match.group(1)) if match else None

        stock_status = "In stock" if "In stock" in stock_clean else "Not In stock"

        scrape_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        yield {
            "title": title,
            "price": price,
            "stock_count": stock_count,
            "stock": stock_status,
            "scrape_time": scrape_time,
            "url": response.url
        }
    def clean_text(self, text):
        return text.strip() if text else text