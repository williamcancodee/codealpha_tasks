"""Stock Portfolio Tracker (simple)

This file implements a minimal command-line stock portfolio tracker that:
- Uses a hardcoded price dictionary for a small set of tickers
- Accepts user input for ticker and quantity
- Calculates per-stock and total investment value
- Optionally saves the result to a CSV or TXT file with a timestamp

This module is intentionally simple to demonstrate working with dictionaries,
I/O (input/print), basic arithmetic, and file handling.
"""

import csv
from datetime import datetime

# Simple, editable price list used throughout the script. Replace or extend as needed.
HARD_CODED_PRICES = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOG": 2750.0,
    "MSFT": 330.0,
    "AMZN": 130.0,
}


def prompt_nonempty(prompt_text):
    """Prompt repeatedly until a non-empty string is entered.

    Returns the trimmed user input.
    """
    while True:
        val = input(prompt_text).strip()
        if val:
            return val


def prompt_float(prompt_text):
    """Prompt repeatedly until a valid float is entered.

    Returns the parsed float. Keeps prompting on invalid input.
    """
    while True:
        val = input(prompt_text).strip()
        try:
            return float(val)
        except ValueError:
            print("Please enter a number (e.g., 10 or 3.5).")


def add_stock(portfolio):
    """Interactively add a single stock entry to the portfolio list.

    The function asks for a ticker and quantity, looks up a price in
    HARD_CODED_PRICES, or prompts the user for a manual price if needed.
    Returns True to continue adding more stocks, or False to finish.
    """
    # Ask for ticker; empty input means "done"
    ticker = prompt_nonempty("Enter ticker (or press Enter to finish): ").upper()
    if not ticker:
        return False

    # Ask for quantity (number of shares)
    qty = prompt_float("Quantity (number of shares): ")

    # Use the hardcoded price if available, otherwise allow manual entry
    if ticker in HARD_CODED_PRICES:
        price = HARD_CODED_PRICES[ticker]
        print(f"Using hardcoded price for {ticker}: ${price:.2f}")
    else:
        print(f"{ticker} not found in price list.")
        use_manual = input("Would you like to enter a price manually? (y/N): ").strip().lower()
        if use_manual == "y":
            price = prompt_float("Manual price per share: $")
        else:
            print("Skipping this ticker.")
            # Return True to continue the outer loop (user can add other tickers)
            return True

    # Append a dictionary representing the holding to the portfolio list
    portfolio.append({"ticker": ticker, "quantity": qty, "price": price})
    return True


def summarize(portfolio):
    """Compute per-stock values and print a formatted portfolio summary.

    Returns a tuple (rows, total) where rows is a list of tuples
    (ticker, quantity, price, value) and total is the total investment.
    """
    print("\n--- Portfolio Summary ---")
    total = 0.0
    rows = []

    # Build rows and accumulate total value
    for entry in portfolio:
        value = entry["quantity"] * entry["price"]
        rows.append((entry["ticker"], entry["quantity"], entry["price"], value))
        total += value

    # Nicely formatted table-like output
    print(f"{'Ticker':<8}{'Qty':>8}{'Price':>12}{'Value':>12}")
    for t, q, p, v in rows:
        print(f"{t:<8}{q:8.2f}{p:12.2f}{v:12.2f}")

    print(f"\nTotal investment: ${total:.2f}")
    return rows, total


def save_to_csv(rows, total):
    """Save the portfolio rows to a timestamped CSV file."""
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Ticker", "Quantity", "Price", "Value"])
        for t, q, p, v in rows:
            writer.writerow([t, q, p, v])
        writer.writerow([])
        writer.writerow(["Total", "", "", total])
    print(f"Saved CSV to {filename}")


def save_to_txt(rows, total):
    """Save the portfolio rows to a timestamped TXT file (tab-separated)."""
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Ticker\tQty\tPrice\tValue\n")
        for t, q, p, v in rows:
            f.write(f"{t}\t{q}\t{p}\t{v}\n")
        f.write(f"\nTotal\t\t\t{total}\n")
    print(f"Saved TXT to {filename}")


def main():
    """Main program flow: collect holdings, summarize, and optionally save."""
    print("Simple Stock Portfolio Tracker")
    print("Hardcoded prices available:")
    for k, v in HARD_CODED_PRICES.items():
        print(f"  {k}: ${v:.2f}")

    portfolio = []

    # Collect user input until a blank ticker is given
    while True:
        ticker = input("\nEnter a ticker (or press Enter to finish): ").strip().upper()
        if not ticker:
            break

        # Validate numeric quantity input
        try:
            qty = float(input("Quantity (number of shares): ").strip())
        except ValueError:
            print("Invalid quantity. Try again.")
            continue

        # Resolve price either from the hardcoded dict or via manual entry
        if ticker in HARD_CODED_PRICES:
            price = HARD_CODED_PRICES[ticker]
            print(f"Using hardcoded price for {ticker}: ${price:.2f}")
        else:
            ans = input(f"{ticker} not in price list. Enter price manually? (y/N): ").strip().lower()
            if ans == "y":
                try:
                    price = float(input("Price per share: $").strip())
                except ValueError:
                    print("Invalid price. Skipping ticker.")
                    continue
            else:
                print("Skipping ticker.")
                continue

        portfolio.append({"ticker": ticker, "quantity": qty, "price": price})

    # If user didn't enter anything, exit gracefully
    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    # Show summary and optionally save to file
    rows, total = summarize(portfolio)

    save = input("Would you like to save the result? (y/N): ").strip().lower()
    if save == "y":
        fmt = input("Format (csv/txt) [csv]: ").strip().lower() or "csv"
        if fmt == "csv":
            save_to_csv(rows, total)
        else:
            save_to_txt(rows, total)


if __name__ == "__main__":
    main()

