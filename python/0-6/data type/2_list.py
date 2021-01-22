#리스트 관련 함수
odd = [1, 3, 5]
print(odd[1] + odd[2])
print(odd[-2])

a = [1, 2, 8, 5, ['apple', 'banana', ['kiwi']]]
print(a[4][2][0])

del a[4]
a.append(3)
a.sort()
print(a)

a.reverse()
print(a)

a = [1, 2, 3]
print(a.index(3))

a.insert(1, 0)
a.remove(2)
a.pop(0)
print(a)

a.extend([3, 4, 8, 8, 3, 5])
print(a.count(3))