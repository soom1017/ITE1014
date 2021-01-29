# hangman 단어를 인터넷에서 긁어왔더니 200개 넘는 단어들이 \n로 구분되어 있어,
# \n -> ' '
# 전환해주는 py 파일 만듦.
#한 줄에 단어 10개씩 끊어서 보여줌.
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
enter_content = f.read()
f.close()

space_content = enter_content

count = enter_content.count('\n') 
forPass = 0
while count > 0:
    num = space_content.find('\n', forPass)  
    if(count % 10 == 0):
        forPass = num + 2
    else:
        space_content = space_content[:num] + space_content[num:].replace('\n', ' ', 1)
    count -= 1

f = open(dst, 'w')
f.write(space_content)
f.close()