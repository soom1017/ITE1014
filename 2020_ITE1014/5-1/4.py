import random
def getRandomString(leng):
    ls = []
    for i in range(0,leng):
        ls.append(chr(random.randint(97,122)))
    return ''.join(ls)

a = int(input())
print(getRandomString(a).lower())


    
    
