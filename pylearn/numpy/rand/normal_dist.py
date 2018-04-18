import numpy as np
import matplotlib.pyplot as plt

mu = 0; sigma = 1

N = 5000
samples = np.random.normal(mu, sigma, N)

counts, bins, ignored = plt.hist(samples, 50, normed=True)

plt.plot(bins, 1.0/np.sqrt(2 * np.pi * sigma**2)*np.exp(-((bins - mu)**2)/(2*sigma**2)))
plt.show()