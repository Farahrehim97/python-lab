def aliquot():
    s=0
    n=int(input("enter a number"))
    for i in range(1,n-1):
        if(n%i==0):
            s=s+i
    if(s==n):
        print("it is an aliquot number");
    else:
        print("it is not an aliquot number");
aliquot()        
