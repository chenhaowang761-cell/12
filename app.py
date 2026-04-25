"""
Step 1: Get stock data from Yahoo Finance.

Goal: run this file and see Apple's recent stock prices in your terminal.

How to run:
    pip install -r requirements.txt
    python app.py
"""

import yfinance as yf


# TODO 1.1: change "AAPL" to any other ticker (e.g. "MSFT", "TSLA", "GOOGL")
ticker = "AAPL"

# Create a Ticker object — this is how yfinance talks to Yahoo
stock = yf.Ticker(ticker)

# Fetch the last 5 days of daily prices.
# history() returns a pandas DataFrame (think: a table).
data = stock.history(period="5d", interval="1d")

# Print the whole table
print(f"--- {ticker} last 5 days ---")
print(data)


# TODO 1.2: print just the Close prices.
#   Hint: data["Close"]

# TODO 1.3: print the latest (most recent) close price only.
#   Hint: data["Close"].iloc[-1]

# TODO 1.4: try different period / interval values.
#   period options:   1d, 5d, 1mo, 3mo, 1y, 5y, max
#   interval options: 5m, 30m, 1h, 1d, 1wk, 1mo
#   (some combinations don't work — find out which!)
