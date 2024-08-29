from cryptography.hazmat.primitives.asymmetric import rsa, padding, dh
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_message(message, reciever):
    encrypted_message = reciever.getPublicKey().encrypt(
        message.encode(),  # Convert message to bytes
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_message



class System:
    msgs = []
    def __init__(self,type):
        self.publicKey , self.__privateKey = generate_rsa_key_pair()

    def addMessage(self,sender, message):
        self.msgs.append({sender,message})

    def listMessages(self):
        for idx,msg in enumerate(self.msgs):
            print(idx, msg)

        def readMessages(self):
            idx = int(input("enter message to read : "))
            if idx >= 0 and idx < len(self.msgs):
                sender,msg = self.msgs[idx]
                print(sender)
                print(msg)
                print(decrypt_message(msg))

    def getPublicKey(self):
        return self.publicKey

    def decrypt_message(self, encrypted_message):
        decrypted_message = self.__privateKey.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_message.decode()


a = System("a")
b = System("b")
c = System("c")

a.addMessage('b',encrypt_message('hello',))
a.listMessages()
