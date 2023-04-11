# 함수는 4종류
# 입 ㅇ 출 ㅇ
def add1(a, b):
    return a + b
print("입 ㅇ 출 ㅇ : ", add1(3, 4)) # 입 ㅇ 출 ㅇ :  7

# 입 x 출 o
def add2():
    return 5 + 5
print("입 x 출 o : ", add2()) # 입 x 출 o :  10

# 입 ㅇ 출 x
def mul(a, b):
    print("입 ㅇ 출 x : ", a * b) # 입 ㅇ 출 x :  12
rtn_val = mul(3, 4)
print("rtn_val : ", rtn_val) # None

mul(3, 4) # 입 ㅇ 출 x :  12
# not equal print(mul(3, 4)). 이건 print(rtn_val)과 마찬기지로 None

# 입 x 출 x
import math
def print_PI():
    print("입 x 출 x : ", math.pi)
print_PI() # 입 x 출 x :  3.141592653589793

# 함수의 파라미터 지정
mul(a = 3, b = 8)
mul(b = 3, a = 8)

# 파라미터 초기값 지정
def mul_test(input, a = 3, b = 4):
    return input * a * b
# 호출
print(mul_test(3)) # 3 * 3 * 4 = 36

# 함수 호출 파라미터의 갯수가 정해져있지 않을 때 (입력갯수가 정해져있지 않을 때)
# 입력 인자를 모두 더하는(누적합 반환) 함수를 만들어보자
def add_many(*args):
    result = 0
    for data in args:
        result += data
    return result
rtn_val = add_many(1, 2, 3, 4)
print(rtn_val) # 결과 : 10
tmp = [1, 2, 3, 4, 5]
print(add_many(*tmp)) # 결과 : 15

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result
print('add : ', add_mul('add', 1, 2, 3, 4, 5))
print('mul : ', add_mul('mul', 1, 2, 3, 4, 5))


# 키워드 파라미터
def myfunc(**kwargs):
    for item in kwargs.items():
        print(item)
myfunc(x = 100, y = 200, z = 'abc')
# 결과 :
# ('x', 100)
# ('y', 200)
# ('z', 'abc')

# 매개변수 초기값(디폴트값) 지정
def say_myself (name, age, dept="AI_Engineering"):
    print(f'name is {name}')
    print(f'age is {age}')
    print(f'dept is {dept}')
say_myself('학생1', 25) # 3개를 모두 정상 출력
say_myself('학생2', 28, dept='Electronic')
# say_myself('학생3', dept='Test') # 디폴트값 지정되지 않은 매개변수의 경우 값을 주지 않으면 에러 발생
# TypeError: say_myself() missing 1 required positional argument: 'age'

# 함수의 범위
a = 1
def vartest(a):
    a = a + 1
    print(f'지역변수 a = {a}')
vartest(a)
print(f'전역변수 a = {a}')

# global 변수 (전역변수)
a = 1
def globalTest(arg):
    global a
    a = arg + 1
print(f'before call function: value a = {a}') # a = 1
globalTest(3)
print(f'after call function: value a = {a}') # a = 4

# 람다 lambda : 함수를 한줄로 간단히 표현
# C : 매크로 함수
# C언어로 표현하면 #define MUL(a, b) (a) * (b)
mul = lambda a, b: a * b
result = mul(3, 4)
print(result)