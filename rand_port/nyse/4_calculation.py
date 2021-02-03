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
        means  = [gmean(stock + 1) for sotkc in stocks]
        mean   = np.sum(means)/20
        returns.append(mean)
    return returns


with open("pickle_files/cleaned.pickle","rb") as file:
    prices = pickle.load(file)


tickers = simulate_tickers(prices,10000)
returns = calculate_returns(prices,tickers)
print(returns)