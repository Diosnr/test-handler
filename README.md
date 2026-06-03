# BTC Price Fetcher

Live Python script that fetches current Bitcoin (BTC) price in USD from CoinGecko public API.

## Requirements

```bash
pip install requests
```

## Usage

```bash
python btc_price_fetcher.py
```

## Output

```
[2024-06-03 14:32:15] BTC Price: $67,234.50 USD
```

## API

Uses CoinGecko free public API (no key required):
- Endpoint: https://api.coingecko.com/api/v3/simple/price
- Rate limit: ~50 calls/minute

## Notes

- Timeout set to 10 seconds
- Error handling for network issues and malformed responses
- Timestamp included in output
