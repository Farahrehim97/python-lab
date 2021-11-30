suml=input("enter elements")
slist=suml.split()
sum=0
for i in range(len(slist)):
    slist[i]=int(slist[i])
    sum=sum+slist[i]
print("sum of elements are:",sum);
