from collections import Counter


def word_count(phrase):
    separated_words = phrase.lower().split()
    counter = Counter()
    for word in separated_words:
        counter[word] += 1
    return counter
