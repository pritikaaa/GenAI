import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
sentence = "I am so onto genai"
tokens = word_tokenize(sentence)
trigrams = list(ngrams(tokens, 3))
print(trigrams)
bigrams = list(ngrams(tokens, 3 - 1))
print(bigrams)