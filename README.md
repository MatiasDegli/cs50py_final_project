# Bitcoin Trading Backtest

#### Video Demo: https://youtu.be/bcemaq-yutk

#### Description: 

A command-line tool that simulates Bitcoin investments using historical data. Users can check the current BTC price, run a manual backtest by selecting custom dates and investment, or execute a predefined test. The tool calculates profit or loss and plots the price chart using matplotlib.

This repository contains the final project for **CS50's Introduction to Programming with Python**.

## Requirements

- Python 3.13 or later
- pip

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv env
   ```

2. Activate the virtual environment:

   - On **Windows**:
     ```bash
     .\env\Scripts\activate
     ```

   - On **macOS/Linux**:
     ```bash
     source env/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

You can run the program in three different modes:

### 1. Check real-time BTC price
```bash
python project.py --price 
```

or

```bash
python project.py -p 
```

---

### 2. Manual backtest (you choose buy/sell dates and investment)
```bash
python project.py --backtest
```

or

```bash
python project.py -b
```

You will be prompted to enter:
- Buy date (YYYY-MM-DD)
- Sell date (YYYY-MM-DD)
- Amount of USD invested

The program will:
- Calculate profit/loss percentage
- Estimate final amount in USD
- Plot the price evolution in the selected period

---

### 3. Predefined test
```bash
python project.py --test
```

or

```bash
python project.py -t
```

Simulates an investment from `2021-01-01` to `2025-01-01`. You only input the amount invested.

---

## Data source

Historical Bitcoin data comes from the file `BTC_USD.csv`, which must be located in the same directory as `project.py`.
