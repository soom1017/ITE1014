#while문 활용
prompt = '''
    1. Add
    2. Del
    3. List
    4. Quit '''
number = 0
while number != 4:
    print(prompt)
    number = int(input('Enter number: '))

#coffee.py
coffee = 10
while True:
    money = int(input('돈을 넣어 주세요: '))
    if money == 300:
        print('커피를 줍니다')
        coffee = coffee - 1
    elif money > 300:
        print('거스름돈 %d를 주고 커피를 줍니다' %(money - 300))
        coffee = coffee - 1
    else:
        print('돈을 다시 돌려주고 커피를 주지 않습니다')
    if coffee == 0:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다')
        break

a = 0
while a < 10:
    a = a + 1
    if a%2 == 0: continue
    print(a)

#무한 루프는 ctrl + c로 빠져나올 수 있다.