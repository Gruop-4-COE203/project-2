import argparse
"""  for getting the urls (input) """
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
""" allows the Scrapy works in main.py  """
from price_stock_tracker.scrapers.spiders.BookSpider import BookSpider

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
