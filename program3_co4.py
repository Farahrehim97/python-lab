class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        self.area=length*breadth

    def __gt__(self,other):
        if(self.area>other.area):
            return True
        else:
            return False

r1=rectangle(7,8)
r2=rectangle(11,3)
if(r1>r2):
    print("Rectangle 1 is greater")
else:
    print("Rectangle 2 is greater")


    
