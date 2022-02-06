f=open("co5.txt","w")
f.write("good morning")
f.write("python lab")
f.close()
l=[]
f=open("co5.txt","r")
for x in f:
    l=x
print(l)
