import random
numbers = []
for i in range(0,100):
    a= random.randint(1, 1000)
    numbers.append(a)

for j in numbers:
    print(j, end = ' ')
print('\n')

max_number = 1
for k in numbers:
    if k > max_number:
        max_number = k
print("max value: " + str(max_number))
    


    
