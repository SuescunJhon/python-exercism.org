def is_isogram(string):
    clean_string = [cha for cha in string.lower() if cha.isalpha()]
    return len(clean_string) == len(set(clean_string))
