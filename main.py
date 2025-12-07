import argparse
"""  for getting the urls (input) """
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
""" allows the Scrapy works in main.py  """
from price_stock_tracker.scrapers.spiders.BookSpider import BookSpider
from price_stock_tracker.tracker.mongo_price_record_repository import MongoPriceRecordRepo

def select_spider(url: str):
   url_lower = url.lower()
   if "books.toscrape" in url_lower:
       return BookSpider
   else:
       raise ValueError("Invalid url")

def run_scraper(url: str):
    spider_class = select_spider(url)

    print (f"URL: {url} ")
    print("Selected spider: ", spider_class.__name__)
    print("Starting up Scraper")

    process = CrawlerProcess(get_project_settings())
    process.crawl(spider_class, url=url)
    process.start()

    print("\n" + "─" * 50)

    from price_stock_tracker.tracker.configuration import local_DB
    product_cursor = local_DB["products"].find({"url": url}).sort("_id", -1).limit(1)
    product = next(product_cursor, None)

    if product:
        title = product.get("title", "Unknown").title()
        stock = product.get("stock", "N/A")
        stock_count = product.get("stock_count", "N/A")
    else:
        title = "Unknown"
        stock = "N/A"
        stock_count = "N/A"

    print(f"📘 BOOK: {title}")
    print(f"🔗 URL: {url}\n")
    print(f"📦 STOCK: {stock} ({stock_count} available)")


    if not MongoPriceRecordRepo().get_history(url):
        print("No price history yet.")
        print("─" * 60)
        return

    if MongoPriceRecordRepo().get_history(url):
        last = MongoPriceRecordRepo().get_history(url)[-1]
        print(f"💰 LAST PRICE: {last.price}")
        print(f"📅 DATE: {last.timestamp}")

        print("📊 PRICE HISTORY:")
        for record in MongoPriceRecordRepo().get_history(url):
            marker = "← latest" if record == last else ""
            print(f"  • {record.price:<8} — {record.timestamp} {marker}")

    print("─" * 60)

    if MongoPriceRecordRepo().get_history(url):
        last=MongoPriceRecordRepo().get_history(url)[-1]
        print(f"Last Price: {last.price}")
    else:
        print(f"No price record for product.")

    print("Scraping Complete")
    print("Data save in MongoDB")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Price Stock Tracker')
    parser.add_argument("--url", required=False, help="Enter the url")

    args = parser.parse_args()

    while True:
       try:
           if args.url:
               url = args.url
           else:
               url = input("Enter the url (or write 'quit' to quit): ")
           if url.lower() == "quit":
               print("Exiting program")
               break
           run_scraper(url)
           break
       except ValueError as e:
           print(f"Error: {e}")
           print("Please try again")
           args.url = None
