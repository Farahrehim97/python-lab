class student:
    def __init__(self):
        self.name=input("enter name")
        self.rollno=input("enter rollno")
        self.mark1=int(input("enter mark1"))
        self.mark2=int(input("enter mark2"))
        self.mark3=int(input("enter mark3"))

    def display(self):
        print("name:",self.name)
        print("rollno:",self.rollno)
        print("mark1:",self.mark1)
        print("mark2:",self.mark2)
        print("mark3:",self.mark3)
        percent=((self.mark1+self.mark2+self.mark3)/300)*100
        print("Total Percentage: %.2f" %percent)

l=[]
n=int(input("enter number of students"))
for i in range(0,n):
    l.append(student())

for i in l:
    i.display()
