def problemDescription():
    print('* Number of divisors *')
def getNumOfDivisors(number):
    numOfDivisors = 0
    for i in range(1,number+1):
        if number%i == 0:
            numOfDivisors = numOfDivisors + 1
    return numOfDivisors

problemDescription()
print('Type the first number:')
first = int(input())
print('Type the second number:')
second = int(input())
print('Number of divisors of the first number is '+str(getNumOfDivisors(first)))
print('Number of divisors of the second number is '+str(getNumOfDivisors(second)))
            
    
