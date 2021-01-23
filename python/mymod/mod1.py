#mod1.py
# 모듈 테스트
def add(a, b):
    return a+b
def sub(a, b):
    return a-b

if __name__ == "__main__": #mod1.py를 직접 실행한 경우
    print(add(1, 4))
    print(sub(4, 2))