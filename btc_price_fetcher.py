#!/usr/bin/env python3
"""
BTC Price Fetcher
Fetches current Bitcoin price from CoinGecko public API and displays it with timestamp.

Usage:
    python btc_price_fetcher.py

Requirements:
    pip install requests

Author: Handler
"""

import requests
from datetime import datetime


def fetch_btc_price():
    """
    Fetches current BTC price in USD from CoinGecko public API.
    
    Returns:
        tuple: (price, timestamp) if successful, (None, error_message) if failed
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        price = data["bitcoin"]["usd"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        return price, timestamp
    except requests.exceptions.RequestException as e:
        return None, str(e)


if __name__ == "__main__":
    price, timestamp = fetch_btc_price()
    
    if price:
        print(f"[{timestamp}] BTC Price: ${price:,.2f} USD")
    else:
        print(f"Error fetching BTC price: {timestamp}")
