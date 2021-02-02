"""
Title      : BOVSP Tickers
Description: Gets tickers of all stocks listed on the BVSP from Wikipedia page.
Author     : Bernardo Paulsen
Version    : 0.9.0
"""


import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


options = Options()
options.add_argument('--headless')
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
with webdriver.Chrome("/home/ubuntu/projects/utilities/chromedriver",options=options) as chrome:
    tickers = []
    for letter in letters:
        print(letter)
        chrome.get(f"https://en.wikipedia.org/wiki/Companies_listed_on_the_New_York_Stock_Exchange_({letter})")
        time.sleep(.5)
        table   = chrome.find_element(By.XPATH, "//table")
        stocks  = table.find_elements(By.XPATH, "//td[2]")
        for stock in stocks:
            ticker = stock.text
            tickers.append(ticker)
        print(len(tickers))


with (open("tickers.pickle","wb")) as file:
    pickle.dump(tickers,file)
