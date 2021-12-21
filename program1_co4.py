class rectangle:
    def __init__(self):
        self.length=int(input("enter length of rectangle"))
        self.breadth=int(input("enter breadth of rectangle"))
    def display(self):
        print("length:",self.length)
        print("breadth:",self.breadth)
    def area(self):
        a=self.length*self.breadth
        print("area is",a)
        return a
    def perimeter(self):
        p=2*(self.length+self.breadth)
        print("perimeter is",p)
r1=rectangle()
r2=rectangle()
print("first rectangle")
r1.display()
r1.perimeter()
a1=r1.area()
print("second rectangle")
r2.display()
r2.perimeter()
a2=r2.area()

if(a1>a2):
    print("First rectangle is larger")
else:
    print("Second rectangle is larger")
