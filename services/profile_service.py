# how we safely store and retrieve user data

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import json

class ProfileService:
    def __init__(self, qifel):
        # We need Qifel to get our encryption keys
        self.qifel = qifel
        # Store encrypted profiles in memory for now
        self.encrypted_profiles = {}
        print("Profile Service started!")
    
    def save_profile(self, user_id, user_data):
        # Get our service-specific key from Qifel
        key = self.qifel.get_service_key(user_id, "profile_service")
        
        # Convert user data to JSON string, then to bytes
        profile_json = json.dumps({
            "name": user_data.name,
            "age": user_data.age
        })
        data_bytes = profile_json.encode('utf-8')
        
        # Encrypt the data
        aesgcm = AESGCM(key)
        nonce = os.urandom(12)
        encrypted_data = aesgcm.encrypt(nonce, data_bytes, None)
        
        # Store encrypted data + nonce
        self.encrypted_profiles[user_id] = {
            "data": encrypted_data,
            "nonce": nonce
        }
        print(f"Saved encrypted profile for {user_id}")
    
    def get_profile(self, user_id):
        # Check if we have data for this user
        if user_id not in self.encrypted_profiles:
            print(f"No profile found for {user_id}")
            return None
        
        # Get our key from Qifel
        key = self.qifel.get_service_key(user_id, "profile_service")
        
        # Get encrypted data
        stored = self.encrypted_profiles[user_id]
        
        # Decrypt
        aesgcm = AESGCM(key)
        decrypted_bytes = aesgcm.decrypt(stored["nonce"], stored["data"], None)
        
        # Convert back to readable data
        profile_json = decrypted_bytes.decode('utf-8')
        profile_data = json.loads(profile_json)
        
        print(f"Retrieved profile for {user_id}: {profile_data}")
        return profile_data