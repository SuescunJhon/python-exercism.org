def reverse(text):
    new_string = []
    for letter in text:
        new_string.insert(0, letter)

    return "".join(new_string)
