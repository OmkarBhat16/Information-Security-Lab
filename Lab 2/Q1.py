from Crypto.Cipher import DES

cipher = DES.new(b"A1B2C3D4",DES.MODE_OFB)

plaintext = b'Confidential Data'
msg = cipher.encrypt(plaintext)
# print(type(msg))
print(msg)

# pt = cipher.decrypt(msg)

# print(pt)
