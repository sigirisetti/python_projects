import pandas as pd
import numpy as np

df = pd.DataFrame()

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df1 = df.append(pd.DataFrame(data))
df2 = df1.append(pd.DataFrame(data))

print(df2)
