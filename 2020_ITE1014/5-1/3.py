sentence = []
sentence = input().split()
dic = {}

for i in range(0, len(sentence)):
    a = 0
    for j in range (0, len(sentence)):
        if sentence[j] == sentence[i]:
            a = a + 1
            
    dic[sentence[i]] = a

for k in dic:
    print(k + ": " + str(dic[k]))

        

