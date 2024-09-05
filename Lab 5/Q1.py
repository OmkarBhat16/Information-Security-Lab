hashes = set()
def hash(message):
    hashval = 5381
    for char , idx in zip(message,range(len(message))):
        hashval = (hashval * idx) ^ (hashval*33 + ord(char))

    hashes.add(str(hashval)[:32])

hash('abcd')
print(hashes)
