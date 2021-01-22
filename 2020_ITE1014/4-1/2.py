x = int(input())
y = int(input())
def add(first, second):
    return first+second
def sub(first, second):
    return first-second
def mul(first, second):
    return first*second
def div(first, second):
    return first/second
def mod(first, second):
    return first%second
def printMsg():
    print('completed')

print('sum: ' + str(add(x,y)))
print('difference: ' + str(sub(x,y)))
print('product: ' + str(mul(x,y)))
print('division: ' + str(div(x,y)))
print('remainder: ' + str(mod(x,y)))
printMsg()
