import random
def getRandomString(leng):
    ls = []
    for i in range(0,leng):
        ls.append(chr(random.randint(97,122)))
    return ''.join(ls)

usedAlphabet = []
def createAlphabet():
    alphabet = chr(random.randint(97,122))
    global usedAlphabet
    while alphabet in usedAlphabet:
        alphabet = chr(random.randint(97,122))
        
    usedAlphabet.append(alphabet)
    return alphabet
    
def eatingCheese():
        this = createAlphabet()       
        print("Start eating '" + this + "'")
        print("Eaten alphabet of cheese : ", end='')
        for i in usedAlphabet:
            print(i, end=' ')
        print()
        print("Original cheese : " + cheese)

        global eaten
        for j in range(0, len(cheese)-1):
            if this == cheese[j]:
                eaten = eaten[:j] + '_' + eaten[j+1:]
        print("Current cheese status : " + eaten + '\n')
        
def final():
    print("Finally remained Cheese Status : ")
    print("Eaten alphabet of cheese : ", end='')
    for i in usedAlphabet:
        print(i, end=' ')
    print()
    print("Original cheese : " + cheese)
    print("Current cheese status : " + eaten)
     
cheeseSize = int(input("Input the length of the string: "))
cheese = getRandomString(cheeseSize)
eaten = cheese

print("Generated Cheese is '" + cheese + "'")
print("Mouse starts eating!!")
for i in range(0, 10):
    if eaten == '_'*cheeseSize:
        print('Out of cheese!')
        break
    else:
        eatingCheese()
if eaten != '_'*cheeseSize:
    final()
