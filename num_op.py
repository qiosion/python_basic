# 숫자 객체 (정수형, 실수형) [8진수, 16진수]

# 정수
a = 432
b = -123
c = 0

print('정수: ', a, b, c)

# 실수
a = 12.34
b = -3.141592
exp_a = 4.23e3 # 4.23 * 10^3
exp_b = 4.23e-3 # 4.23 * (1/10)^3
print('실수: ', a, b, exp_a, exp_b)

# 8진수 (0~7), 16진수(0~15: 10:a, 11:b, .., 0~F)
# 8진수 : 0o : 표기시 0o37 와 같이 앞에 0o 붙여줌
# 16진수 : 0x : hexadecimal
# 포맷팅 f'{}'
# 콜론(:) 뒤에 원하는 타입을 적어줌
# d : decimal 10진수
# f : float 실수
a = 0x10
print('포맷팅 이용 예시: ', f'{a:d}, {a:f}, {a:0x}')

# range : 범위. range(이상,미만)
# for : 반복문
# for x in range(1, 10):
#     print(x)
num = 0.0
for i in range(0,100): # 0~99 : 100회
    num = num + 0.1
print('for문 예시: ', num)
print('포맷팅: ', f'{num:.17f}') # 17f는 소수점 17자리까지 표기하라 명시한것

num = 0.1 + 100
print('근사치 예시: ', num)
print('근사치 포맷팅: ', f'{num:.17f}')

# 연산자: +, -, *, /, **, %, //

# >> 소수 판단 Prime Number 구하기 <<

# 반복과 관련된 statement : for, while
# for : 정해진 갯수만큼 도는 것
# while : 특정 조건을 만족할 때 까지 영원히 도는 것
while(1): # 1==참. 즉, 영원히 while문을 도는 것
    # input : 키보드의 입력을 받는 메서드
    # 즉, 키보드에 입력을 받을때 까지 계속 while문을 돈다는것
    # input의 반환형은 문자열
    testNum = input() # 입력을 받으면 testNum에 바인딩됨
    if(testNum.isdigit()): # 입력된 값이 숫자인지 판단하는 메서드
        break # 숫자면 while문을 나간다

# int : casting 연산자 : 문자열을 숫자형으로 변환하는 연산자
testNum = int(testNum)

# 소수판단
# for i in range(2, testNum): # 2~(testNum-1)
#     if(testNum % i) == 0:
#         print(f'{testNum} is not Prime Number')
#         break
#     print(f'{testNum} is Prime Number')

for i in range(2, testNum): # 2~(testNum-1)
    if(testNum % i) == 0:
        print(f'{testNum} is not Prime Number')
        break
    print(f'{testNum} is Prime Number')

