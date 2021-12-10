def amicable():
    s1=0
    s2=0
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    for i in range(1,a-1):
        if(a%i==0):
            s1=s1+i
    for i in range(1,b-1):
        if(b%i==0):
            s2=s2+i
    if(a==s2 and b==s1):
        print("it is an amicable pair");
    else:
        print("it is not an amicable pair");
amicable()        
