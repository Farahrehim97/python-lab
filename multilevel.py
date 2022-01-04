class student:
    def __init__(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
    def display(self):
        print("rollNo=",self.roll)
        print("name=",self.name)
        print("course=",self.course)

class test(student):
    def __init__(self,roll,name,course,mark):
        student.__init__(self,roll,name,course)
        self.mark=mark
    def displaymarks(self):
        self.display()
        print("mark=",self.mark)

class details(test):
    def __init__(self,roll,name,course,mark,age):
        test.__init__(self,roll,name,course,mark)
        self.age=age
    def displaydetails(self):
        self.displaymarks()
        print("age=",self.age)

d1=details(112,"farhana","MCA",79,24)
d1.displaydetails()
