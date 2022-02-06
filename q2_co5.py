f=open("co5.txt","w")
f.write("python files program \n lab course outcome 5\n file operation in python\nprogram no 2 in co5")
f.close()
f=open("co5","r")
i=1
for x in f:
    if(i%2 !=0):
        f1=open("temp.txt","a")
        f1.write(x)
    i=i+1
f.close()
f1.close()
f=open("temp.txt","r")
print(f.read())
