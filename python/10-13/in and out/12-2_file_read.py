#파일 읽고 쓰기
# 파일 객체 = open(파일 이름, 파일 열기 모드)

#read_all1.py
f = open('C:/Users/min00/newFile.txt', 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

#read_all2.py
f = open('C:/Users/min00/newFile.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

#read_all3.py
f = open('C:/Users/min00/newFile.txt', 'r')
data = f.read()
print(data)
f.close()
