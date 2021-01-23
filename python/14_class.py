#python의 class
# class의 함수: 'method', class의 객체: '인스턴스'
# -> a = Fourcal()에서 객체 a: Fourcal의 인스턴스

class FourCal:
    def __init__(self, first, second): # constructor
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)
print(a.first); print(a.second)
print(a.add() + a.mul() + a.sub() + a.div())

#클래스 상속(inheritance)
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

b = MoreFourCal(4, 2)
print(b.pow())

#메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

c = SafeFourCal(4, 0)
print(c.div())

#클래스 변수
# 클래스 변수는 클래스의 모든 인스턴스에 공유됨
class Family:
    lastname = '이'

fam1 = Family(); fam2 = Family()

Family.lastname = '박'
print(fam1.lastname)
print(fam2.lastname)
print(fam1.lastname is fam2.lastname)