class time:
    def __init__(self,hour,minute,sec):
        self.hour=hour
        self.minute=minute
        self.sec=sec

    def __add__(self,other):
        return self.hour+other.hour,self.minute+other.minute,self.sec+other.sec

t1=time(3,22,35)
t2=time(5,40,34)
t3=t1+t2
print(t3)
