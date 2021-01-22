a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a >= b:
    if a >= c:
        if b >= c:
            print('min: ' + str(c))
            print('max: ' + str(a)) # a >= b >= c
        else:
            print('min: ' + str(b))
            print('max: ' + str(a)) # a >= c > b
    else:
        print('min: ' + str(b))
        print('max: ' + str(c)) # c > a >= b

else: # b > a
    if b >= c:
        if c >= a:
            print('min: ' + str(a))
            print('max: ' + str(b)) # b >= c >= a
        else:
            print('min: ' + str(c))
            print('max: ' + str(b)) # b > a > c
    else:
        print('min: ' + str(a))
        print('max: ' + str(c)) # c > b > a
