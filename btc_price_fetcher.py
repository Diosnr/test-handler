#!/usr/bin/env python3
"""
BTC Price Fetcher
Fetches current Bitcoin price from CoinGecko public API and prints it with timestamp.

Usage:
    python btc_price_fetcher.py

Requirements:
    pip install requests
"""

import requests
from datetime import datetime


def fetch_btc_price():
    """
    Fetch current BTC price from CoinGecko public API.
    
    Returns:
        float: Current BTC price in USD, or None if request fails
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
        
        btc_price = data['bitcoin']['usd']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        print(f"[{timestamp}] BTC Price: ${btc_price:,.2f} USD")
        return btc_price
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching BTC price: {e}")
        return None


if __name__ == "__main__":
    fetch_btc_price()
