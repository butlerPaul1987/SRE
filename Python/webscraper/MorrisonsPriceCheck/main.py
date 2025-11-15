import time
import random 
from common.exceptions import TokenFailed, APIParseFailed, ProductNotFound, RetryLimitExceeded
from common.API import API_Parser
from common.logger import log_to_file

# Product List
ProdList = {
    "111127143": "dr-pepper-zero-8-x-330ml",
    "113327237": "sour-patch-kids-watermelon-130g"
}

if __name__ == "__main__":
    try:
        # Iterate through your product dictionary
        for prodkey, prodvalue in ProdList.items():
            url = f"https://groceries.morrisons.com/products/{prodvalue}/{prodkey}"
            
            log_to_file(f"{'URL'}: {url}", "INFO")
            time.sleep(random.random() * 4 + 2.5)
            
            # Create parser instance
            API = API_Parser(URL=url)
            API.getHTML()
            
    except TokenFailed:
        log_to_file("Token failed", "CRITICAL")
    except APIParseFailed:
        log_to_file("APIParseFailed", "CRITICAL")
    except ProductNotFound as e:
        log_to_file(f"ProductNotFound: {e}", "CRITICAL")
    except Exception as e:
        log_to_file(f"Exception: {e}", "CRITICAL")

    
