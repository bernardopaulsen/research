"""
Title      : Random Portfolios
Description: Simulates random portfolios of 20 stocks each.
Author     : Bernardo Paulsen
Version    : 0.0.1
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
        tickers = []
        for e in range(20):
            while True:
                index  = np.random.randint(n_stocks)
                ticker = stocks[index]
                if ticker not in tickers:
                    tickers.append(ticker)
                    break
        all_tick.append(tickers)
    return all_tick

def calculate_returns(prices : pd.DataFrame(), tickers : list):
    n       = len(tickers)
    returns = []
    for ticks in tickers:
        stocks = [prices[tick].values for tick in ticks]
        means  = [gmean(stock + 1) for stock in stocks]
        mean   = np.sum(means)/20
        returns.append(mean)
    return returns

def simulate(prices,index):
    for n in [1000,10000,100000]:
        print(n)
        tickers = simulate_tickers(prices,n)
        returns = calculate_returns(prices,tickers)
        i = 0
        for ret in returns:
            if ret > gmean(index + 1):
                i += 1
        print(f"n={n}; {i/n*100:.2f}% maiores.")

with open("pickle_files/cleaned.pickle","rb") as file:
    prices = pickle.load(file)

sp500 = yahoo.get("^GSPC",(1991,1,1),(2021,1,1))["Ret"].values

simulate(prices,sp500)