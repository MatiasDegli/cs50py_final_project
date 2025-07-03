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
    group.add_argument("-p", "--price", action="store_true", help="See BTC actual price")
    parser.add_argument("-b", "--backtest", action="store_true", help="Excecute backtest")
    args = parser.parse_args()

    if args.price:
        price = get_bitcoin_price()
        print(f"Bitcoin price: ${price}")
    elif args.backtest:
        df = load_asset_data()
        while(True):
            try:
                buy = input("Buy date (YYYY-MM-DD): ")
                sell = input("Sell date (YYYY-MM-DD): ")
                if not date.fromisoformat(buy) or not date.fromisoformat(sell):
                    raise ValueError
                break
            
            except ValueError:
                print("Invalid date")
        
        df = run_strategy(df, buy, sell)
        run_backtest(df)
        plot_close(df)

    
    
    
def get_bitcoin_price():
    
    url=f"https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    data = response.json()
    
def run_strategy():
    ...

def run_backtest():
    ...

def plot_close():
    ...

def load_asset_data():
    data = ""

if __name__ == "__main__":
    main()
