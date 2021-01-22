#불 자료형
print(2 > 1)
a = True
print(a)
print(type(a))

# 문자열, 리스트, 튜플, 딕셔너리는 안에 값이 없으면 False
b = [1, 2, 3, 4]
while b:
    b.pop()

if []:
    print('true')
else:
    print('false')

print(bool(''))

#숫자 자료형은 0이면 거짓
print(bool(3))