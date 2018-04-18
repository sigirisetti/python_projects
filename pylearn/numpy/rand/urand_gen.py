import numpy as np

N = 10000
games = np.random.uniform(size=N)

wins = np.sum(games > 0.49)
losses = N - wins

print('You won {0} times ({1:%})'.format(wins, float(wins) / N))

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(games)
plt.show()