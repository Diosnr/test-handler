# BTC Price Fetcher

A simple Python script that fetches the current Bitcoin (BTC) price from the CoinGecko public API and displays it with a timestamp.

## Features

- Fetches live BTC price in USD
- Displays formatted price with timestamp
- Uses CoinGecko's free public API (no API key required)
- Error handling for network issues

## Installation

```bash
pip install requests
```

## Usage

```bash
python btc_price_fetcher.py
```

## Example Output

```
[2026-06-03 02:07:24] BTC Price: $66,812.00 USD
```

## API Reference

This script uses the CoinGecko Simple Price API endpoint:
- **Endpoint**: `https://api.coingecko.com/api/v3/simple/price`
- **Rate Limit**: 10-50 calls/minute (free tier)
- **Documentation**: https://www.coingecko.com/en/api/documentation

## License

Open source - use freely.
