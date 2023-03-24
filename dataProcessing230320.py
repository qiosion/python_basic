# Pandas 자료구조 - 시리즈
import pandas as pd

print("---------------------------------------------")
# Dict ==> Series
# dictionary 자료형 { key1: value1, key2: value2, ... , keyN: valueN }
dict_data = {'key1': 1, 'key2': 2}
sr = pd.Series(dict_data)
print(sr)

print("---------------------------------------------")
# 튜플, 리스트 ==> 시리즈 : index 옵션에 인덱스 이름을 지정
list_data = ['홍길동', '19xx-xx-xx', '남', True]
sr = pd.Series(list_data, index=['이름', '생년월일', '성별', '학생여부'])
# tup_data = ('홍길동', '19xx-xx-xx', '남', True)
# sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr)

print("---------------------------------------------")
# 딕셔너리 vs 리스트 인덱스
# Dict : 인덱스가 key
# List : 인덱스가 정수형 인덱스
# 시리즈 : 인덱스 + value(data)
idx = sr.index # RangeIndex 반환
data = sr.values # Data value가 반환
print(idx, data)

print("---------------------------------------------")
# 정수형 인덱스 뿐만 아니라 인덱스 자체를 변경 또는 지정
# rename method 사용
# Data, PI, 2, 3
sr.rename({0: "data", 1: "PI"}, inplace=True) # key와 value 형태로 표현
# inplace=True : 이 변수 sr에 바로 적용
# False라면 다른 변수에 대입하여 사용
print(sr)

print("---------------------------------------------")
# 딕셔너리, 리스트
sr = pd.Series([1, 2, 3], index=["one", "two", "three"])
print(sr)

print("---------------------------------------------")
# tuple vs list
# immutable한 객체 vs mutable한 객체
# index value의 개수는 같아야 함
tup_data = ('2023-03-20', 3.141592, 'ABC', True)
sr = pd.Series(tup_data, index=["date", "PI", "String", "Bool"])
print(sr)

print("---------------------------------------------")
# Series 원하는 데이터를 인덱싱, 슬라이싱, 개별요소 선택
# 인덱싱 : sr[0], sr[1], sr['date']
# 슬라이싱 : sr[0:3] 시리즈에서 0, 1, 2 번을 반환
# 개별요소 선택 : sr[[1, 4]], sr['date', 'PI']


# 여러개의 원소를 선택  : 인덱스 리스트 활용
print(sr[[1, 3]])
print(sr[['생년월일', '학생여부']])
print(sr[1:4]) # 생년월일~학생여부
print(sr['생년월일':'학생여부'])

