from Crypto.Cipher import AES

message = b"Sensitive Information"
key = b"0123456789ABCDEF0123456789ABCDEF"

cipher = AES.new(key,AES.MODE_EAX)
nonce = cipher.nonce

ciphertext, tag = cipher.encrypt_and_digest(message)
print("Cipher text : ",ciphertext)

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
print("Plain text : ",plaintext)
