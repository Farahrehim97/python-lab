n=int(input("Enter number of steps"))
print("1")
for j in range(2,n+1):
    print(j,end=" ")
    s=j
    for k in range(1,j):
        j=j+s
        print(j,end=" ")
    print(end="\n")
        
        
        
        
