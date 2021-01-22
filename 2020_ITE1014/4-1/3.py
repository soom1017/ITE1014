n = int(input())
def addTotal(var):
    added = 0
    for i in range(1,var+1):
        added = added + i
    return added
def mulTotal(var):
    global gMul
    gMul = 1
    for i in range(1,var+1):
        gMul = gMul*i

print('addTotal(): '+str(addTotal(n)))
mulTotal(n)
print('gMul: '+str(gMul))
