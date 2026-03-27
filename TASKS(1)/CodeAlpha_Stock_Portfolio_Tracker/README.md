# Stock Portfolio Tracker ✅

Simple command-line stock tracker that calculates the total investment based on manually provided quantities and a hardcoded price list.

## Goal
- Let users input stock tickers and quantities
- Use hardcoded dictionary for prices (example: `{"AAPL": 180, "TSLA": 250}`)
- Show per-stock value and total investment
- Optionally save results to a `.csv` or `.txt` file

## Requirements
- Python 3.8+

## Usage
1. Open a terminal in `CodeAlpha_Stock_Portfolio_Tracker`.
2. Run:

```
python stock_portfolio_tracker.py
```

3. Follow prompts to add tickers and quantities. Press Enter on the ticker prompt to finish entering stocks.
4. Choose whether to save the results and which format (`csv` or `txt`).

### Example session
```
$ python stock_portfolio_tracker.py
Simple Stock Portfolio Tracker
Hardcoded prices available:
  AAPL: $180.00
  TSLA: $250.00
  GOOG: $2750.00
  MSFT: $330.00
  AMZN: $130.00

Enter a ticker (or press Enter to finish): AAPL
Quantity (number of shares): 10
Using hardcoded price for AAPL: $180.00

Enter a ticker (or press Enter to finish): TSLA
Quantity (number of shares): 5
Using hardcoded price for TSLA: $250.00

Enter a ticker (or press Enter to finish):
--- Portfolio Summary ---
Ticker       Qty       Price       Value
AAPL       10.00     180.00    1800.00
TSLA        5.00     250.00    1250.00

Total investment: $3050.00
Would you like to save the result? (y/N): y
Format (csv/txt) [csv]: csv
Saved CSV to portfolio_20260203_153012.csv
```

## Notes
- If a ticker is not found in the hardcoded price list, you can optionally enter a manual price.
- Saved files will be timestamped (e.g., `portfolio_20260203_153012.csv`).

## Extending this project
- Replace hardcoded prices with live API lookups (e.g., Yahoo Finance)
- Add support for fractional shares and currency selection
- Add unit tests and CLI arguments

---
Enjoy! 🎯
