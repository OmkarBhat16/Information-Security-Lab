from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad, unpad
import time

def DES_encryption(plaintext: str, key: bytes) -> bytes:
    cipher = DES.new(key, DES.MODE_ECB)
    padded = pad(plaintext.encode(), DES.block_size)  # Convert plaintext to bytes and pad
    ciphertext = cipher.encrypt(padded)
    return ciphertext

def DES_decryption(ciphertext: bytes, key: bytes) -> str:
    cipher = DES.new(key, DES.MODE_ECB)
    deciphertext = cipher.decrypt(ciphertext)
    plaintext = unpad(deciphertext, DES.block_size).decode()  # Convert bytes to string
    return plaintext

def DES_run(plaintext: str, key: bytes):
    # Measure encryption time
    start_time = time.time()
    encrypted = DES_encryption(plaintext=plaintext, key=key)
    end_time = time.time()
    encryption_time = end_time - start_time
    print(f"DES encryption time: {encryption_time:.6f} seconds")
    print(f"Encrypted message (hex): {encrypted.hex()}")  # Display encrypted message in hex

    # Measure decryption time
    start_time = time.time()
    decrypted = DES_decryption(ciphertext=encrypted, key=key)
    end_time = time.time()
    decryption_time = end_time - start_time
    print(f"DES decryption time: {decryption_time:.6f} seconds")
    print(f"Decrypted message: {decrypted}")

def AES_encryption(plaintext: str, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(plaintext.encode(), AES.block_size)  # Convert plaintext to bytes and pad
    ciphertext = cipher.encrypt(padded)
    return ciphertext

def AES_decryption(ciphertext: bytes, key: bytes) -> str:
    cipher = AES.new(key, AES.MODE_ECB)  # Corrected from DES.new to AES.new
    deciphertext = cipher.decrypt(ciphertext)
    plaintext = unpad(deciphertext, AES.block_size).decode()  # Convert bytes to string
    return plaintext

def AES_run(plaintext: str, key: bytes):
    # Ensure key length is 16, 24, or 32 bytes for AES
    key = pad(key, AES.block_size)[:AES.block_size]

    # Measure encryption time
    start_time = time.time()
    encrypted = AES_encryption(plaintext=plaintext, key=key)
    end_time = time.time()
    encryption_time = end_time - start_time
    print(f"AES encryption time: {encryption_time:.6f} seconds")
    print(f"Encrypted message (hex): {encrypted.hex()}")  # Display encrypted message in hex

    # Measure decryption time
    start_time = time.time()
    decrypted = AES_decryption(ciphertext=encrypted, key=key)
    end_time = time.time()
    decryption_time = end_time - start_time
    print(f"AES decryption time: {decryption_time:.6f} seconds")
    print(f"Decrypted message: {decrypted}")

# Example usage
plaintext = "Performance Testing of Encryption Algorithms"
key = b"secretke"  # Initial key (8 bytes), will be padded or truncated for AES

# DES Run
DES_run(plaintext=plaintext, key=key)

# AES Run
AES_run(plaintext=plaintext, key=key)
