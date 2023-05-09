# 템플릿 패턴 : 객체지향 디자인 패턴 중 하나
# 추상화를 설명하기에 적합하고 실제로 사용하고 있음

"""
추상클래스 : 전체적인 흐름(공통부분)을 정의. 하위클래스에서 다르게 동작하는 부분에 관해서는 추상화 메서드로 정의
하위클래스(추상클래스를 상속받은 클래스) : 추상화 메서드를 구현

예) 자동차 운전
전체적인 흐름 : 시동 키고, 운전, 주차, 시동 끈다
    def run () {
        turnOn ();
        driving ();
        parking ();
        turnOff ();
    }
- 자율운행 자동차 vs 일반 자동차 비교
    - 시동을 키고 끄는 부분은 일반적인 메서드로 정의할 수 있음
    - 운전, 주차하는 기능은 자율운행 자동차와 일반 자동차가 다르기 때문에 추상화 메서드로 정의
- 루틴 자체를 final로 정의해서 다른 클래스에서 오버라이딩 못하게 막음
    ==> 파이썬에서는 final이 없음
"""

from abc import *
class Car(metaclass=ABCMeta):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def parking(self):
        pass

    def turnOn(self):
        print('시동')

    def turnOff(self):
        print('종료')

    # 파이썬에서는 오버라이딩을 하지 못하게 하기 위해
    # 관행적으로 메서드명 앞에 _를 붙여줌
    def _run(self): # 주행 순서를 지켜줘야함
        self.turnOn()
        self.drive()
        self.parking()
        self.turnOff()