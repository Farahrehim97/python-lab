def perfectSquares(l, r):
    for i in range(l, r + 1):
        if (i**(.5) == int(i**(.5))):
            if(i%2==0):
                print(i, end=" ")
l = 1000
r = 9999
 
perfectSquares(l, r)
