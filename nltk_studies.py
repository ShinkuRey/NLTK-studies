import nltk
import string

import io
import numpy as np
from PIL import Image

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from collections import Counter

from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from nltk.stem import WordNetLemmatizer

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

"""
This code snippet defines several functions related to text analysis using the NLTK library. The functions include:

- read_file: Reads a file and returns the raw text, word tokens, and sentence tokens.
- max_length: Finds the word with the maximum length in a list of word tokens.
- unique_words: Removes stop words from a list of word tokens and returns the unique words and the number of unique words.
- token_number: Returns the number of tokens in a given string.
- average_words_length: Calculates the average length of words in a list of word tokens.
- average_sent_length: Calculates the average length of sentences in a list of sentence tokens.
- average_words_sent: Calculates the average number of words per sentence in a list of word tokens and sentence tokens.

Note: The code snippet also imports necessary modules and downloads the required NLTK resources.
"""

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

        lemmatizator = WordNetLemmatizer()
        english_stopwords = set(stopwords.words("english"))
        russian_stopwords = set(stopwords.words("russian"))
        stop_words = english_stopwords.union(russian_stopwords)
        punctuation = string.punctuation + "”“’»«—"
        translator = str.maketrans('', '', punctuation)

        raw_text = text.translate(translator).lower()


        word_tokens_wsw = [word for word in word_tokenize(raw_text) if word not in stop_words and word.isalpha()]
        word_tokens = word_tokenize(raw_text)
        sent_tokens = sent_tokenize(text)
        print(len(sent_tokens))
        return raw_text, word_tokens, sent_tokens, word_tokens_wsw


def max_length(word_tokens):
    max_length = 0
    max_length_word = ""

    for word in word_tokens:
        if len(word) > max_length:
            max_length = len(word)
            max_length_word = word

    return max_length, max_length_word

def unique_words(word_tokens):

    unique_words = set(word_tokens)
    unique_words_number = len(word_tokens)

    return unique_words, unique_words_number

def token_number(s):
    return len(s)

def average_words_length(word_tokens, raw_text):
    num = round(len(raw_text) / len(word_tokens), 2)
    return num

def average_sent_length(sent_tokens, raw_text):
    num = round(len(raw_text) / len(sent_tokens), 2)
    return num

def average_words_sent(word_tokens, sent_tokens):
    num = round(len(word_tokens) / len(sent_tokens), 2)
    return num


def word_cloud(word_tokens):
    text = " ".join(word_tokens)
    wordcloud = WordCloud(width=400, height=200, background_color="white").generate(text)
    plt.figure(figsize=(5, 2.5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img = Image.open(buf)

    word_counts = Counter(word_tokens)

    words_list = []

    for word, count in word_counts.items():
        words_list.append((word, count))

    sorted_list = sorted(words_list, key = lambda x: x[1], reverse=True)

    return img, sorted_list[:30]

def collocations(word_tokens, num=20):
    finder = BigramCollocationFinder.from_words(word_tokens)
    collocations_counts = {}
    for bigram, freq in finder.ngram_fd.items():
        collocations_counts[bigram] = freq
    collocations_list = []
    sorted_collocations = dict(sorted(collocations_counts.items(), key=lambda item: item[1], reverse=True))
    for i, (bigram, freq) in enumerate(sorted_collocations.items()):
        if i < num:
            collocations_list.append((bigram, freq))
        else:
            break
    
    return collocations_list
