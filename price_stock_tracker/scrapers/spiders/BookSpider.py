import scrapy

class BookSpider(scrapy.Spider):
    name = "book"

    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url]

    def parse(self, response):
        title = response.css("div.product_main h1::text").get()
        price = response.css("p.price_color::text").get()

        yield {
            "title": title,
            "price": price,
            "url": response.url
        }