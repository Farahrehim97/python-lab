n=int(input("enter a number"))
a=0
b=1
print(a)
print(b)
for i in range(1,n):
    sum=a+b
    print(sum)
    a=b
    b=sum
