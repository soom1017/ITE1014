#for문 활용
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

#marks1.py
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print('%d번 학생 축하합니다. 합격입니다.' % number)

#range(10): 0~9, range(1, 11): 1~10
#marks3.py
for number in range(len(marks)):
    if marks[number] < 60: continue
    print('%d번 학생 축하합니다. 합격입니다' % (number+1))

#gugudan.py
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print(' ')

#리스트 내포(list comprehension) 사용
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num%2 == 0]
print(result)