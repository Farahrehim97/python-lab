class student:
    def __init__(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
    def display(self):
        print("rollNo=",self.roll)
        print("name=",self.name)
        print("course=",self.course)

class test:
    def __init__(self,mark):
        self.mark=mark
    def displaymarks(self):
        print("mark=",self.mark)

class details(student,test):
    def __init__(self,roll,name,course,mark,age):
        student.__init__(self,roll,name,course)
        test.__init__(self,mark)
        self.age=age
    def displaydetails(self):
        self.display()
        self.displaymarks()

d1=details(116,"farhana","mca",89,24)
d1.displaydetails()
