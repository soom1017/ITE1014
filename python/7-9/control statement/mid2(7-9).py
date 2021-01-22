#2번
result = 0
i = 1
while i <= 1000:
    if i%3 == 0:
        result += i
    i += 1
print(result)

#3번
i = 0
while True:
    i += 1
    if i > 5: break
    print('*' * i)

#6번
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]
print(result)