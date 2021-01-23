#예외 처리
# 오류는 아주 다양
# FileNotFoundError, ZeroDivisionError, IndexError, ...

# try - except 구문
try:
    4/0
    a = [1, 2]
    print(a[3])
except ZeroDivisionError as e1: # ZeroDivisionError 먼저 발생. 따라서 IndexError는 발생하지 X
    print(e1)
except IndexError as e2:        # 두 개 이상의 오류 처리할 때는 튜플 사용
    print(e2)                   # -> except (ZeroDivisionError, IndexError) as e: ...

# try - finally
# finally는 오류 발생과 상관없이 실행
f = open('foo.txt', 'w')
try:
    ...
finally:
    f.close()

# 오류 그냥 통과시키기
try:
    f = open('non_exist_file', 'r')
except FileNotFoundError:
    pass

# 오류 일부러 발생시키기
# Bird 클래스를 상속받는 자식 클래스가 반드시 fly 함수를 구현하도록 만듦.
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

eagle1 = Eagle()
eagle1.fly()

# 예외 만들기
class MyError(Exception):
    def __str__(self):
        return '허용되지 않은 별명임.'

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)