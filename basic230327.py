# 함수 잠깐

def sorting(a):
    a.sort()

def sorting_rtn(a):
    a.sort()
    return a

input_1 = [1, 6, 2, 5, 4, 3] # 정렬되지 않은 배열
print("리턴 값이 없는 함수 >>> sorting(input_1)")
print(sorting(input_1)) # None. 왜? return값 없고 그냥 정렬만 하는 함수니까!
print(input_1) # 정렬된 input_1 배열을 출력
# print(input_1.sort())

input_2 = [1, 6, 2, 5, 4, 3]
print("리턴 값이 있는 함수 >>> sorting_rtn(input_2)")
print(sorting_rtn(input_2))