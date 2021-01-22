#if문 활용
money = 2000
card = True
if money >= 3000 or card:
    print('택시를 타고 가라')
else:
    print('걸어가라')

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: # in, not in
    pass
elif card: # elif ~ == else: if ~
    print('카드를 꺼내라')
else:
    print('걸어가라')

score = 89
if score >= 60: message = 'success'
else: message = 'failure'
print(message)

#조건부 표현식
message = 'success' if score >= 60 else 'failure'
print(message)