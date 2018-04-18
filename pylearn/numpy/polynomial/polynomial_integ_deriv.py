import numpy as np

p = np.poly1d([2, 0, -1])

p2 = np.polyder(p)
print('derivative of p : ', p, ' is :', p2, ' Its value at 4 is : ', p2(4))

p3 = np.polyint(p)
print(p3)
print(p3(4) - p3(2))