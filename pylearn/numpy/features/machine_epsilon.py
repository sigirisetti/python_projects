import numpy as np

epss = np.finfo(np.float32).eps
print("Machine epeilon for single precision : ", epss)

epsd = np.finfo(np.float64).eps
print("Machine epeilon for double precision : ", epsd)
