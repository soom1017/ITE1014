#모듈: 'import 모듈' 또는 'from 모듈 import 함수'로 가져오기
# 모듈 파일과 동일한 디렉터리에 있어야만 가능.
from mod1 import *
print(add(3,4))

import mod2
print(mod2.PI)

a = mod2.Math()
print(a.solv(2))

print(mod2.add(mod2.PI, 4.4))

# 모듈 파일을 어느 디렉터리에서든 쓸 수 있게 하는 방법
# 1. sys.path.append('C:/min00/python/mymod')
#       ㄴsys.path: 파이썬 라이브러리 저장소
# 2. set PYTHONPATH=C:/min00/python/mymod
#        ㄴ환경변수 이용