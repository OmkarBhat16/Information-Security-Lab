import math

alphabets = "abcdefghijklmnopqrstuvwxyz"

def getA(char):
    return (ord('A') if char >= 'A' and char <= 'Z' else ord('a'));

def vignere_cipher(text: str, key: str):
    result = ""
    key = (key * math.ceil(len(text)/len(key)))[:len(text)]
    for c1, c2 in zip(text,key):
        if c1 == " ":
            result += " "
        else:
            result += chr((ord(c1)+ord(c2)-getA(c1)-getA(c2))%26 + getA(c1))

    return result

def autokey_cipher(text : str, autokey : str):
    result = ""
    key = autokey + text[:-len(autokey)]
    for c1, c2 in zip(text,key):
        if c1 == " ":
            result+= " "
        else:
            result+= chr((ord(c1)+ord(c2)-getA(c1)-getA(c2))%26 + getA(c1))

    return result

text = "the house is being sold tonight"
result = vignere_cipher("text","dollars")
print("Vignere Cipher : ", result)

result = autokey_cipher(text,"h")
print("Autokey Cipher : ", result)
