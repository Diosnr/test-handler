import requests
import json
from datetime import datetime

def fetch_btc_price():
    """
    Fetches current BTC/USD price from CoinGecko public API.
    No API key required.
    """
    try:
        # CoinGecko free API endpoint
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "bitcoin",
            "vs_currencies": "usd"
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        btc_price = data["bitcoin"]["usd"]
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"[{timestamp}] BTC Price: ${btc_price:,.2f} USD")
        return btc_price
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching BTC price: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Error parsing response: {e}")
        return None

if __name__ == "__main__":
    fetch_btc_price()
