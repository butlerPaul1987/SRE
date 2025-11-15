# Morrisons Product Scraper
A Python-based web scraper for extracting product information from Morrisons online grocery store, including product names and pricing details.

## Features
- Scrapes product information from Morrisons groceries website
- Extracts both standard and reduced pricing
- Automatic retry mechanism for failed requests
- Comprehensive logging system
- Built-in rate limiting to avoid overwhelming the server
- XPath-based parsing with fallback support

### Requirements
- Python 3.6+
- requests
- beautifulsoup4
- lxml

### Installation
Clone the repository:
```bash
git clone https://github.com/butlerPaul1987/SRE/Python/webscraper/morrisons-scraper.git
cd morrisons-scraper
```
Install required dependencies:
```
pip install requests beautifulsoup4 lxml
```

## Project Structure
```
.
├── main.py                 # Main application entry point
└── common/
    ├── API.py             # API parser and scraping logic
    ├── exceptions.py      # Custom exception classes
    └── logger.py          # Logging configuration
```
### Usage
Basic Usage

Edit the ```ProdList``` dictionary in ```main.py``` with your desired products:
```python
ProdList = {
    "111127143": "dr-pepper-zero-8-x-330ml",
    "113327237": "sour-patch-kids-watermelon-130g"
}
```
Run the scraper:
```python
python main.py
```
Adding Products
Products are defined using their product ID and URL slug:
```python
"<product_id>": "<product-url-slug>"
```

You can find these in the Morrisons product URL structure:
```
https://groceries.morrisons.com/products/{product-slug}/{product-id}
```

### Features in Detail
Retry Mechanism
The scraper includes an automatic retry decorator that will attempt failed requests up to 3 times with a 2-second delay between attempts:
```python
@retry((TokenFailed, APIParseFailed), tries=3, delay=2)
```
"Rate Limiting"
```python


time.sleep(random.random() * 4 + 2.5)
```

### Logging

All operations are logged with timestamps and severity levels:
- `INFO`: Successful operations and scraped data
- `WARNING`: Non-critical issues
- `ERROR`: Recoverable errors
- `CRITICAL`: Fatal errors that stop execution

### Exception Handling

Custom exceptions for different failure scenarios:
- `TokenFailed`: Authentication or token issues
- `APIParseFailed`: HTML parsing failures
- `ProductNotFound`: Product not available or page structure changed
- `RetryLimitExceeded`: Maximum retry attempts reached

### Output

The scraper logs the following information for each product:
```
2025-11-15 14:30 - INFO      - URL: https://groceries.morrisons.com/products/...
2025-11-15 14:30 - INFO      - Product: Dr Pepper Zero 8 x 330ml
2025-11-15 14:30 - INFO      - Reduced: £3.00
2025-11-15 14:30 - INFO      - Normal: £4.50
```
