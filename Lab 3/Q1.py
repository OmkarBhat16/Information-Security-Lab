from Crypto.PublicKey import RSA

key = RSA.generate(1024)
n , e , d = key.n , key.e , key.d
print('modulus (n) :',n)
print('private exponent (e) :',e)
print('public exponent (d) :',d)

message = b"Asymmetric Encryption"


encrypted = pow(int.from_bytes(message,'big'),e, n)
print("encrypted string is : ", hex(encrypted))


decrypted = pow(encrypted, d , n)
print("decrypted string is : ", decrypted.to_bytes((decrypted.bit_length() + 7) // 8 , "big").decode())
