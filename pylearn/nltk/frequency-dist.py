from nltk.book import *

fdist1 = FreqDist(text1)
print(fdist1)

vocabulary1 = fdist1.keys()
print(vocabulary1)

print(fdist1['whale'])

# Words longer than 15 chars
V = set(text1)
long_words = [w for w in V if len(w) > 15]
print(sorted(long_words))


fdist5 = FreqDist(text5)
print(sorted([w for w in set(text5) if len(w) > 7 and fdist5[w] > 7]))