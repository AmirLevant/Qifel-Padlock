import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class Qifel:
    def __init__(self):
        # This dictionary stores root keys for each user
        self.user_root_keys = {}
        print("Qifel key management system initialized!")

    def generate_root_key(self, user_id):
        # check if user already has a key
        if user_id in self.user_root_keys:
            print(f"User {user_id} already has a key!")
            return
        
        # Make a random 32-byte key, the user's "master key"
        root_key = os.urandom(32)
        self.user_root_keys[user_id] = root_key
        print(f"Made root key for user: {user_id}")

    def get_service_key(self, user_id, service_name):
        # Make sure user has a master key first
        if user_id not in self.user_root_keys:
            self.generate_root_key(user_id)
        
        root_key = self.user_root_keys[user_id]
        
        # master key + service name = unique service key
        hkdf = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=service_name.encode('utf-8'),  # Service name makes it different
        )
        
        derived_key = hkdf.derive(root_key)
        print(f"Made service key for {user_id} -> {service_name}")
        return derived_key
    
    def delete_user_keys(self, user_id):
        # remove the master key, now their data is unreadable!
        if user_id in self.user_root_keys:
            del self.user_root_keys[user_id]
            print(f"DELETED {user_id} - all their data is now garbage!")
        else:
            print(f"User {user_id} has no keys to delete")