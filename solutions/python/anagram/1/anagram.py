def find_anagrams(word, candidates):
    word = word.lower()
    sorted_word = sorted(word)
    result = []
    
    for candidate in candidates:
        low_cand = candidate.lower()
        if low_cand == word:
            continue
        if sorted_word == sorted(low_cand):
            result.append(candidate)

    return result
    
