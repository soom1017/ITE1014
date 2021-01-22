a = 'pithon'
b = a[:1] + 'y' + a[2:]
print(b)

number = 3
print("i eat %d apples" %number)

print('%10s' %'hi')

print('i eat {0} apples'.format(3))

print('i eat {number} apples'.format(number=5))

name = 'soom'
str1 = f'my name is {name}'
print(str1)

#문자열 관련 함수
#문자열은 immutable type
a = 'hobby'
num = a.count('b')
print(num)
num = a.find('c') #위치 찾아줌. 없으면 -1
num = a.index('b') #위치 찾아줌. 없으면 에러
str2 = ",".join('abcd')
print(str2)
a = 'HI'; b = 'hi'
print(a.lower())
print(b.upper())

str3 = ' hi '
print(str3.strip())
print(str3.replace('i', 'ello'))

str4 = 'life is too short'
print(str4.split())