import pandas as pd
import numpy as np

np.random.seed(1234)

data = np.random.randn(8, 4)  # 5x2 matrix of N(0, 1) random draws
dates = pd.date_range('28/12/2010', periods=8)

df = pd.DataFrame(data, columns=('id', 'price', 'weight', 'quality'), index=dates)
x_mean = df.mean()

df.drop(['quality'], axis=1, inplace=True)

print(df.columns)
print(x_mean.keys)

for c in df.columns:
    if c not in x_mean:
        x_mean.pop()

print(x_mean.keys)
df.drop(['abc'], axis=1)