class employee:
    def __init__(self):
        self.name=input("enter name")
        self.empid=input("enter empid")
        self.salary=int(input("enter salary"))
        self.dept=input("enter department")
    def display(self):
        if(self.salary>1500000):
            print("name:",self.name)
            print("empid:",self.empid)
            print("salary:",self.salary)
            print("department:",self.dept)

l=[]
n=int(input("enter number of employees"))
for i in range(0,n):
    l.append(employee())

for i in l:
    i.display()
    
