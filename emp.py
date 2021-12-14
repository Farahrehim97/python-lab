class employee:
    def __init__(self,name,empid,salary,dept):
        self.name=name
        self.empid=empid
        self.salary=salary
        self.dept=dept
    def display(self):
        if(self.salary>15000):
            print("name:",self.name)
            print("empid:",self.empid)
            print("salary:",self.salary)
            print("department:",self.dept)

l=[]
n=int(input("enter number of employees"))
for i in range(0,n):
    l.append(employee(input("enter name"),input("enter empid"),int(input("enter salary")),input("enter dapratment")))

for i in l:
    i.display()
    
