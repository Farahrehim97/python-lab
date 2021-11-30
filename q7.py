list1=[1,2,3]
list2=[5,6,7]
l1=len(list1)
l2=len(list2)
sum1=sum2=0
print(list1)
print(list2)
if(l1==l2):
    print("same length")
else:
    print("not same length")
for x in list1:
    sum1=sum1+x;
for y in list2:
    sum2=sum2+y;
if(sum1==sum2):
    print("sum is same")
else:
    print("sum is not same")
for x in range(l1):
    for y in range(l2):
        if(list1[x]==list2[y]):
            print(list1[x],"is there in both")
            
