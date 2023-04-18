# class namespace

"""
객체를 생성하고
인스턴스명.멤버변수, 인스턴스 변수
형태로 사용가능

인스턴스명. 점찍고 찾아가는 순서가 있음
인스턴스 내에 존재하는지를 체크하고, 없으면 class 변수에서 찾는다
"""

"""
class Student:
    name = "" # 클래스 변수
    age = 0 # 클래스 변수
    def __init__(self, deptCode, deptName):
        self.deptCode = deptCode # 인스턴스 변수
        self.deptName = deptName # 인스턴스 변수

std1 = Student()
std1.name = "홍길동"
std1.deptName = "활빈당"
"""

# 게임 캐릭터를 만들어보자
class GameChar:
    strength = 10
    energy = 100

    def __init__(self, id, alias): # 아이디, 닉
        self.id = id
        self.alias = alias

    def training(self):
        self.strength += 2

user1 = GameChar("ai-engr.#1", "공부하기 싫어")
user2 = GameChar("ai-engr.#2", "나도 싫어")

print("print Class NameSpace")
print(dir()) # 사용할 수 있는 클래스, 객체 등을 출력해줌
# 출력되는 것은 프롬프트(에디터)에서 입력해도 에러는 발생하지 않음

# user1, 2의 인스턴스를 출력해보자
# 현재, user1, 2는 생성자에 의해 id와 alias는 존재함
print(user1.__dict__) # {'id': 'ai-engr.#1', 'alias': '공부하기 싫어'}
print(user2.__dict__) # {'id': 'ai-engr.#2', 'alias': '나도 싫어'}

user1.training()
# 트레이닝 결과로 user1에게만 +2된 strength가 보이게 됨
# 인스턴스 내에서 사용가능한 strength
print(user1.__dict__) # {'id': 'ai-engr.#1', 'alias': '공부하기 싫어', 'strength': 12}
print(user2.__dict__) # {'id': 'ai-engr.#2', 'alias': '나도 싫어'}

print(user1.strength, user2.strength) # 12 10
# 출력해보면 user2에게도 strength 10이라고 뜨지만, user2 인스턴스 내에는 없음
# 즉, user2는 GameChar 라는 클래스 내에 있는 변수 strength를 가져오는 것

user2.training()
print(user1.__dict__) # {'id': 'ai-engr.#1', 'alias': '공부하기 싫어', 'strength': 12}
print(user2.__dict__) # {'id': 'ai-engr.#2', 'alias': '나도 싫어', 'strength': 12}

user2.training()
print(user1.strength, user2.strength) # 12 14

print(GameChar.strength, user1.strength, user2.strength)
# GameChar. : 클래스로 접근. 공통적으로 사용할수 있는 변수이므로 10에서 고정
# user1., user2. : 인스턴스로 접근.
