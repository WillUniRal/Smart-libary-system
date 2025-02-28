class test :
    def __init__(self):
        self.gyat = "ohio"

    @property
    def in_egypt(self) :
        print("you are getting")
        return self.gyat
    
    @in_egypt.setter
    def in_egypt(self,type_shiii):
        print(str(self.gyat)+" is now "+str(type_shiii))
        self.gyat = type_shiii

rizzler = test()
print(rizzler.in_egypt)

rizzler.in_egypt = "fanum tax","sigma"

print(rizzler.in_egypt)

rizzler.in_egypt = "livy dune just got fortnite danced on by baby gronk"

# ('fanum tax', 'sigma') tuple
