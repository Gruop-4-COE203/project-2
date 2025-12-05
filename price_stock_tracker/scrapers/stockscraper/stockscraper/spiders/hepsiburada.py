import scrapy

class HepsiburadaSpider(scrapy.Spider):
    name = 'hepsiburada'
    def __init__(self, url=None, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.start_urls = [url]
    def parse(self, response):
        title = response.css("h1.xeL9CQ3JILmY0QPCgDcI::text").get()
        price = response.css("div.z7kokklsVwh0K5zFWjIO > span::text").get()
        yield {
            'title': title,
            'price': price,
            'url': response.url
        }

