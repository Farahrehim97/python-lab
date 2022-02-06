f=open("co5.txt","w")
f.write("good morning")
f.write("python lab")
f.close()
l=[]
f=open("co5.txt","r")
l=f.readlines()
f.close()
print(l)

