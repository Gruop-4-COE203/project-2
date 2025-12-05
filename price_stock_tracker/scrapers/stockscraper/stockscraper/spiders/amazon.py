import scrapy

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url]
    def parse(self, response):
        title = response.css("#productTitle::text").get().strip()
        price = response.css("span.a-offscreen::text").get()
        yield {
            "title": title,
            "price": price,
            "url": response.url
        }