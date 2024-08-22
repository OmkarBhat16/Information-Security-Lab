from Crypto.Cipher import DES3

message = "Classified Text"
key = b"1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF"

def TDES_encryption(message: str, key: bytes ):
