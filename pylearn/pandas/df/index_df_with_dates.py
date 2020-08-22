import pandas as pd
import numpy as np

np.random.seed(1234)

data = np.random.randn(8, 4)  # 5x2 matrix of N(0, 1) random draws
dates = pd.date_range('28/12/2010', periods=8)

df = pd.DataFrame(data, columns=('id', 'price', 'weight', 'quality'), index=dates)
print(df)
print(df.mean())
