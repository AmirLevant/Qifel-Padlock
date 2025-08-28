import os
import user
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def microservice():
    amir = user.User("amir", 24, "Green")
    return amir.name


# Testing AES-GCM which is block cipher using Galois Counter Mode
def encryption_test():
    initialdata = microservice() # Data is amir
    final_data = b""+initialdata

    key = AESGCM.generate_key(bit_length=128) 
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    cipher_text = aesgcm.encrypt(nonce,final_data,None)


    # decrypting
    aesgcm.decrypt(nonce,cipher_text,None)







def main():
    #encryption_test
    initialdata = microservice() # Data is amir
    final_data = b""+initialdata

    print(final_data)
    



main()