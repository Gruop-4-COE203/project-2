import scrapy

class BookSpider(scrapy.Spider):
    name = "book"

    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url]

    def parse(self, response):
        title = response.css("div.product_main h1::text").get()
        price = response.css("p.price_color::text").get()
        availability = response.css("p.availability::text").get()

        title = self.clean_text(title)

        yield {
            "title": title,
            "price": price,
            "availability":availability,
            "url": response.url
        }

    def clean_text(self, text):
        return text.strip() if text else text
