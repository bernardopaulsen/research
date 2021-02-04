"""
Title      : Random Portfolios
Description: Simulates random portfolios of 20 stocks each.
Author     : Bernardo Paulsen
Version    : 1.0.1
"""


import numpy as np
import pandas as pd
import pickle
from scipy.stats.mstats import gmean
import yahoo


def simulate_tickers(prices : pd.DataFrame, n : int):
    stocks   = prices.columns
    n_stocks = len(stocks)
    all_tick = []
    for i in range(n):
        while True:
            tickers = []
            for e in range(20):
                while True:
                    index  = np.random.randint(n_stocks)
                    ticker = stocks[index]
                    if ticker not in tickers:
                        tickers.append(ticker)
                        break
            if tickers not in all_tick:
                all_tick.append(tickers)
                break
        e = i + 1
        if not e%1000:
            print(e)
    return all_tick

def calculate_returns(prices : pd.DataFrame(), tickers : list):
    n       = len(tickers)
    returns = []
    i = 0
    for ticks in tickers:
        i += 1
        stocks = [prices[tick].values for tick in ticks]
        means  = [gmean(stock + 1) for stock in stocks]
        mean   = np.sum(means)/20 - 1
        returns.append(mean)
        if not i%100:
            print(i)
    return returns

def simulate(prices,index,n):
    print("Creating tickers...")
    tickers = simulate_tickers(prices,n)
    print("Simulating portfolios...")
    returns = calculate_returns(prices,tickers)
    print("Calculating relative returns...")
    i = 0
    e = 0
    for ret in returns:
        e += 1
        if ret > gmean(index + 1) - 1:
            i += 1
        if not e%100:
            print(e)
    return i/n
    print("Done.")


with open("pickle_files/cleaned.pickle","rb") as file:
    prices = pickle.load(file)
sp500 = yahoo.get("^GSPC",(1991,1,1),(2021,1,1))["Adj Close"]
sp500 = ((sp500 - sp500.shift(1))/sp500.shift(1)).values[1:]
n     = 10000


how_many = simulate(prices,sp500,n)


print(f"From {n} portfolios, {how_many*100:.2f}% had better returns than the S&P500.")