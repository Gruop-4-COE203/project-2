# project-2
## **  PRICE AND STOCK TRACKER **

 It's mini project to use Python, Scrapy and MongoDB(local and atlas).Purpose of this code is tracking books price and stock 

#### HOW IT WORKS?
This project get URL in input, then retrieves product information from given URL, runs ,scrapy,spider and  extracted data, finally saves it to database (Atlas and Local MongoDB)
Also, project has 3 test module written by pytest.

#### HOW TREE LOOKS LIKE?
project-2/
│
├── main.py
├── scrapy.cfg
├── README.md
│
├── price_stock_tracker/
│   ├── __init__.py
│   │
│   ├── scrapers/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── pipelines.py
│   │   └── spiders/
│   │       ├── __init__.py
│   │       └── BookSpider.py
│   │
│   └── tracker/
│       ├── __init__.py
│       ├── base_repositories.py
│       ├── configuration.py
│       ├── models.py
│       ├── mongo_price_repository.py
│       └── mongo_stock_repository.py
│
└── tests/
    ├── main_test.py
    ├── repo_test.py
    └── spider_test.py
#### STEP BY STEP FİLES
##### main.py

- Take URL as input
- Runs Scrapy spider
- Process data returned by the spider.
- Saves data to Local MongoDB and, if available, Atlas MongoDB
- Also, for user prints output

##### price_stock_tracker/scrapers/spiders/BookSpider.py

- Visits given URL
- Extracts fields from HTML (title, price, stock information, URL)
- Outputs these values as a Scrapy item.

##### price_stock_tracker/scrapers/pipelines.py

- Processes items returned by the spider.
- Handles saving scraped data into MongoDB (Local and Atlas).
- Acts as a bridge between Scrapy output and database storage.


##### price_stock_tracker/tracker/models.py

- Contains PriceRecord model
- Define product (product_id, price,date)

##### price_stock_tracker/tracker/base_repositories.py

- Contains basic templates (base classes) for price and stock repositories.
- Defines common functions that other repository files must follow.

##### price_stock_tracker/tracker/mongo_price_repository.py

- Handle how data stored in MongoDB both(Atlas and local)
- add_record -> saves a new price record
- get_history -> returns teh full price history

##### price_stock_tracker/tracker/mongo_stock_repository.py

- Responsible for creating, listing, updating, deleting producst in MongoDB(Atlas and Local)
- Impliments full CRUD operations:
-  * create_product()
-  * list_product()
-  * update_product()
-  * remove_product()

##### price_stock_tracker/tracker/configuration.py

- Sets up MongoDB connections.
- Connects to local MongoDB. 
- Tries to connect to Atlas; falls back to local if it fails.
- Exposes local_DB and atlas_DB for other modules.

##### tests/main_test.py
- Runs the entire pipeline using `subprocess`.
- Sends a sample product URL to `main.py`.
- Checks whether the program prints key outputs such as:
  - `BOOK:`
  - `URL:`
- Ensures Scrapy, processing logic, and output formatting work together correctly.

##### tests/repo_test.py
- Tests the `MongoPriceRecordRepo` class.
- Verifies that:
  - A new price record is inserted properly.
  - `get_history()` returns the expected record list.
- Atlas connection is disabled during this test for stability.

##### tests/spider_test.py
- Tests the Scrapy `BookSpider`.
- Confirms that HTML parsing correctly extracts:
  - title
  - price
  - stock information
  - URL

##### Running Tests
To run all tests:

```bash
pytest