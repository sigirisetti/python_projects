from nltk.book import *

# exact search
print('---------------       Exact Search        ---------------')
print(text1.concordance("monstrous"))

# similarity search
print('---------------       Similarity Search 1       ---------------')
print(text1.similar("monstrous"))
print('---------------       Similarity Search 2       ---------------')
print(text2.similar("monstrous"))

# Dispersion plot
print('---------------       Dispersion Plot        ---------------')
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

# generating some random text
print('---------------       Generating random text        ---------------')
#print(text3.generate())

