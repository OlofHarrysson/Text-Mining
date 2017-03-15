import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.util import *
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import words





def top_tokens(word_tokens):
    print("Tokens count ------------------------------------------------------")
    tokens_count = sorted(((word_tokens.count(e), e) for e in set(word_tokens)), reverse=True)

    print_nbr = 5
    tokens_count = tokens_count[:print_nbr]
    for token in tokens_count:
        print(token)


def top_stems(stems):
    print("Stems count ------------------------------------------------------")
    stem_values = list(stems.values())
    print(stem_values)
    print(stems)
    stems_count = sorted(((stem_values.count(e), e) for e in set(stem_values)), reverse=True)

    print_nbr = 5
    stems_count = stems_count[:print_nbr]
    for stem in stems_count:
        print(stem)


def top_lemmas(lemmas):
    print("Lemmas count ------------------------------------------------------")
    lemma_values = list(lemmas.values())
    print(lemma_values)
    print(lemmas)
    lemma_count = sorted(((lemma_values.count(e), e) for e in set(lemma_values)), reverse=True)

    print_nbr = 5
    lemma_count = lemma_count[:print_nbr]
    for lemma in lemma_count:
        print(lemma)


def top_nouns_verbs(tagged):
    print(tagged)
    nouns = []
    verbs = []
    for tagged_sent in tagged:
        for tagg in tagged_sent:
            if tagg[1] == 'NN' or tagg[1] == 'NNS' or tagg[1] == 'NNP' or tagg[1] == 'NNPS':
                nouns.append(tagg[0])
            if tagg[1] == 'VB' or tagg[1] == 'VBD' or tagg[1] == 'VBG' or tagg[1] == 'VBN' or tagg[1] == 'VBP' or tagg[1] == 'VBZ':
                verbs.append(tagg[0])

    print("Nouns count ------------------------------------------------------")
    nouns_count = sorted(((nouns.count(e), e) for e in set(nouns)), reverse=True)

    print_nbr = 5
    nouns_count = nouns_count[:print_nbr]
    for noun in nouns_count:
        print(noun)

    print("Verbs count ------------------------------------------------------")
    verbs_count = sorted(((verbs.count(e), e) for e in set(verbs)), reverse=True)

    print_nbr = 5
    verbs_count = verbs_count[:print_nbr]
    for verb in verbs_count:
        print(verb)

def top_entities(text):
    pass

def top_sentiment(text):
    pass



# ------------------------------ START -----------------------------------
text = None
with open('sentences.txt', 'r') as f:
    text = f.read()

sentences = nltk.sent_tokenize(text)
print("Sentences are ------------------------------------------------------")
print(sentences)

sent_tokens = [nltk.word_tokenize(sent) for sent in sentences]
word_tokens = nltk.word_tokenize(text)

print("Sentence tokens are ------------------------------------------------------")
print(sent_tokens)

# Stems are basic versions of words
# stemmer = PorterStemmer()
# stems = {token:stemmer.stem(token) for token in word_tokens}
# print("Stems are ------------------------------------------------------")
# print(stems)

# Lemmas look at the meaning of the word
# lemmatizer = WordNetLemmatizer()
# lemmas = {token:lemmatizer.lemmatize(token) for token in word_tokens}
# print("Lemmas are ------------------------------------------------------")
# print(lemmas)

tagged = [nltk.pos_tag(sent) for sent in sent_tokens]
# print("Tagged are ------------------------------------------------------")
# print(tagged)

# tagged = nltk.pos_tag(word_tokens)
# ne_chunked = nltk.ne_chunk(tagged, binary=True)
# print("ne_chunked are ------------------------------------------------------")
# print(ne_chunked)

# vader_analyzer = SentimentIntensityAnalyzer()
# print("vader_analyzer are ------------------------------------------------------")
# print(vader_analyzer.polarity_scores(text))


# top_tokens(word_tokens)
# top_stems(stems)
# top_lemmas(lemmas)
top_nouns_verbs(tagged)



