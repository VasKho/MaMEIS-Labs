import string
import itertools


def encypt_caesar(text: str, shift: int) -> str: 
    text = text.lower()
    result = "" 
 
    for i in range(len(text)): 
        result += chr((ord(text[i]) + shift - 97) % 26 + 97) 
    return result 


def decrypt_caesar(text: str, shift: int) -> str:
    result = ""

    for i in range(len(text)):
        result += chr((ord(text[i]) - shift + 26 - 97) % 26 + 97)
    return result


def caesar_brute_force(text: str, correct_text: str):
    variant = itertools.product(string.ascii_lowercase, repeat = len(text))
    for i in variant:
        str = ''.join(i)
        if str == correct_text:
            print(str)
            return str


if __name__ == "__main__":
    text = 'magic'
    shift = 4

    print(text)

    enc = encypt_caesar(text, shift)
    print(enc)

    caesar_brute_force(enc, text)
