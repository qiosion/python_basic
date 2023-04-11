# 입력값 X 결과값 O
def say():
	return 'HI'

a = say()
print(a) # 결과 : HI

# 입력값 O 결과값 X
def add(a, b):
    print("%d + %d = %d" % (a, b, a+b))

a = add(3, 4) # 콘솔창에 3 + 4 = 7 라고 뜸
print(a) # 결과 : None

# 입력값 X 결과값 X
def nothing():
    print('Nothing!')
nothing() # 결과 : Nothing!

# 매개변수 지정
def add_para(a, b):
    return a + b
result = add_para(a = 5, b = 3)
print(result)

# 입력값(매개변수)이 몇개일지 모를 때는 가변인자 * 을 씀
def add_many(*args):
    result = 0 # 결과값
    for i in args:
        result += i # 입력값들을 모두 더해라
    return result

rtn_val = []
rtn_val.append(add_many(1,2,3,4,5)) # 1~5까지 더한 값을 rtn_val[0]에 넣음
rtn_val.append(add_many(1,2,3,4))
rtn_val.append(add_many(1,2,3))

print(rtn_val) # 결과 : [15, 10, 6]

# 리스트를 파라미터로 넣을 수도 있다
val = [1, 2, 3, 4, 5]
tmp = add_many(*val)
print(tmp)

# 함수의 결과값은 하나
def add_and_mul(a, b):
    return (a+b), (a*b)
print("result = %d, %d" % add_and_mul(2, 4)) # result = 6, 8
# 함수 add_and_mul에 2와 4를 파라미터로 넣었을 때 나온 결과물
# 튜플이 알아서 둘로 나눠서 나온다

result = add_and_mul(2, 4)
print("result : ", result) # result :  (6, 8)

a, b = add_and_mul(2, 4)
print('a = ', a, ', b = ', b) # a =  6 , b =  8

# 초기값 설정
def say_myself(name, old, female=True):
    print("나의 이름은 %s이고" % name)
    print("나이는 %d살입니다" % old)

    if female:
        print("여자입니다")
    else:
        print("남자입니다")

say_myself("강은선", 30)
say_myself("강은선", 30, True)

# 변수의 범위 scope
a = 1 # 함수 밖의 변수
def vartest(a):
    a = a + 1
    print('함수 안에서의 a : ', a) # 결과 : 2

vartest(a) # 함수 vartest에 a = 1이라는 값을 줌
print('함수 밖에서의 a : ', a) # 결과 : 1

# lambda
add = lambda a, b: a + b
result = add(3, 4)
print(result)


