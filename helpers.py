def alphabet_position(letter):
    if letter.isupper():
        letter = ord(letter) - ord('A')
    elif letter.islower():
        letter = ord(letter) - ord('a')
    return letter

def rotate_character(char, rot):
    if char.isalpha:
        charp = alphabet_position(char)
        code = (((rot + charp) % 26) + ord('a'))
        code = chr(code)
        if char.isupper():
            code = code.upper()
    return code
