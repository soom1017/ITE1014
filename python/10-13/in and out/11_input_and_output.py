#사용자 입력과 출력
# 프롬프트: 컴퓨터가 입력을 기다리고 있음을 가리키기 위해 화면에 나타나는 표시
prompt = '숫자를 입력하세요'
number = input(f'{prompt}: ')
print(number)

print('life' 'is' 'too' 'short') # == print('life'+'is'+'too'+'short')
print('life', 'is', 'too', 'short')

for i in range(10):
    print(i, end=' ')
