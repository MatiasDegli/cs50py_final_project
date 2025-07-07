import pytest
import pandas as pd
from project import run_backtest, load_asset_data, get_bitcoin_price

df = load_asset_data()

def test_get_bitcoin_price():
    price = get_bitcoin_price()
    assert isinstance(price, float)
    assert price > 0

def test_load_asset_data():
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "close" in df.columns

def test_run_backtest_output_format():
    test_df = df.loc["2020-01-01":"2020-12-31"].copy()
    usd_amount = 1000
    result = run_backtest(test_df, usd_amount)
    assert isinstance(result, str)
    assert "Buy price" in result
    assert "Sell price" in result
    assert "Profit" in result
    assert "Final amount in USD" in result

def test_run_backtest_profit_calculation():
    test_df = pd.DataFrame({
        "close": [100, 150]
    }, index=pd.date_range(start="2022-01-01", periods=2))
    usd_amount = 200
    result = run_backtest(test_df, usd_amount)
    assert "Profit:     50.00%" in result
    assert "Final amount in USD: $300.00" in result
