input_string=input("enter element")
user_list=input_string.split()
for i in range(len(user_list)):
    user_list[i]=int(user_list[i])
    if(user_list[i]>100):
        user_list[i]='over'

for i in range(len(user_list)):
    print(user_list[i],end=" ,")
    
