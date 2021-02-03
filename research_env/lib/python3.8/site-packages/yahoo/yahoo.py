import datetime as dt
import numpy as np
import pandas as pd
import pandas_datareader.data as web

def get(stock : str, start : tuple, end : tuple) -> pd.DataFrame:
    """
    Gets data from Yahoo Finance

    Parameters
    ----------
    stock : string
        Name of stock in Yahoo Finance

    start : tuple or list
        Initial date for the series, (YYYY,MM,DD)

    end : tuple or list
        Final date for the series, (YYYY,MM,DD)

    Returns
    -------
    object : pandas.DataFrame
    """
    start = dt.datetime(start[0],start[1],start[2])
    end = dt.datetime(end[0],end[1],end[2])
    prices = web.DataReader(stock, 'yahoo', start, end)
    prices['Ret'] = np.log(prices['Adj Close']/prices['Adj Close'].shift(1))
    return prices

def multiple(tickers: list, column: str, start: tuple, end : tuple) -> pd.DataFrame:
    """
    Gets data from Yahoo Finance for multiple tickers.
    
    Parameters
    ----------
    tickers : list
        List of tickers.
        
    column : string
        Column of stock given by get() to be added to dataframe.
        
    start : tuple or list
        Initial date for the series, (YYYY,MM,DD)

    end : tuple or list
        Final date for the series, (YYYY,MM,DD)
        
    """
    df = pd.DataFrame()
    n = len(tickers)
    i = 0
    for ticker in tickers:
        while  True:
            try:
                df[ticker] = get(ticker,start,end)[column]
                i += 1
                print(i)
                break
            except:
                pass
    return df
