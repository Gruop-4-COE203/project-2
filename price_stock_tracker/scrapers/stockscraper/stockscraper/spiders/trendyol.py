import scrapy

class TrendyolSpider(scrapy.Spider):
    name = 'trendyol'
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url]
    def parse(self, response):
        title = response.css("h1.pr-new-br span::text").get()
        price = response.css("span.prc-dsc::text").get()
        yield{
            "title": title,
            "price": price,
            "url": response.url
        }
