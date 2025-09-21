import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
nltk.download('punkt')
sample_text = 'This is soo fucking boring!!!'
tokens = word_tokenize(sample_text)
bigrams = list(ngrams(tokens, 2))
print('Bigrams:', bigrams)

# print('Tokens:', tokens)