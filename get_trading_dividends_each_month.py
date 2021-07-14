# ========= PLEASE READ CAREFULLY ==========
# Code credits to Algovibes
# Youtube Channel: 
# https://www.youtube.com/channel/UC87aeHqMrlR6ED0w2SVi5nw
# How To Get a Dividend EACH Month Using Python [Dividend Scraper]
# https://www.youtube.com/watch?v=BGG4t8VvlMo
# Disclaimer: This code is no Investment advice and is only for educational and entertainment purposes.
# ===========================================
# ===========================================

# import yahoo finance to get x stock's dividend dates
import yfinance as yf
# import pandas for data handling
import pandas as pd
# import datetiem for date manipulations
import datetime as dt

# get x dividends for a particular stock
# storing a ticker object, 'Apple' for example
var = yf.Ticker('AAPL')

# pull the 5 years history method for 'Apple'
var.history(period='5y')
# print(var.history(period='5y'))

# use the dividends method in the last 5 year
var.dividends
# print(var.dividends)

# create a variable to get dividends for multiple stocks from Down Jones Industrial Average
tickers = pd.read_html('https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average')[1]
# print(tickers)

# store ticker symbols into a list
tickers = tickers.Symbol.to_list()
# print(tickers)

# store dividends in an empty list
divs = []

# populate list looping through tickers list
# looping through ticker symbols
for i in tickers:
    # store in an instance the ticker, providing ticker's symbols
    inst = yf.Ticker(i)
    # use the history method in 1 year period
    inst.history(period='1y')
    # appending dividends to the empty list
    divs.append(inst.dividends)
# getting a list containing average dividend dates in the last year
# print(divs)

# store in a data frame the list created with ticker symbols in columns
df = pd.DataFrame(divs, index=tickers)
# store the month values
df.columns = df.columns.month
# print(df)

# store the sum of column group of each month
df = df.groupby(df.columns, axis=1).sum()

# Provide fake month's name of the date to header
df.columns = [dt.date(1900, i, 1).strftime('%b') for i in df.columns]
# print(df)

# check out if in January are dividends
df[df.Jan > 0]
# print(df)

# check out if in January or February are dividends
df[(df.Jan > 0) | (df.Feb >0)]
print(df)