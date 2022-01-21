class time:
    def __init__(self,hour,minute,sec):
        self.__hour=hour
        self.__minute=minute
        self.__sec=sec

    def __add__(self,other):
        return self.__hour+other.__hour,self.__minute+other.__minute,self.__sec+other.__sec

t1=time(3,22,35)
t2=time(5,40,34)
t3=t1+t2
print(t3)
