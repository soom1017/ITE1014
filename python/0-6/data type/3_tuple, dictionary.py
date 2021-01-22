#튜플 관련 함수
#튜플은 immutable type
t1 = (1, 2, 'a', 'b')
t2 = ('i', 'like', 'python')
print(t1[1:] + t2)

print(len(t1 * 3))

#딕셔너리 관련 함수
#파이썬의 딕셔너리: 일반적으로 '해시', '연관배열'이라 부름
#non_sequential

#딕셔너리 주의사항: key에는 immutable type만 쓸 수 있음
# 리스트X, 튜플0

dic1 = {'name': 'pey', 'phone':'0119993323', 'birth':'1118'}
dic2 = {'a': [1, 2, 3], 'b': [4, 5, 6]}
dic2['c'] = 'hi'
print(dic2)

print(dic1.get('name')) #dic1['not_in_the_keys']은 오류 발생, dic.get['not_in_the_keys']는 None을 반환
is_in_dic1 = dic1.get('not_in_the_keys', 'instead_return_this')
print(is_in_dic1)

is_in_dic2 = 'a' in dic2
print(is_in_dic2)

del dic1['name']
print(dic1)

#딕셔너리 관련 리스트 반환 함수
print(dic2.keys())
print(dic2.values())

#딕셔너리 관련 튜플 반환 함수
t = dic2.items()
print(t)

dic1.clear()
print(dic1)