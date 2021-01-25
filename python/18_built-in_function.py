#python 내장 함수들
print(abs(-3))

print(all([1, 2, 3])) # 입력: iterable type, 반환값: 값이 모두 참이면 True
print(any([0, ''])) # 입력: iterable type, 반환값: 하나라도 참이면 True

print(chr(97)) # ascii code -> char
print(ord('a')) # char -> ascii code

print(dir([1, 2, 3])) # 객체가 자체적으로 가지고 있는 변수, 함수 반환

k  = divmod(7, 3) # (몫, 나머지) 반환
print(k)

for i, name in enumerate(['body', 'foo', 'bar']): # enumerate: ordered type을 입력받아 enumerate 객체 반환
    print(i, name)

print(eval('1+2')) # eval: 실행 가능한 문자열 입력받아 실행한 값 반환

print(hex(234)) # hex: 정수 -> 16진수
print(oct(342391)) # oct: 정수 -> 8진수

print(min('python')); print(max('python'))
print(round(3.6)) # 반올림

print(sorted([3, 1, 2]))

#is_instance.py
class Person: pass
a = Person()

print(isinstance(a, Person)) # a가 Person 클래스의 인스턴스인지 확인

#filter1.py
def positive(x):
    return x > 0

li = list(filter(positive, [1, -3, 2, 0, -5, 6])) # filter(func_name, list): list의 값들을 차례로 함수에 대입
print(li)                                         # 함수의 반환 값이 참인 값들만 돌려준다.

#map1.py
def two_times(x): return x * 2

li = list(map(two_times, [1, 2, 3, 4]))
print(li)