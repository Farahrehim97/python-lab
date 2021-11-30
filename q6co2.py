from collections import Counter
test_str = input("enter a string")
res = Counter(test_str)
print ("Count of all characters in string is :\n "
                                           +  str(res))
