from price_stock_tracker.tracker.models import PriceRecord
from price_stock_tracker.tracker.mongo_price_repository import MongoPriceRecordRepo


def test_price_record_insert_and_history():
    repo = MongoPriceRecordRepo()
    repo.atlas_collection = None  # disable Atlas for tests


    record = PriceRecord(
        product_id="https://example.com/book",
        price = 123.00,
        date = "01/01/2025, 12:00:00"
    )

    repo.add_record(record)

    history = repo.get_history("https://example.com/book")

    # last must be lastest one
    last = history[-1]

    assert last.product_id == "https://example.com/book"
    assert last.price == 123.00
    assert "2025" in last.date

