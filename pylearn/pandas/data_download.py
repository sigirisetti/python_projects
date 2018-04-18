import pandas_datareader.data as web

import datetime

start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2017, 5, 15)

# download from yahoo
# f = web.DataReader("AAPL", 'yahoo', start, end)


# download from google
f = web.DataReader("AAPL", 'google', start, end)

print(f.head())

# read current quotes
q = web.get_quote_google(['AMZN', 'GOOG'])
print(q)

goog = web.DataReader(["AAPL", "GOOG"],  "google", start, end)
print(goog)