str=input("enter string")
str=str.split()
str2=[]
for i in str:
    if i not in str2:
        str2.append(i)
for i in range(0,len(str2)):
    print("frequency of",str2[i],"is",str.count(str2[i]))
    
