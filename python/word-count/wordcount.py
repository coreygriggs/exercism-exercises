from collections import Counter


def word_count(phrase): 
    return Counter(phrase.lower().split()) 
