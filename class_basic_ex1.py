"""
학생 -> 버스 또는 지하철을 타고 학교로 가는 것
# 절차지향
getup() ==> eat() ==> take bus() ==> ...

# 객체지향
1. 학생클래스, 버스/지하철 클래스, 학교클래스 등등
2. 각 클래스마다 객체가 하는 기능을 정의하고 구현(메서드)
   버스를 탄다, 밥을 먹는다, .. 등등
3. 각 객체들이 제공하는 기능들을 이용하여, 객체간의 협력을 구현함
"""

"""
자바 >>>
public class Student {
    int studentId;
    String studentName;
    int grade;

    // 자바의 생성자
    public Student() {} // 자바에서는 자동으로 기본생성자를 만들어 줌

    public Student(int studentId, String studentName, int grade) {
        this.studentId = studentId;
        this.studentName = studentName;
        this.grade = grade;
    }

    // 메서드
    public String showStudentInfo() {
        return studentName + "의 학번은 " + studentId;
    }
}
1. 객체를 정의하고
2. 각 객체를 표현할 수 있는 속성을 멤버변수로 정의
3. 역할을 메서드로 구현 후,
4. 각 객체간의 협력을 구현
"""

# 파이썬으로 Student, Bus, Subway 클래스 만들고
# 각각의 인스턴스변수, 메서드 만들고 어떻게 동작하는지 알아보자
# 학생은 버스나 지하철을 타고, 돈을 지불함
# 버스, 지하철은 승객 수와 금액이 늘어남

"""
학생 클래스
- 인스턴스 변수(=멤버변수) : 학생 이름, 학년
- 메서드 : 버스, 지하철을 탄다. 버스클래스의 메서드 중 take 호출. 금액 minus
- 디버깅 용도로 printInfo를 하자

버스/지하철 클래스
- 인스턴스 변수 : 버스/라인 번호, 승객 수, 금액
- 메서드 : 버스/지하철에 승객을 태우다. 금액 plus, 승객 plus
- 디버깅 용도로 printInfo를 하자

학생 클래스를 이용하여 학생 객체를 2~3명 생성
버스/지하철 객체도 생성
학생들이 버스/지하철을 탔을 때 각각의 객체들의 상황을 print
"""

# 강의자료 : 클래스변수 vs 인스턴스 변수
# 자바 : 클래스변수 static, 멤버변수
# 클래스변수 == 클래스변수 , 멤버변수 == 인스턴스 변수
class Student:
    # 생성자 -> 초기값 지정
    def __init__(self, name, money):
        self.name = name
        self.grade = 1 # 굳이 모든 것을 인자로 받지 않아도 생성자에서 초기화 가능
        self.money = money

    # 메서드 : 버스/지하철 탄다
    def takeBus(self, bus):
        bus.take(1000)
        self.money = self.money - 1000
    def takeSubway(self, subway):
        subway.take(1200)
        self.money -= 1200

    def takeTaxi(self, taxi, min):
        taxi.take(1100, min)
        self.money -= 3800 + (1100 * min)

    # 학생 정보
    def printInfo(self):
        print(f'{self.name} 학생이 가진 돈은 {self.money}원 입니다.')

class Bus:
    def __init__(self, busNum):
        self.busNum = busNum
        self.cntPassenger = 0 # 처음엔 승객수 0명이니까
        self.money = 0
    def take(self, money): # bus.take 로 호출할 때 money 인자를 1000원으로 넣었음
        self.cntPassenger += 1
        self.money += money

    def printInfo(self):
        print(f'{self.busNum}번 버스의 승객 수는 {self.cntPassenger}명이며 '
              f'현재 수입은 {self.money}원입니다.')

class Taxi:
    def __init__(self, taxiNum):
        self.taxiNum = taxiNum
        self.money = 0

    def take(self, money, min): # 몇분 타냐에 따라서 가격이 달라짐
        self.money += 3800 + (money * min)

    def printInfo(self):
        print(f'택시{self.taxiNum}의 현재 수입은 {self.money}원입니다.')

class Subway:
    def __init__(self, lineNum):
        self.lineNum = lineNum
        self.cntPassenger = 0  # 처음엔 승객수 0명이니까
        self.money = 0

    def take(self, money):  # subway.take 로 호출할 때 money 인자를 1200원으로 넣었음
        self.cntPassenger += 1
        self.money += money

    def printInfo(self):
        print(f'지하철 {self.lineNum}라인의 승객 수는 {self.cntPassenger}명이며 '
              f'현재 수입은 {self.money}원입니다.')

# 학생 인스턴스 3명 생성
std1 = Student("강은선", 10000)
std2 = Student("구보람", 20000)
std3 = Student("김권아", 30000)

# 버스/지하철 인스턴스 생성
bus_100 = Bus(100) # 버스번호
sub_1 = Subway(1) # 지하철 호선
taxi_1111 = Taxi(1111)

# 학생 1번 객체는 takeSubway 메서드를 사용하는데, 이때 sub_1 객체를 이용한다
std1.takeSubway(sub_1)
std2.takeBus(bus_100)
std3.takeTaxi(taxi_1111, 10) # 택시 몇분 타는지 필요함

# 각 정보를 출력해보자
std1.printInfo()
std2.printInfo()
std3.printInfo()
bus_100.printInfo()
sub_1.printInfo()
taxi_1111.printInfo()

