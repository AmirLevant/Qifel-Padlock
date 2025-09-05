import os
import user
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def microservice():
    amir = user.User("amir", 24, "Green")
    return amir.name


# Testing AES-GCM which is block cipher using Galois Counter Mode
def encryption_test():
    initialdata = microservice() # Data is amir
    print("pre-encrypted data ") 
    print( initialdata)
    data = initialdata.encode("utf-8")

    key = AESGCM.generate_key(bit_length=128) 
    print("key:")
    print(key)

    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    cipher_text = aesgcm.encrypt(nonce,data,None)

    print("encrypted data ")
    print(cipher_text)

    # decrypting
    after_decrypt = aesgcm.decrypt(nonce,cipher_text,None)

    print("decrypted data " )
    print(after_decrypt )


def



def main():
    encryption_test()

    
    



main()