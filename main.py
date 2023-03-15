# import pandas as pd
#
# data = {
#     "name": ["A", "B", "C"],
#     "StudentNum": ["2003-01", "2003-02", "2003-03"]
# }
#
# df = pd.DataFrame(data)
#
# print(data)
# print(df)
#
#
# x = 5
# print(x)
#
# x,y,z = 1, 2, 3
# print(x,y,z)

""" """

# 모든 자료형 == 객체로 취급
# 5라는 숫자형 객체가 특정 메모리에 할당되고, 해당 객체 5 를 x라는 변수에 바인딩
# 주의:
# == 기호가 프로그램에서는 등호로 사용된다
# = 기호는 할당 assign

# x = 11
# print('test', x)
# x, y, z = 1, 2, 3
# print('test', x, y, z)

""" """

a, b, c = 3, 7, 2
d = a+b
print(d, a-b, a/b, a*b)
print(b%a, b//a) # % : 나머지 연산자, // : 몫 연산자
# 파이썬에선 별도의 자료형을 지정해주지 않기에, 몫 연산자가 필요하다

# [] <-- list 자료형 : 배열 array
answer = [a+b, a-b, a/b, a*b]
print(answer)
print("answer[0] = ", answer[0])
print("answer[1] = ", answer[1])