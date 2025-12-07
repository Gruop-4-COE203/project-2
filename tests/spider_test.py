import scrapy
from price_stock_tracker.scrapers.spiders.BookSpider import BookSpider
from scrapy.http import HtmlResponse


def fake_response(url: str, html: str):
    """Create a fake HTML response for testing the spider parse() method."""
    request = scrapy.Request(url=url)
    return HtmlResponse(url=url, request=request, body=html, encoding="utf-8")


def test_book_spider_extracts_fields():
    # Create spider instance (url param is required)
    spider = BookSpider(url="https://books.toscrape.com/test")

    # Fake HTML — matches BookSpider selectors exactly
    html = """
    <html>
        <div class="product_main">
            <h1>Test Book</h1>
        </div>

        <p class="price_color">£50.00</p>

        <p class="instock availability">
            In stock (22 available)
        </p>
    </html>
    """

    # Build fake response
    response = fake_response("https://books.toscrape.com/test", html)

    # Run spider.parse()
    result = list(spider.parse(response))
    assert len(result) == 1, "Spider did not return any items."

    item = result[0]

    # FIELD TESTS
    assert item["title"] == "Test Book"
    assert item["price"] == "£50.00"
    assert item["stock"] == "In stock"
    assert item["stock_count"] == 22

    # auto-generated fields
    assert "scrape_time" in item
    assert "url" in item