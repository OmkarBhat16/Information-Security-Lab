from cryptography.hazmat.primitives.asymmetric import rsa, padding, dh
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend


class KeyManager:
    def __init__(self):
        self.keys = {}

    def generate_rsa_key_pair(self, key_id):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        self.keys[key_id] = {
            'private': private_key,
            'public': public_key
        }

    def get_public_key(self, key_id):
        return self.keys[key_id]['public']

    def get_private_key(self, key_id):
        return self.keys[key_id]['private']

    def serialize_public_key(self, public_key):
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def deserialize_public_key(self, public_key_bytes):
        return serialization.load_pem_public_key(
            public_key_bytes,
            backend=default_backend()
        )

class DiffieHellmanKeyExchange:
    def __init__(self):
        self.parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

    def generate_private_key(self):
        return self.parameters.generate_private_key()

    def generate_shared_key(self, private_key, peer_public_key):
        shared_key = private_key.exchange(peer_public_key)
        return shared_key

class SecureCommunication:
    def __init__(self):
        self.key_manager = KeyManager()
        self.dh_key_exchange = DiffieHellmanKeyExchange()

    def setup_communication(self, system_id):
        self.key_manager.generate_rsa_key_pair(system_id)
        private_key = self.key_manager.get_private_key(system_id)
        public_key = self.key_manager.get_public_key(system_id)

        serialized_public_key = self.key_manager.serialize_public_key(public_key)
        return private_key, serialized_public_key

    def encrypt_message(self, public_key_bytes, message):
        public_key = self.key_manager.deserialize_public_key(public_key_bytes)
        encrypted_message = public_key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_message

    def decrypt_message(self, private_key, encrypted_message):
        decrypted_message = private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_message.decode()

# Example Usage
if __name__ == "__main__":
    comms = SecureCommunication()

    private_key_A, public_key_A = comms.setup_communication('SystemA')

    private_key_B, public_key_B = comms.setup_communication('SystemB')

    message = "This is a confidential message."
    encrypted_message = comms.encrypt_message(public_key_B, message)
    print(f"Encrypted message: {encrypted_message}")

    decrypted_message = comms.decrypt_message(private_key_B, encrypted_message)
    print(f"Decrypted message: {decrypted_message}")
