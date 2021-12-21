class cosmetics:
    def __init__(self):
        self.prodcode=input("enter product code")
        self.prodname=input("enter product name")
        self.fruit=input("enter fruit name used")
        self.avail=input("is the fruit used in cosmetics (true/false)")
    def display(self,f):
        if(self.fruit==f and self.avail=='true'):
            print("product code",self.prodcode)
            print("product name",self.prodname)
            print("fruit name",self.fruit)
            print("fruit available",self.avail)
        else:
            print("fruit not there in the product")
c1=cosmetics()
f=input("enter the fruit to be searched")
c1.display(f)

