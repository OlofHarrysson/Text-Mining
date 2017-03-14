import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.util import *
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import words


text = None
with open('sentences.txt', 'r') as f:
    text = f.read()

sentences = nltk.sent_tokenize(text)
print("Sentences are ------------------------------------------------------")
print(sentences)

tokens = [nltk.word_tokenize(sent) for sent in sentences]
print("Tokens are ------------------------------------------------------")
print(tokens)

stemmer = PorterStemmer()
tokens = nltk.word_tokenize(text)
stems = {token:stemmer.stem(token) for token in tokens}
print("Stems are ------------------------------------------------------")
print(stems)

lemmatizer = WordNetLemmatizer()
tokens = nltk.word_tokenize(text)
lemmas = {token:lemmatizer.lemmatize(token) for token in tokens}
print(lemmas)

tokens = [nltk.word_tokenize(sent) for sent in sentences]
tagged = [nltk.pos_tag(sent) for sent in tokens]
print("Tagged are ------------------------------------------------------")
print(tagged)

tokens = nltk.word_tokenize(text)
tagged = nltk.pos_tag(tokens)
ne_chunked = nltk.ne_chunk(tagged, binary=True)
print("ne_chunked are ------------------------------------------------------")
print(ne_chunked)

vader_analyzer = SentimentIntensityAnalyzer()
print("vader_analyzer are ------------------------------------------------------")
print(vader_analyzer.polarity_scores(text))
