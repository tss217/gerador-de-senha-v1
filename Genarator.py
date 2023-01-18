import random

class Generator:

    def __init__(self,name,size):
        self.name = name
        self.size = int(size)
        self.passWord = "::::::"
    
    def size(self):
        return self.size

    def passWord(self):
        return self.passWord

    def name(self):
        return self.name

    def creat(self):

        lowCase = "abcdefghijklmnopqrstuvwxyz"
        upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number ="0123456789"
        Symbols = "!@#%*&()[]:<>çÃ"

        mix = lowCase+upperCase+number+Symbols

        self.passWord = "".join(random.sample(mix,self.size))
