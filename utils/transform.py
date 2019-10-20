""" File containing functions related to embedding of the words to vectors """

from nltk.tokenize import word_tokenize


def WordsToVec(word_list, text):
    "Function to map a list of texts to a list of vector from the word basis word_list"

    token_text = word_tokenize(text)
    features = {}
    for feat in word_list:
        features[feat] = (feat in token_text)

    return features
