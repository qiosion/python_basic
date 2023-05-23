# abs : 절대값
print(-3, abs(-3), abs(3), 3) # -3 3 3 3

# all / any
list_a = [1, 2, 3, 0] # list_a 의 원소 0을 false 로 인식한다.
list_b = [1, 2, 3]

# all : 모든게 참이여야 참
print(all(list_a), all(list_b)) # false, true

# any : 하나라도 참이면 참
print(any(list_a), any(list_b)) # true, true

# chr : 아스키 코드 문자 출력
print(f'char 65 = {chr(65)}') # char 65 = A

# dir : 객체, 자료형이 가지고 있는 내장함수의 리스트를 출력하는 용도로 사용
list_var = [1, 2, 3]
str_var = "ABC"
dict_var = {'key': 'value'} # JSON 파일 형태가 딕셔너리로 되어있음

print(dir(list_var))
print(dir(str_var))
print(dir(dict_var))

# div : tuple 형태로 나누기 몫과 나머지 값을 반환
def div_mod(in_a, in_b): # 함수로 구현하면 이렇다
    return ( (in_a // in_b), (in_a % in_b))

print(divmod(7, 3)) # (2, 1)
print(div_mod(7, 3)) # (2, 1)

# enumerate : loop에서 index, val(data) 값을 같이 반환
for idx, data in enumerate(str_var):
    print(idx, data)
"""
for idx in range(len(str_var)):
    print(idx)

for data in str_var:
    print(data)
"""

# eval


# filter(함수이름, 함수에 들어갈 반복 가능한 자료형) : 함수 결과 값이 참인 것만 묶어서 반환
in_data = [1, -1, 2, 0, -2, 3, -3, 4]
# 리스트에서 양수만 리스트로 반환하는 함수를 작성
def rtn_positive(in_data):
    rtn_list = []
    for val in in_data:
        if val > 0:
            rtn_list.append(val)
    return rtn_list
print(rtn_positive(in_data)) # [1, 2, 3, 4]

# 필터를 사용해서 써보자! 파이썬을 파이썬 답게 쓰는 것(내장함수 활용)
def positive(x): # 필터에 사용할 함수
    # x 는 반복가능한 자료에 있는 각 요소 값. 요소 하나하나 씩의 값
    return x > 0

print(list(filter(positive, in_data))) # [1, 2, 3, 4]

# 필터의 람다식
print(list(filter(lambda x: x > 0, in_data))) # [1, 2, 3, 4]
print(list(filter(lambda x: x * 2, in_data))) # [1, -1, 2, -2, 3, -3, 4]
# 필터는 람다의 함수 결과값이 참인 애들만 반환한다 -> 0은 빠짐
# 근데 왜 *2는 안되는거임?? ㅡㅡ;;


# map 은 함수의 계산값을 모두 다 반환한다
print(list(map(lambda x: x * 2, in_data))) # [2, -2, 4, 0, -4, 6, -6, 8]
# 이걸 함수로 표현하면..
def mul2(in_data):
    rtn_list = []
    for val in in_data:
        rtn_list.append(val * 2)
    return rtn_list
print(mul2(in_data)) # [2, -2, 4, 0, -4, 6, -6, 8]


# 리스트 내포 list comprehension
positive_values = [value for value in in_data if value > 0]
print(positive_values) # [1, 2, 3, 4]

# zip : 반복 자료형에 item 갯수가 같아야 함. 결과값을 튜플로 반환
list_1 = [1, 2, 3]
list_2 = [2, 3, 4]
list_3 = list(zip(list_1, list_2))
print(list_3) # [(1, 2), (2, 3), (3, 4)]
print(list(zip("abc", "def"))) # [('a', 'd'), ('b', 'e'), ('c', 'f')]


