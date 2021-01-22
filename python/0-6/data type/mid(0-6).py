#7번
#join 함수의 입력으로 list, tuple도 가능
a = 'life is too short'
list1 = a.split()
print(list1)

result = ' '.join(list1)
print(result)

#8번
a = (1, 2, 3)
a = a + tuple([4])
print(a)

#10번
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

#11번
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

#12번
#a = b, b = [1, 2, 3]이므로 a와 b는 같은 객체를 가리킴
a = b = [1, 2, 3]
a[1] = 4
print(b)