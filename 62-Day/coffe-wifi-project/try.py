class Try:
    name = "Jams"
    def __init__(self):
        self.name = "ik"
        #print(self.__dict__)

    def mydict(self):
        print(__dict__)

ik = Try()
print(ik.__dict__)
print(Try.__dict__)
