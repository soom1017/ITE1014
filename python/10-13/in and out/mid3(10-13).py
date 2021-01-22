#2번
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1, 2))
print(avg_numbers(1, 2, 3, 4, 5))

#3번
input1 = int(input('first number: '))
input2 = int(input('second number: '))

total = input1 + input2
print('sum of numbers is %s' % total)

#6번
user_input = input('저장할 내용을 입력하세요: ')
f = open('test.txt', 'a')
f.write(user_input)
f.write('\n')
f.close()

#7번
f = open('test.txt', 'r')
body = f.readlines()
f.close()

body = body[0] + body[1].replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()
