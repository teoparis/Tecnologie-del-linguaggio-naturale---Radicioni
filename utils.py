"""
Shared preprocessing utilities for NLP exercises.
Each notebook imports this via: sys.path.insert(0, '..'); from utils import ...
The stopwords file is read relative to the notebook's working directory.
"""

import re
import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer


def get_stopwords(path="stop_words_FULL.txt"):
    """Load stopwords from file (relative to caller's working directory)."""
    with open(path, "r") as f:
        return [word.strip() for word in f]


def remove_punctuation(sentence):
    """Remove punctuation from a sentence string."""
    return re.sub(r'[^\w\s]', '', sentence)


def remove_stopwords(words_list, path="stop_words_FULL.txt"):
    """Filter stopwords from a list of words."""
    stopwords_list = get_stopwords(path)
    return [w.lower() for w in words_list if w.lower() not in stopwords_list]


def tokenize_sentence(sentence):
    """Tokenize, POS-tag, and lemmatize a sentence. Returns a list of lemmas."""
    lmtzr = WordNetLemmatizer()
    pos_map = {"NN": wn.NOUN, "VB": wn.VERB, "RB": wn.ADV, "JJ": wn.ADJ}
    words_list = []
    for word, tag in nltk.pos_tag(word_tokenize(sentence)):
        pos = pos_map.get(tag[:2])
        if pos:
            words_list.append(lmtzr.lemmatize(word, pos=pos))
    return words_list


def pre_processing(sentence):
    """Full preprocessing pipeline: remove punctuation → tokenize/lemmatize → remove stopwords."""
    return set(remove_stopwords(tokenize_sentence(remove_punctuation(sentence))))
