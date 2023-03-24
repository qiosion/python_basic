# list "+" 연산할 때, 같은 자료형끼리만 덧셈이 가능함
# 문자열에서 "+" 는 연결하는 연산자
a = [1, "a", 2, "b"]
print(a[0] + a[2], a[0] * a[2])

# 자료형2 - practice1 (p.8)
# 리스트를 이용해 집을 표현
# 인덱싱, 슬라이싱, 문자열, 포맷팅, 내장함수, .append()
list_2 = [30, 3, ["study", "bed", "game"], "1층", "3억"]

# 방의 용도를 가지고 와서 표현하기 위해서는
print(list_2[2][0])

str2 = f'My house area is {list_2[0]}, there are {list_2[1], len(list_2[2])} ' \
    f'I like the {list_2[2][2]}'
print(str2)

# 리스트 더하기
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

# 내장함수를 설명하기 전에,
# append() 내장함수
# shallow copy vs deep copy in python

# shallow copy
a = [[1, 2], [3, 4]]
b = a[:] # copy
b = a.copy()
print('a의 id :' , id(a) , ' , b의 id :' , id(b))
# 카피를 했어도 id(메모리주소)가 다르다 -> 독립된 위치를 갖고있다

# a의 값을 변경(수정)
a[0] = [5, 6]
print(a, b)

# a의 첫번째 원소에 특정한 값을 append
a[1].append(7)
print(a, b) # a와 b 모두에게 원소가 추가된걸 확인할수있다

# 이런 일을 방지하기 위해 deep copy 를 이용한다
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
print('a의 id :' , id(a) , ' , b의 id :' , id(b)) # 여전히 id는 다르긴 함

# a의 값을 변경(수정)
a[0] = [5, 6]
print(a, b)

# a의 첫번째 원소에 특정한 값을 append
a[1].append(7)
print(a, b) # a만 변했다!


# list add / delete
list_a = [1, "2", 4]
print(id(list_a), id(list_a[1]))

list_a[1] = 4 # [1, 4, 4]
print(id(list_a[1]), id(list_a[2]))
# 전체 리스트를 가리키는 주소는 변경되지 않고,
# list_a[1]번째가 "2"가 들어가있는 메모리 주소를 참조하고 있다가
# list_a[1] = 4를 통해서 "2"를 가리키고 있던 포인터를 제거하고
# 4가 들어있는 메모리 주소를 다시 참조..
# "2"를 참조하고 있던 포인터는 가비지 컬렉션을 통해 정리가 됨

# 내장함수 append
list_a = [1, 2, 3]
list_a.append([8, 9, 4, 5, 6])
print(list_a)

list_a.append("string")
list_a.append(3.14)
print(list_a)

# 내장함수 sort
# list_a.sort() # 오류
# print(list_a)

list_a[3].sort() # 리스트 안의 리스트도 정렬 가능
print(list_a)

# 내장함수 reverse
# reverse : 리스트 요소 반대로 뒤집음(순서 정렬은 X)
tmp = [8, 9, 3, 5, 7]
print(tmp.sort(reverse=True)) # 왜 None??????????????????


# 슬라이싱을 통해 숫자와 문자열을 각각 sort
test = [2, 4, 1, 'd', 'b', 'c']
tmp = test[3:]
    # ['d', 'b', 'c']
print(tmp)
print(tmp.reverse()) # 왜 None 이야?


# 내장함수 index("특정 자료형에 해당하는 값") => 인덱스를 반환
print(tmp.index('d'))

# 내장함수 insert
test = [2, 4, 1, 'd', 'b', 'c']
test.insert(0, [1, 2, 3])
print(test)

# 인덱스 파라미터(인자)가 정상적이지 않으면? 에러 발생 X 그냥 맨 끝에 insert
test.insert(8, "e")
print(test)

# 내장함수 remove
test = [[4, 2, 3], 2, 4]
test.remove(4) # 해당 요소를 삭제
print(test)

# 내장함수 pop
test = [2, 4, 1, 'd', 'v',' q']
test.pop(2) # 해당 인덱스를 삭제
print(test)
# 특정한 인덱스에 있는 자료형을 pop을 통해 삭제