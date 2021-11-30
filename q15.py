def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i in li1 and i not in li2]
    return li_dif
 
li1 = ["yellow", "blue"]
li2 = ["blue","red"]
print(li1)
print(li2)
li3 = Diff(li1, li2)
print(li3)
