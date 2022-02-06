f = open("demofile2.txt", "a")
f.write("welcome everyone!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())
f = open("demofile2.txt", "r")
for fline in f:
    rslt = fline.title() 
    print(rslt)
