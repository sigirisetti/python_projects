import pandas as pd
import numpy as np

np.random.seed(1234)

data = np.random.randn(10, 4)  # 5x2 matrix of N(0, 1) random draws

df = pd.DataFrame(data, columns=('id', 'price', 'weight', 'quality'))
print(len(df))

df = df.drop(df.index[[1,3]])
def chg():
    for i,r in df.iterrows():
        df.at[i,'quality']=i

chg()
print(df)

df=df.reset_index(drop=True)
print(df)
