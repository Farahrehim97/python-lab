l=["fara","amal","aabu"]
count=0
for x in range(len(l)):
    s=l[x]
    for y in s:
        if(y=='a'):
            count=count+1
print("Total number of a is",count)
