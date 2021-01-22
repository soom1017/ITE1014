def printStarDia(n):
    for i in range(1,n+1):
        for k in range(1,n-i+1):
            print(' ', end = '')
        for l in range(1,i+1):
            print('* ', end = '')
        print('\n')
    for i in range(n, 0, -1):
        for k in range(1,n-i+1):
            print(' ', end = '')
        for l in range(1,i+1):
            print('* ', end = '')
        print('\n')

x = int(input())
printStarDia(x)
