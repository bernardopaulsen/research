"""
Title      : Clean Stocks
Description: Removes stocks with less than the maximum data length from dataframe.
Author     : Bernardo Paulsen
Version    : 1.0.0
"""


import pickle


with open("prices.pickle","rb") as file:
    df = pickle.load(file)


print(len(df.columns))
df = df[1:]
df = df.dropna(1)
print(len(df.columns))


with open("cleaned.pickle","wb") as file:
    pickle.dump(df,file)
