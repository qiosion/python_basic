# 집합 set
s1 = set([1, 2, 3]) # sort 기능 없음
s2 = set("Hello")
print(s1, s2)

# set 자료형은 순서가 없고, 중복을 허용하지 않음
# => 인덱스를 통한 접근 불가능
s1_tuple = tuple(s1)

# 교집합, 합집합, 차집합
set_a = set([1, 2, 3, 4, 5, 6])
set_b = set([3, 4, 7, 8, 9, 10])

print(f'set_a와 set_b의 교집합은 {set_a.intersection(set_b)}')
print(f'set_a와 set_b의 합집합은 {set_a.union(set_b)}')
print(f'set_a와 set_b의 차집합은 {set_a.difference(set_b)}')

# 차집합의 경우, set_a - set_b != set_b - set_a

# set 관련 함수
set1 = set([1, 2, 3, 4, 5, 6])
# add : 하나의 값 추가
set1.add('5') # 문자열 5를 추가했으므로 중복 X
# print(set1) => {'5', 1, 2, 3, 4, 5, 6}
set1.add(1) # 중복
# print(set1) => {'5', 1, 2, 3, 4, 5, 6}

# update : 여러개의 값 추가
set1.update(['3', '4'])
# print(set1) => {1, 2, 3, 4, 5, 6, '3', '4', '5'}

# remove : 특정 값 하나 삭제
set1.remove(4)
# print(set1) => {1, 2, 3, 5, 6, '4', '3', '5'}
