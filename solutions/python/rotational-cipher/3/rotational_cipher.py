def rotate(text, key):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    cipher = []
    
    for char in text:
        alphabet = lower if char.islower() else upper
        char_i = alphabet.find(char)
        if char_i == -1:
            cipher.append(char)
        else:
            index = (char_i + key) % 26
            cipher.append(alphabet[index])

    return "".join(cipher)