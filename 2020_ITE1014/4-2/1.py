x = int(input())
def printLine(n):
    for i in range(1,n+1):
        print(i, end = ' ')
    print('\n')

for k in range(1, x+1):
    printLine(k)
for k in range(x, 0, -1):
    printLine(k)
