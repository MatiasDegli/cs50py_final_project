import pandas as pd
import matplotlib.pyplot as plt
import requests
import sys
import argparse
import os
# import date

def main():
    parser = argparse.ArgumentParser(description="Simulador de trading")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-p", "--price", action="store_true", help="Ver precio actual de BTC")
    parser.add_argument("-b", "--backtets")
    args = parser.parse_args()
    
    
    
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
    ...

if __name__ == "__main__":
    main()
