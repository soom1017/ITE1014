#함수 활용
def add(a, b):
    return a + b
print(add(3,4))

#반환값이 없는 함수를 반환값 있는 걸로 착각하고 쓰면
# None
def no_return(a, b):
    print('이 함수는 반환값이 없고, %d %d만 입력으로 받음' %(a, b))
c = no_return(3, 4)
print(c)

#매개변수 지정하여 호출
def justPrint(a, b):
    print(a)
    print(b)
justPrint(b=3, a=4) # 순서 상관X

#입력값이 몇 개가 될지 모를 때
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

added = add_many(3, 4, 5)
print(added)

#키워드 파라미터 - 입력 매개변수 앞에 **를 붙이면 매개변수는 딕셔너리가 됨
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(name='foo', age=3)

#return 값 응용
# return a+b, a*b -> (a+b, a*b) 튜플 반환
# return a+b; return a*b -> a+b 반환
# 함수를 단순히 빠져나가고 싶다면 return 단독으로 써도 됨.

#매개변수에 초기값 설정(default argument) - c/c++와 동일

#lambda로 함수 간결하게 표현 가능
add = lambda a, b: a+b
result = add(3, 4)
print(result)

#함수 안의 변수는 global 변수와 독립
#vartest_return.py
a = 'this_is_not_in_func'
def vartest():
    a = 'this_is_in_func'
    return a

print(vartest())
print(a)

#global 키워드 사용 - 함수 안에서 global 변수 사용
#vartest_global.py
a = 'this_is_not_in_func'
def vartest():
    global a
    a = 'this_is_in_func'

vartest()
print(a)