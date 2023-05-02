"""
java 에서 클래스 변수 = static 변수
- 여러 객체(인스턴스)가 공유하는 기준 값이 필요한 경우 사용
    - 학생마다 새로운 학번을 부여
    - 은행계좌, 카드번호 부여
    - 사번증 발급시 사용되는 사번 등
"""

class Bank:
    # 아래는 클래스 변수로서 여러 인스턴스가 공유됨
    countAccount = 0 # 만들어진 계좌의 총 갯수
    numUniqAccount = 1000 # 계좌번호
    total = 0 # 은행의 잔고

    # 새로운 고객이 생김
    def __init__(self, name, alias, password):
        Bank.countAccount += 1 # 전체 계좌개수 +1됨
        Bank.numUniqAccount += 1 # 계좌번호는 1001부터 시작
        self.name = name
        self. alias = alias
        self.password = password
        self.numUniqAccount = Bank.numUniqAccount
        self.total = 0 # 고객의 잔고. 0부터 시작

    def income(self, money): # 고객이 돈을 넣으면,
        Bank.total += money # 은행의 총 잔고가 늘어나고
        self.total += money # 고객 개인의 통장 잔고도 늘어난다

user1 = Bank("강은선", "용돈", "1234")
user2 = Bank("구보람", "월급", "0000")

user1.income(100000)
user2.income(5000000)

print(f"만들어진 계좌의 총 갯수 : {Bank.countAccount}") # 2
print(f"user1의 계좌번호 : {user1.numUniqAccount}") # 1001
print(f"user2의 계좌번호 : {user2.numUniqAccount}") # 1002
print(f"은행 수입 총액 : {Bank.total}") # 5100000
print(f"user1의 수입 총액 : {user1.total}") # 100000
print(f"user2의 수입 총액 : {user2.total}") # 5000000