import math
import numpy as np

def getA(char):
    return (ord('A') if char >= 'A' and char <= 'Z' else ord('a'));

def additive_cipher(text : str , num : int):
    result = ""
    for char in text:
        if char == " ":
            result += " "
        else :
            result += chr(((ord(char)- getA(char)) + num)%26 +getA(char))

    return result

def multiplicative_cipher(text : str , num : int):
    result = ""
    for char in text:
        if char == " ":
            result += " "
        else:
            result += chr(((ord(char)- getA(char)) * num)%26 +getA(char))

    return result

def affine_cipher(text: str , num1 : int , num2 : int):
    result = ""
    for char in text:
        if char == " ":
            result += " "
        else:
            result += chr(((ord(char)- getA(char))* num1 + num2)%26 +getA(char))

    return result

text = "I am learning information security"
print("Original Text :", text)
result = additive_cipher(text,20)
print("Additive Cipher : ", result)
result = multiplicative_cipher(text,15)
print("Multiplicative Cipher : ", result)
result = affine_cipher(text,15,20)
print("Affine Cipher : ", result)
