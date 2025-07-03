import pandas as pd
import matplotlib.pyplot as plt
import requests
import sys
import argparse
import os
from datetime import date

def main():
    parser = argparse.ArgumentParser(description="Trading simulator")
    group = parser.add_mutually_exclusive_group(required=True)

    # Defining possible arguments
    group.add_argument("-p", "--price", action="store_true", help="See BTC actual price")
    group.add_argument("-b", "--backtest", action="store_true", help="Excecute backtest")
    group.add_argument("-t", "--test", action="store_true", help="Run a predefined backtest")

    args = parser.parse_args()

    if args.price:
        if price := get_bitcoin_price():
            print(f"Bitcoin price: ${price}")
        else:
            sys.exit("Failed to fetch price.")

    elif args.backtest:
        df = load_asset_data()

        date_min = df.index.min().date()
        date_max = df.index.max().date()

        print(f"Data available from {date_min} to {date_max}")

        while(True):
            try:
                buy = input("Buy date (YYYY-MM-DD): ")
                sell = input("Sell date (YYYY-MM-DD): ")
                buy_date = date.fromisoformat(buy)
                sell_date = date.fromisoformat(sell)       
                trades = [buy_date, sell_date]
                if any(trade < date_min or trade > date_max for trade in trades) or sell_date < buy_date:
                    raise ValueError
                break
            
            except ValueError:
                print("Invalid date format")
        

        while(True):
            try:
                usd_amount = float(input("Amount of USD invested: "))
                break
            except ValueError:
                print("Invalid amount")


        df_filtered = df.loc[buy:sell].copy()
        run_backtest(df_filtered, usd_amount)
        plot_close(df_filtered)

    elif args.test:
        df = load_asset_data()

        while(True):
                try:
                    usd_amount = float(input("Amount of USD invested: "))
                    break
                except ValueError:
                    print("Invalid amount")
             
        df_filtered = df.loc["2021-01-01":"2025-01-01"].copy()
        run_backtest(df_filtered, usd_amount)
        plot_close(df_filtered)
    
def get_bitcoin_price():
    try:
        url=f"https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(url)
        data = response.json()
        return float(data["price"])
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None


# Shows profit or loss in the selected range
def run_backtest(df: pd.DataFrame, usd_amount):

    if df.empty:
        sys.exit("No data available for backtest.")

    buy_price = df["close"].iloc[0]
    sell_price = df["close"].iloc[-1]
    profit = ((sell_price - buy_price)/buy_price) * 100
    final_amount = usd_amount * (1 + profit / 100)
    
    print("\nBacktest result:📈") if profit >= 0 else print("\nBacktest result:📉")
    print(f"Buy price:  ${buy_price:.2f}")
    print(f"Sell price: ${sell_price:.2f}")
    print(f"Profit:     {profit:.2f}%")
    print(f"Final amount in USD: ${final_amount:.2f}")


# Plot price evolution in the selected range
def plot_close(df):
    if df.empty:
        sys.exit("No data available.")
    
    df["close"].plot(title="BTC price in selected range")
    plt.xlabel("date")
    plt.ylabel("price")
    plt.grid(True)
    plt.show()


# Loads data from a csv to a variable of DataFrame type
def load_asset_data():
    path = os.path.join(os.path.dirname(__file__), "BTC_USD.csv")
    df = pd.read_csv(path, parse_dates=["date"], dayfirst=False)
    df.set_index("date", inplace=True)
    return df


if __name__ == "__main__":
    main()
