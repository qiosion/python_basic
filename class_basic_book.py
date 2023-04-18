# 함수: def
# 클래스: class
# 자바에서 패키지 Package는 소문자로 시작
# 클래스는 일반적으로 대문자로 시작

# 사칙연산 계산기 클래스
class FourCal:
    # 클래스 내에서 def로 시작되는 것 = 메서드 Method
    # 메서드는 일반적으로 클래스의 멤버변수, 인스턴스 변수를 활용하여 무언가를 하는 것이다
    # 클래스 안의 함수(메서드)이므로 괄호를 치면 자동으로 self가 붙어옴

    # 객체 생성 시 독립적인 공간이 만들어짐

    # 생성자 def __init__(self) : 객체가 만들어 질 때, 초기값을 할당해서 만들 수 있음
    # 파이썬에서는 오버로딩을 하려하면 다른방법을 써야함
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def set_data(self, first, second):
        self.first = first # 파이썬의 self = 자바의 this. 과 같다
        self.second = second
    def add(self):
        return self.first + self.second
    def mul(self):
        return self.first * self.second
    def sub(self):
        return self.first - self.second
    def div(self):
        return self.first / self.second

# 객체, 인스턴스 생성
# 자바의 경우 : 자료형 객체명 = new 자료형()
# FourCal cal_0 = new FourCal()
# 자바 jdk 12 이상 부터 지역변수 타입 지정하지 않고 파이썬과 같이 사용 가능
# var num1 = 10
# var num2 = 10.3f
# 이런식으로 변수임을 var (variable)로 지정

# 파이썬의 경우 : 객체명 = 자료형()
# cal_0 = FourCal() # 생성자 파라미터와 수가 맞지않아 에러
#
# cal_0.set_data(4, 2)
# print(cal_0.add(), cal_0.sub())
#
# # 생성자 연습
# # def __init__(self, a, b):
# cal_1 = FourCal() # 생성자 파라미터와 수가 맞지않아 에러
# cal_1.second(1, 2) # 매번 이런식으로 하기 귀찮으니까 생성자를 만든다

# 생성자
cal_2 = FourCal(5, 3)
print(cal_2.add())