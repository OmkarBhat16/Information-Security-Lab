from numpy import char

alphabets = "abcdefghijklmnopqrstuvwxyz"
mapping = {}

def playfair_cipher(text: str,key: str):
    result = ""
    text = text.replace(" ","")
    if len(text)%2 != 0:
        text += 'x'

    ls = []
    matrix = [['a']*5 for _ in range(5)]
    for ch in key:
        if ch not in ls:
            ls.append(ch)

    for ch in alphabets:
        if ch != 'j' and ch not in ls:
            ls.append(ch)

    for i in range(5):
        for j in range(5):
            matrix[i][j] = ls[i*5+j]
            mapping[ls[i*5+j]]=(i,j)

    for i in range(5):
        print(matrix[i])

    i , j = 0 , 1
    while i < len(text) and j < len(text):
        l1 , l2 = text[i] , text[j]
        l1_co , l2_co = mapping[l1], mapping[l2]
        print(l1 , l1_co , l2 , l2_co)
        if(l1_co[0] == l2_co[0]):
            result += matrix[l1_co[0]][(l1_co[1]+1)%5]
            result += matrix[l2_co[0]][(l2_co[1]+1)%5]
        elif(l1_co[1] == l2_co[1]):
            result += matrix[(l1_co[0]+1)%5][l1_co[1]]
            result += matrix[(l2_co[0]+1)%5][l2_co[1]]
        else:
            result += matrix[l1_co[0]][l2_co[1]]
            result += matrix[l2_co[0]][l1_co[1]]
        i+=2
        j+=2

    return result


result = playfair_cipher("we are discovered","monarchy")
print("Playfair cipher : ", result)
print(result == "ugrmkcsxhmufmkzx")
