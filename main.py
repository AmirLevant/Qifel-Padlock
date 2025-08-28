import os
import user
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id


def microservice():
    amir = user.User("amir", 24, "Green")
    print(amir.name)





def main():
    microservice()
    



main()