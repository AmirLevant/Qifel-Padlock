import user
from user import User


def microservice():
    amir = user.User("amir", 24, "Green")
    print(amir.age)





def main():
    microservice()
    



main()