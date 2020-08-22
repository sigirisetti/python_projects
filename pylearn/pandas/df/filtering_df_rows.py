import pandas as pd
import numpy as np

np.random.seed(1234)

data = np.random.randn(8, 4)  # 5x2 matrix of N(0, 1) random draws
dates = pd.date_range('28/12/2010', periods=8)

df = pd.DataFrame(data, columns=('id', 'price', 'weight', 'quality'), index=dates)

print(df)
print(df.mean())

print(df['id'][0])

# First two rows 0,1
print(df[0:2])

# Rows 2,3,4
print(df[2:5])

# Gets last one row as df
print(df[-1:])

# Retains df except last one row
print(df[:-1])

# Positive prices
print(df[df["price"] > 0])

# Positive prices
print(df[(df["price"] > 0) & (df["price"] < 1)])
