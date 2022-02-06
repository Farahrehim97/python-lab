f = open("first.txt", "a")
f.write("welcome everyone!")
f.close()

f1 = open("second.txt", "a")
f1.write("good morning!")
f1.close()

with open('first.txt','r') as firstfile:
    with open('second.txt','a') as secondfile:
        for line in firstfile:
            secondfile.write(line)
f=open("second.txt","r")
print(f.read())
