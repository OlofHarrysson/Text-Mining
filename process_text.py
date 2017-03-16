import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.util import *
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import words
from string import punctuation
from nltk.corpus import stopwords
from nltk.corpus import brown
import matplotlib.pyplot as plt
from wordcloud import WordCloud


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
    stems_count = sorted(((stem_values.count(e), e) for e in set(stem_values)), reverse=True)

    print_nbr = 5
    stems_count = stems_count[:print_nbr]
    for stem in stems_count:
        print(stem)


def top_lemmas(lemmas):
    print("Lemmas count ------------------------------------------------------")
    lemma_values = list(lemmas.values())
    lemma_count = sorted(((lemma_values.count(e), e) for e in set(lemma_values)), reverse=True)

    print_nbr = 5
    lemma_count = lemma_count[:print_nbr]
    for lemma in lemma_count:
        print(lemma)


def top_nouns_verbs(tagged):
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

    verbs_count = verbs_count[:print_nbr]
    for verb in verbs_count:
        print(verb)


def top_entities(ne_chunked):
    print("Top Entities ------------------------------------------------------")

    data = {}
    for entity in ne_chunked:
        if isinstance(entity, nltk.tree.Tree):
            text = " ".join([word for word, tag in entity.leaves()])
            ent = entity.label()
            data[text] = ent
        else:
            continue
    print(data)


def top_sentiment_sentence(polarity_scores):
    sorted_negative = sorted(score.get('compound') for score in polarity_scores)
    sorted_positive = sorted((score.get('compound') for score in polarity_scores), reverse=True)

    print_nbr = 5
    print("Most negative sentences ------------------------------------------------------")
    for score in sorted_negative:
        print(score)

    print("Most positive sentences ------------------------------------------------------")
    for score in sorted_positive:
        print(score)

    print("Sum of sentiment is ------------------------------------------------------")
    sent_sum = sum(sorted_positive)
    print(sent_sum)


def identify_weird_words(tokens): # Currently to slow. Approx 3 sec to check one word
    # weird_words = []
    # brown_words = brown.words()

    # for word in tokens:
    #     if word not in brown_words:
    #         weird_words.append(word)
    #         break;


    # print("Weird words are ------------------------------------------------------")
    # print(weird_words)
    pass


def disp_text(text):
    wordcloud = WordCloud().generate(text)

    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


# ------------------------------ START -----------------------------------
text = None
with open('sentences.txt', 'r') as f:
    text = f.read()

sentences = nltk.sent_tokenize(text)

# Splits into words
sent_tokens = [nltk.word_tokenize(sent) for sent in sentences]
word_tokens = nltk.word_tokenize(text)

# Removes punctuation and stop words such as "and, the, is..."
stops = stopwords.words('english')
temp = []
for sent_t in sent_tokens:
    no_punct = [token for token in sent_t if token not in punctuation]
    temp.append([token for token in no_punct if token not in stops])

sent_tokens = temp
word_tokens = [token for token in word_tokens if token not in punctuation]
word_tokens = [token for token in word_tokens if token not in stops]

# Stems are basic versions of words
stemmer = PorterStemmer()
stems = {token:stemmer.stem(token) for token in word_tokens}

# Lemmas look at the meaning of the word
lemmatizer = WordNetLemmatizer()
lemmas = {token:lemmatizer.lemmatize(token) for token in word_tokens}

tagged_sent = [nltk.pos_tag(sent) for sent in sent_tokens]

tagged_words = nltk.pos_tag(word_tokens)
ne_chunked = nltk.ne_chunk(tagged_words, binary=True)

vader_analyzer = SentimentIntensityAnalyzer()
polarity_scores = [vader_analyzer.polarity_scores(sent) for sent in sentences]



top_tokens(word_tokens)
top_stems(stems)
top_lemmas(lemmas)
top_nouns_verbs(tagged_sent)
top_entities(ne_chunked)
top_sentiment_sentence(polarity_scores)
identify_weird_words(word_tokens)
disp_text(text)
