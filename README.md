# BTC Price Fetcher

Live Python script that fetches current Bitcoin price from CoinGecko public API and displays it with a timestamp.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python btc_price_fetcher.py
```

## Output Example

```
[2026-06-03 02:14:13] BTC Price: $66,785.00 USD
```

## Features

- Uses CoinGecko public API (no API key required)
- Displays formatted price with timestamp
- Error handling for network issues
- 10-second timeout for reliability

## API

CoinGecko API endpoint: `https://api.coingecko.com/api/v3/simple/price`

No authentication required for basic price queries.
