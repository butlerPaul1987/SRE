import requests
from bs4 import BeautifulSoup
from lxml import etree
from common.exceptions import TokenFailed, APIParseFailed, ProductNotFound, RetryLimitExceeded
import time
from common.logger import log_to_file

# xpath paths
headerxpath = '//*[@id="main"]/div/div[3]/div/div/h1'
headerxpath2 = '//*[@id="main"]/div/div[3]/div/div[1]/h1'
normpricexpath =  '//*[@id="main"]/div/div[3]/div/div/div[2]/span[2]'
normpricexpath2 = '//*[@id="main"]/div/div[3]/div/div[1]/div[2]/span'

def retry(exceptions, tries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < tries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt == tries:
                        raise RetryLimitExceeded(f"Retry limit exceeded: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator


class API_Parser:
    def __init__(self, URL: str):
        self.URL = URL

    @retry((TokenFailed, APIParseFailed), tries=3, delay=2)
    def getHTML(self):
        URL = self.URL
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept-Language': 'en-US,en;q=0.5'
        }
        data = requests.get(URL, headers=headers)
        if data.status_code != 200:
            raise APIParseFailed()
        soup = BeautifulSoup(data.content, "html.parser")
        dom = etree.HTML(str(soup))

        # --- Helper to check multiple XPaths ---
        def get_first_xpath(dom, *xpaths):
            for xp in xpaths:
                result = dom.xpath(xp)
                if result:  # non-empty list
                    return result[0].text.strip()
            return None

        try:
            Heading = get_first_xpath(dom, headerxpath, headerxpath2)                               # Product Name
            Red_price = get_first_xpath(dom, '//*[@id="main"]/div/div[3]/div/div/div[2]/span[1]',
                                       '//*[@id="main"]/div/div[3]/div/div[1]/div[2]/span[1]')      # Reduced Price
            Norm_price = get_first_xpath(dom, normpricexpath, normpricexpath2)                      # Normal Price

            if not Heading:
                raise ProductNotFound("Product name not found")

            log_to_file(f"{'Product'}: {Heading}", "INFO")
            log_to_file(f"{'Reduced'}: {Red_price}", "INFO")
            log_to_file(f"{'Normal'}: {Norm_price}", "INFO")

        except IndexError:
            raise ProductNotFound("Product not found")
        except Exception as e:
            raise APIParseFailed(f"Error parsing HTML: {e}")
