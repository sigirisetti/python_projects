import numpy as np

n = np.random.uniform()
print('n = {0}'.format(n))

if n > 0.49:
    print('You win!')
else:
    print('you lose.')