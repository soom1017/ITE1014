#python 외장 함수들
# 파이썬 라이브러리 중 자주 사용되는 것들

#sys_ex.py
# 1. 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어하는 모듈
# import sys

# print(sys.argv)
# sys.path.append("{module's path}")

#pickle_ex.py
# 2. 객체의 형태를 그대로 유지하면서 파일에 저장, 불러올 수 있는 모듈
import pickle

f = open('data.txt', 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f) # dump: 객체를 그대로 file에 저장

f = open('data.txt', 'rb')
data = pickle.load(f) # load: 객체를 그대로 불러옴 
print(data)

#os_ex.py
# 3. os 자원을 제어하는 모듈
import os

print(os.environ) # environ: 환경변수
# os.chdir('C:/Users')
print(os.getcwd())

os.system('dir') # 시스템 명령어 실행

f = os.popen('dir') # 시스템 명령어 실행한 결과를 읽기모드 형태의 파일 객체로 돌려줌.
print(f.read())

#shutil_ex.py
# 4. 파일을 복사하는 모듈
import shutil
shutil.copy('src.txt', 'dst.txt') # src 파일을 dst로 복사

#glob_ex.py
# 5. 특정 디렉터리에 있는 파일 이름을 알 수 있는 모듈
import glob
li = glob.glob('C:/Users/python/*')

#tempfile_ex.py
# 6. 파일을 임시로 만들어 사용할 때 쓰는 모듈
import tempfile
filename = tempfile.mktemp()
print(filename)

f = tempfile.TemporaryFile() # 임시 저장 공간으로 사용할 파일 객체를 돌려줌.
f.close()

#time_ex.py
# 7. 시간 관련 모듈
import time
now = time.ctime() # time.ctime() == time.asctime(time.localtime(time.time()))
print(now)

for i in range(10):
    print(i)
    time.sleep(1)

#calendar_ex.py
# 8. 달력 관련 모듈
import calendar
print(calendar.prmonth(2021, 1))

day_of_today = calendar.weekday(2021, 1, 25)
print(day_of_today)

#random_ex.py
# 9. 난수를 발생시키는 모듈
import random
num = random.randint(1, 10) # 1~10 사이 난수 발생
print(num)

nums = [1, 2, 3, 4, 5]
def random_pop(data):
    number = random.choice(data) # 리스트에서 하나 골라줌.
    data.remove(number)
    return number

random_number = random_pop(nums)
print(random_number)

random.shuffle(nums) # 리스트의 항목을 무작위로 섞어 줌.
print(nums)

#webbrowser_ex.py
# 10. 기본 웹브라우저를 자동으로 실행
import webbrowser
webbrowser.open('http://google.com')