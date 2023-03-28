# 딕셔너리 Dictionary Type = {key1 : value1, key2 : value2, ... }
a = {1:'a', 2:'b'}
# print(a) => {1: 'a', 2: 'b'}

# dict[key] : key 를 지정하는 용도로 사용
# 타 자료형은 대부분 [index]

# key 값 'name' 에 이름의 집합(list, tuple)을 value 로 넣어보자
a['name'] = ['shin', 'park', 'kang']
# print(a) => {1: 'a', 2: 'b', 'name': ['shin', 'park', 'kang']}

# 삭제할 때도 key 값을 기준으로 삭제
del a[1] # key = 1 인 키:값 한쌍을 삭제
# print(a) => {2: 'b', 'name': ['shin', 'park', 'kang']}

# 폴리텍 학과와 그 학생 수
# 키에는 mutable 한 객체를 사용할 수 없음
# value 는 어떠한 자료형을 사용해도 무관 (Don't care: immutable, mutable)
polytec = {"dept": ["AI-Engineering", "Smart Electronic", "contents design"], "student_number": (22, 46, )}

# polytec 기준으로 student_number 키와 쌍이 되는 value의 원소 개수 : 2개
# polytec 기준으로 키와 쌍이 되는 value의 개수 : 2개
print(polytec["dept"], polytec["student_number"])
# 그러나 dept의 원소 개수와 student_number의 원소개수가 일치해야하는건 아님

print(polytec["dept"][0]) # 리스트처럼 작성은 가능하지만, 그 내장함수는 사용불가

# 키가 중복될 경우, 하나만 적용이 됨

# 키에는 mutable 한 객체를 사용할 수 없음 ==> 에러를 발생시켜 확인해보자
# key_mut = {
#     ['name', 'age'] : [['shin', 'park', 'kang'], [42, 23, 60]]
# }
# print(key_mut) => TypeError: unhashable type: 'list'

key_mut = {
    # ['name', 'age'] : [['shin', 'park', 'kang'], [42, 23, 60]]
    ('name', 'age') : [['shin', 'park', 'kang'], [42, 23, 60]]
}
print(key_mut) # key 값이 튜플(immutable) 이라 ㅇㅋ
# (name, age) <-- 이 튜플 1개 전체가 키값이므로, 키값으로 찾으려면 전체를 작성
key_mut[('name', 'age')]

a = {
    'name': ['kang', 'goo', 'kim1', 'kim2'],
    'ID': [23001, 23002]
}

list_tmp = ['name', 'ID']
print(list_tmp) # 리스트 내장함수 사용 가능

# keys()
dict_keys = a.keys()
print(dict_keys)

# key 값 뽑아내는 방법
# 1
for k in a.keys(): # dict_keys(['name', 'ID'])
    print(k)

# 2
# for (int i = 0; i < 10; i++)
for idx in range(len(list_tmp)):
    print(list_tmp[idx])

# 리스트 내장함수 -> 딕셔너리 사용불가능 확인
list_tmp.append('phone')
# dict_keys.append('phone') # 불가능

# 꼭 list 함수를 쓰고싶다면 형변환 casting 이용
dict_list = list(a.keys())
print(type(dict_list), type(dict_keys))
dict_list.append('phone')

# 리스트 뿐 아니라 다른 자료형도 변환 가능
b = "123"
c = int(b)
# 자바에서는 (원하는 자료형)변수명


# values()
dict_values = a.values()
print(dict_values, type(dict_values))
# dict_values([['kang', 'goo', 'kim1', 'kim2'], [23001, 23002]]) <class 'dict_values'>
dict_values_list = list(dict_values)

# items()
print(a.items(), type(a.items()))
# dict_items([('name', ['kang', 'goo', 'kim1', 'kim2']), ('ID', [23001, 23002])]) <class 'dict_items'>

dict_items_list = list(a.items())
print(dict_items_list[0][1][0]) # kang
