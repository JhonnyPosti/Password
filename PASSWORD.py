import random
import string
import os
from time import sleep


def getHost(): 
    user = os.getlogin()
    return user

def Creat_pass(length):
    characteres = list(string.ascii_letters + string.digits + "!@#$%¨&*()" )
    password = []

    random.shuffle(characteres)
   
    for i in range(length):
        password.append(random.choice(characteres))
    
    random.shuffle(password)
    sleep(1)

    return str("".join(password))