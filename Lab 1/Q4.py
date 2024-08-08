import math
import numpy as np

def getA(char):
    return (ord('A') if char >= 'A' and char <= 'Z' else ord('a'));

def split_text(text : str):
    pass

def hill_cipher(text: str, key):
    result = ""
    words = []
    for char in text:
        if char == " ":
            result += char
        else :
            character = np.matrix([ord(char)-getA(char)])
            print(character.size)
            multed = np.dot(character,key)[0]%26
            print(multed)
            # result += chr(np.dot(character,key)[0][0]%26)
    return result

text = "We live in an insecure world"
key = np.matrix([3,3,2,7]).transpose()
print(hill_cipher(text,key))
