from nltk.book import *

print('---------------       Length of text        ---------------')
print(len(text3))

print('---------------       Sorted Set of Words        ---------------')
print(sorted(set(text3)))

print('---------------       Word repeatition count         ---------------')
print(len(text3) / len(set(text3)))

print('---------------       Word count         ---------------')
print(text3.count("smote"))


def lexical_diversity(text):
    return len(text) / len(set(text))


def percentage(text, word):
    return 100 * text.count(word) / len(text)

print(lexical_diversity(text3))
print(percentage(text3, "smote"))

