"""
Title      : NYSE Stocks
Description: Gets historical prices of NYSE stocks given list of tickers.
Author     : Bernardo Paulsen
Version    : 1.0.0
"""


import pandas as pd
import pickle
import yahoo


with open("tickers.pickle","rb") as file:
    tickers = pickle.load(file)

print(len(tickers))

i  = 0
l  = len(tickers)
df = pd.DataFrame()
print(i)
for ticker in tickers:
    i += 1
    try:
        stock      = yahoo.get(ticker,(1991,1,1),(2021,1,1))
        df[ticker] = stock["Ret"]
        print(i/l, f"{ticker} OK")
    except:
        print(i/l, f"{ticker} --")


with open("prices.pickle","wb") as file:
    pickle.dump(df,file)

