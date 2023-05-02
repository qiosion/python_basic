# overloading 오버로딩을 사용하기 위해서는
# @dispatch 라는 어노테이션을 해줘야함

from multipledispatch import dispatch

class Student:
    # 클래스 바로 아래에 변수를 지정 : 클래스 변수
    # 파이썬 생성자 : __init__

    @dispatch()
    def __init__(self):
        # 파이썬에서의 객체 변수는 생성자 아래에 작성
        # 자바는 초기값을 주지 않아도 타입이 정해져있어서 알아서 0 또는 null로 들어가지만
        # 파이썬에서는 초기값을 지정해줘야 함
        self.id = 0
        self.name = ""
        self.grade = 0
    @dispatch(int, str)
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grade = 0

    @dispatch(int, str, int)
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade

    def printInfo(self):
        print(f'student Id is {self.id}, name is {self.name} and '
              f'grade = {self.grade}')

std1 = Student()
std2 = Student(1100, "강은선")
std3 = Student(1200, "구보람", 1)

std1.printInfo() # student Id is 0, name is  and grade = 0
std2.printInfo() # student Id is 1100, name is 강은선 and grade = 0
std3.printInfo() # student Id is 1200, name is 구보람 and grade = 1

std1.id = 1300
std1.name = "김권아"
std1.grade = 2
std2.grade = 3

std1.printInfo() # student Id is 1300, name is 김권아 and grade = 2
std2.printInfo() # student Id is 1100, name is 강은선 and grade = 3


class SampleCalc:
    @dispatch(int, int)
    def add(self, a, b):
        return a + b

    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c

sampleCalc = SampleCalc()
print(sampleCalc.add(3, 4))
print(sampleCalc.add(3, 4, 5))