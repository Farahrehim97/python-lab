class cosmetics:
    def __init__(self):
        self.prodcode=input("enter product code")
        self.prodname=input("enter product name")
        self.fruit=input("enter fruit name used")
        self.avail=input("is the fruit used in cosmetics (true/false)")
    def display(self,f):
        if(self.fruit==f and self.avail=='true'):
            print("product details")
            print("product code",self.prodcode)
            print("product name",self.prodname)
            print("fruit name",self.fruit)
            print("fruit available",self.avail)

l=[]
n=int(input("enter the number of cosmetics"))
for i in range(0,n):
    l.append(cosmetics())
f=input("enter the fruit to be searched")
for i in l:
    i.display(f)

