"""
추상화 클래스 : 구현 코드 없이 메서드 선언만 있는 추상 메서드(abstract keyword)를 포함한 클래스
- 메서드 선언 declaration : 반환타입, 메서드이름, 매개변수
- 메서드 정의 definition : 메서드 구현 implementation

int add(int x, int y); // 메서드 선언 declaration (아직 구현은 안한것) -> 추상화 메서드
int add(int x, int y) {} // 메서드 정의 definition : 구현부가 존재 함 -> 추상 메서드 X

추상 클래스는 new를 통해서 객체를 생성할 수 없음
상속받아서 추상화 메서드를 구현해야 함

public abstract Class Computer {
    abstract void cpu_calc(); // 추상메서드
    abstract void display();

    public void turnOn() { System.out.println("실행") }
    public void turnOff() { System.out.println("종료") }
}

Computer c = new Computer(); // 에러 발생 ! (파이썬도 마찬가지. 추상클래스이므로)

// 추상클래스를 구현하기 위해서는 상속받아야 한다
public Class Laptop extends Computer {
    void cpu_calc() { }
    void display() { }

    @override
    void turnOn() { System.out.println("오버라이딩") }
}
"""

# ABC (ABstract Class)를 import
from abc import *
class Computer(metaclass=ABCMeta): # public abstract class Computer
    # abstract method 사용
    @abstractmethod
    def cpu_calc(self):
        pass

    @abstractmethod
    def display(self):
        pass

    def turnOn(self):
        print(f'Turn On a Computer')

    def turnOff(self):
        print(f'Turn Off a Computer')

# myComputer = Computer() => 에러. 추상클래스는 상속받아 구현해야함

class Laptop (Computer):
    def cpu_calc(self):
        print('Laptop cpu Spec.')

    def display(self):
        print('Laptop display')


class Desktop(Computer):
    def cpu_calc(self):
        print('Desktop cpu Spec.')

    def display(self):
        print('Desktop display')

    def turnOn(self):
        print(f'Turn On a Desktop')

    def turnOff(self):
        print(f'Turn Off a Desktop')

desktop = Desktop()
laptop = Laptop()

desktop.display()
desktop.turnOff()
laptop.cpu_calc()