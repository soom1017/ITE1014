#변수 이해 확장
a = [1, 2, 3]
b = a  # [1, 2, 3]을 참조하는 변수가 2개로 늘어남
       # -> a와 b의 메모리 주소 동일 (같은 객체를 가리킴)
print(id(a)); print(id(b))
print(a is b)

a[0] = 4 #a를 바꾸면 b도 같이 바뀜
print(b) 

c = a[:] #1. [:] 사용 - a와 c는 다른 객체를 가리킴
print(a is c)

from copy import copy #2. copy module 사용
d = copy(a) 
print(a is d)

#변수 만들기
a, b = ('python', 'life') # == (a, b) = 'python', 'life'
print(a); print(b)

[c, d] = ['python', 'life']
print(c); print(d)

e = f = 'python'

num1 = 3
num2 = 5
num1, num2 = num2, num1
print(num1); print(num2)