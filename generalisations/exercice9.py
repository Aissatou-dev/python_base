a, b,r= 0,  1, 1
while r<=50:
    print(r, end=',')
    r = a + b
    a, b = b, r
