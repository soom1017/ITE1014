#집합 관련 함수
# set()은 리스트나 문자열을 입력받아 집합을 반환
# unordered, unrepeated
s1 = set([1, 2, 3])
print(s1)

s2 = set('hello')
print(s2)

s3 = s1 & s2 # == s1.interaction(s2)
s4 = s1 | s2 # == s1.union(s2)

s5 = s1 - s2 # == s1.difference(s2)

# 집합을 다시 리스트, 튜플로
print(list(s3))
print(tuple(s4))

s4.add(5)
s4.update([6, 7, 7, 8, 9])
print(s4)

s2.remove('e')
print(s2)

