import nltk
import os

print(os.listdir(nltk.data.find("corpora")))

sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
print(tokens)
tagged = nltk.pos_tag(tokens)
print(tagged[0:6])

# Identify named entities:
entities = nltk.chunk.ne_chunk(tagged)
print(entities)

# Display a parse tree:
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()