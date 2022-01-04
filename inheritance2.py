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

s1=test(112,"farhana","MCA",78)

s1.displaymarks()
