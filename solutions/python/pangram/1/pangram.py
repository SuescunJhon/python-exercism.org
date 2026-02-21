def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence_set = set(sentence.lower())
    return len(alphabet.intersection(sentence_set)) == 26 
