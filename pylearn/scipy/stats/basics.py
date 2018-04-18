import numpy as np

y = [8.1, 8.0, 8.1]

ybar = np.mean(y)
s = np.std(y, ddof=1)

print(ybar, s)


from scipy.stats.distributions import  t
ci = 0.95
alpha = 1.0 - ci

n = len(y)
T_multiplier = t.ppf(1.0 - alpha / 2.0, n - 1)

ci95 = T_multiplier * s / np.sqrt(n)

print('T_multiplier = {0}'.format(T_multiplier))
print('ci95 = {0}'.format(ci95))
print('The true average is between {0} and {1} at a 95% confidence level'.format(ybar - ci95, ybar + ci95))