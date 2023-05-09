"""
상속, 오버라이딩, 다형성 => 세트로 자주 다니니까 잘 알기
오버라이딩 : 같은 코드에서 여러 다른 실행 결과가 나올 수 있음
다형성 -> 유연하고 확장성 있게 코드 작성 가능

# 똑같은 함수로 다른 결과를 낸다
def price(customerGrade):
    if customerGrade == "silver":
        discont = 0
        bonusRatio = 0.05
    elif customerGrade == "VIP":


"""

class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.bonusPoint = 0
        self.grade = "SILVER"
        self.bonusRatio = 0.05 # 보너스 적립해주는 비율
        # silver 등급일 때
        # discont = 0
        # bonusRatio = 0.05

    def calcPrice(self, price):
        self.bonusPoint += (price * self.bonusRatio)
        return price

    def printCustomerInfo(self):
        print(f'{self.name}님의 등급은 {self.grade}이며, 현재 보너스 포인트는 '
              f'{self.bonusPoint} 입니다')

# vip 등급일 때
# discont = 0.1
# bonusRatio = 0.3
class VIPCustomer(Customer):
    def __init__(self, id, name, agentID):
        super().__init__(id, name)
        self.agentID = agentID
        self.grade = "VIP"
        self.bonusRatio = 0.3
        self.discountRatio = 0.1
        self.bonusPoint = 5000

    def calcPrice(self, price):
        self.bonusPoint += (price * self.bonusRatio)
        price = price - int((price * self.discountRatio))
        return price

    def printCustomerInfo(self):
        print(f'{self.name}님의 등급은 {self.grade}이며, 현재 보너스 포인트는 '
              f'{self.bonusPoint} 입니다. 담당자 : {self.agentID}')

class GoldCustomer(Customer):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.grade = "GOLD"
        self.bonusRatio = 0.1
        self.discountRatio = 0.05
        self.bonusPoint = 1000

    def calcPrice(self, price):
        self.bonusPoint += (price * self.bonusRatio)
        price = price - int((price * self.discountRatio))
        return price

    def printCustomerInfo(self):
        print(f'{self.name}님의 등급은 {self.grade}이며, 현재 보너스 포인트는 '
              f'{self.bonusPoint} 입니다')

customer_list = []
customer_silver = Customer(100, "강은선")
customer_gold = GoldCustomer(200, "구보람")
customer_vip = VIPCustomer(300, "김권아", "ABC-1001")

customer_list.append(customer_silver)
customer_list.append(customer_gold)
customer_list.append(customer_vip)

print("==================== customer Information ====================")
for value in customer_list:
    value.printCustomerInfo()

print("==================== Calculate price each customer ====================")
price = 10000
for value in customer_list:
    cost = value.calcPrice(price)
    print(f'{value.name}님은 {cost}를 지불하였습니다.')
    print(f'{value.name}님의 현재 포인트는 {value.bonusPoint} 입니다.')


# 상속하는 방법
# 자바 : Class 자손클래스 extends 조상클래스
# 파이썬 : class 자손클래스 (조상클래스)
class Rect: # 사각형
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self): # 둘레
        return 2 * self.w + 2 * self.h

    def calc_area(self):
        print("==")
        return self.w * self.h

class Square: # 정사각형
    def __init__(self, w):
        self.w = w

    def area(self):
        return self.w ** 2

    def perimeter(self):
        return self.w * 4

class SquareInh(Rect): # 사각형을 상속받아 만든 정사각형
    def __init__(self, w):
        super().__init__(w, w)

    def calc_area(self):
        print("==parent==")
        return self.w * self.w

class Cube(SquareInh): # 정육면체
    def volume(self): # 한 면의 넓이
        vol = super().calc_area() # 상위클래스의 calc_area 메서드
        return vol * self.w

    def surface(self):
        sur_area = super(SquareInh, self).calc_area() # 상위 -> 상위 클래스의 calc_area
        # 정육면체의 넓이 : w * w * 6
        return sur_area * 6

print('>>> 사각형')
rect = Rect(2, 6)
print(rect.area()) # 12
print(rect.perimeter()) # 16

print('>>> 정사각형')
square = Square(4)
print(square.area()) # 16
print(square.perimeter()) # 16

print('>>> 사각형을 상속받아 만든 정사각형')
square_inh = SquareInh(4)
print(square_inh.area()) # 16
print(square_inh.perimeter()) # 16

print('>>> 정육면체')
cube = Cube(3)
print(cube.volume()) # ==parent==      27
print(cube.surface()) # ==      54