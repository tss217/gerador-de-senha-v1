import os
from MainDef import Generator

def dethMetal():
    list = os.listdir()

    if "passwordPath" in list:
        print("")
    else:
        mkdir = os.mkdir("passwordPath")
    
dethMetal()

def fileCreator(name,password):
    
    with open(f"passwordPath/{name}","w") as ofPassWord:
        ofPassWord.write(password)


name = input("nome do arquivo:")
size = int(input("Qual será o tamanho da senha?"))

passwordGenerator = Generator(name,size)
passwordGenerator.creat()

fileCreator(name,password = str(passwordGenerator.passWord))
