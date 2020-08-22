import pandas as pd
import numpy as np

s1 = pd.Series(index=True)
s1.append("a", "1")

print(s1)
s1.append(4)

print(s1)