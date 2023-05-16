def add(a, b):
    return a + b

def mul(a, b):
    return a * b

class Calc:
    def __init__(self):
        self.a = 1
        self.b = 2


"""
module_ex에서만 테스트 하고싶다면 if __name__ == "__main__" 를 붙여줘야한다
아니면 다른 파일에서 import 했을 때, 여기서 테스트한 실행결과가 같이 뜬다
if __name__ == "__main__":
    calc = Calc()

    print(add(2, 3))
    print(mul(3, 4))

    print(f'result of the class: {calc.a + calc.b}')
"""
