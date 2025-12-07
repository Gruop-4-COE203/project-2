import subprocess
import sys

def test_full_pipeline_runs():
    """
    main.py is correctly works(reading line by liny?)
    """
    process = subprocess.Popen(
        [sys.executable, "main.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # enter Test URL  (BooksToScrape is safe?)
    output, error = process.communicate(
        "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html\nquit\n",
        timeout=10
    )

    #     # ın terminal output must have title or stock
    assert "Product:" in output or "PRODUCT:" in output
    assert "Price history" in output or "price record" in output