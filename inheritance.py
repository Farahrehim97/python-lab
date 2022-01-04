class student:
    def getdata(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
    def display(self):
        print("rollNo=",self.roll)
        print("name=",self.name)
        print("course=",self.course)

class test(student):
    def getmarks(self,mark):
        self.mark=mark
    def displaymarks(self):
        self.display()
        print("mark=",self.mark)

s1=test()
s1.getdata(112,"farhana","MCA")
s1.getmarks(80)
s1.displaymarks()

            
