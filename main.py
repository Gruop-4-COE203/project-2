import argparse
"""  for getting the urls (input) """
from scrapy.crawler import CrawlerProcess
""" allows the Scrapy works in main.py  """
from price_stock_tracker.scrapers.spiders import BookSpider

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

    process = CrawlerProcess()
    process.crawl(spider_class, url=url)
    process.start()

    print("Scraping Complete")
    print("Data save in MongoDB")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Price Stock Tracker')
    parser.add_argument("--url", required=False, help="Enter the url")

    args = parser.parse_args()
    #If user doesn't write --url directly in terminal, get URL with input()
    if args.url:
        url = args.url
    else:
        url = input("Enter the url: ")

    run_scraper(url)


