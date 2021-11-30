l1=[11,21,22,24,26,66,86,69]
print(l1)
l2=[]
for x in l1:
    if(x%2==0):
        l2.append(x)
print("Even number list is")
for x in l2:
    print(x,end=" ")
