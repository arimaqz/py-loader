from random import choice
from string import ascii_letters,digits
from sys import argv
from os import listdir,mkdir

XOR_KEY_LENGTH = 10

def crypt(filename,key=""):
    letters = ascii_letters+digits
    encrypt = False
    if(key == ""):
        encrypt=True
        for i in range(XOR_KEY_LENGTH):
            key += choice(letters)
    open_mode = "r" if key == "" else "rb"
    with open(filename,open_mode) as f:
        data = f.read().encode() if open_mode == "r" else f.read()
        data_array = bytearray(data) #modifable when bytearray    
        for i in range(len(data_array)):
            current_key = key[i % len(key)]
            data_array[i] ^=  ord(current_key)
        final = bytes(data_array)
        f.close()
    if encrypt:
        if "dist" not in listdir(): mkdir("dist")
        with open("dist/encrypted.out", "wb") as f:
            f.write(final)
            f.close()
        print("encrypted.out",key)
    else:
        return final
        
if __name__ == "__main__":
    action = argv[1]
    filename = argv[2]
    if action == "encrypt":
        crypt(filename)
    elif action == "execute":
        plain_py = crypt(filename,argv[3])
        exec(plain_py)