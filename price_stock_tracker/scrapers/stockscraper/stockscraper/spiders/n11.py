import scrapy

class N11Spider(scrapy.Spider):
    name = 'n11'
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url]
    def parse(self, response):
        title = response.css("div.proNameHolder h1::text").get()
        price = response.css("ins::attr(content)").get()
        yield{
            "title": title,
            "price": price,
            "url": response.url
        }
