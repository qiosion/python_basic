# # string 자료형
# str1 = "python is interperter language\n" # \n : new line
# str2 = "python is a very easy"
# print(str1, str2) # 이어서 출력하면 엔터대신 띄어쓰기로 표현됨
#
# # 따옴표 " 자체를 문자열로 표현
# # 1. 백 슬래시 \ 이용
# # 2. 작은따옴표 ' ' 이용
# str1 = "We have to learn the \"python\""
# print(str1)
#
# multiline = """
# Life is too short,
# We have to learn the python
# """ # 멀티라인 """ 이지만 주석처리와 같은 표현방법이니 사용하지 말기
# print(multiline)

# # + : concatenation 문자열 연결
# # * : 반복
# str0 = "@Author"
# str1 = "Hi everyone. "
# str2 = "My name is sun :)"
# str3 = "**********" # comment block
# # print(f'{str3 * 3}\n{str0}\n{str1 + str2},\n'
# #       f'This is the comment block\n'
# #       f'{str3 * 3}')
#
# # 인덱싱 indexing, 슬라이싱 slicing 실습
# # length : len() => 문자열의 갯수를 반환
# print(len(str2))
#
# # mutable vs immutable 한 객체
# print(str2[-6]) # s
#
# #TypeError: 'str' object does not support item assignment
# # str2[-6] = 'S'
#
# # str2 = "My name is sun :)" 의 대소문자 수정에 슬라이싱을 이용해보자
# # [ start index : end index] => 시작 이상 ~ 끝 미만
# # [: end index] => start index = 0
# # [2:] => 2번째부터 끝까지라는 뜻
#
# # "My name is " : str2[0:11] = str2[:-6]
# # "S"
# # "un :)" : str2[-5:] = [len(str2)-5:]
# str2 = str2[:-6] + "S" + str2[-5:]
# print(str2)

# 문자열 내장함수
a = "hobby"
a.count('b')
print(a.count('b')) # 2

a.find('b')
print(a.find('b')) # 2

a.find('a')
print(a.find('a')) # -1 : 없음

",".join("abcd")
print(",".join("abcd")) # a,b,c,d

a.upper()
print(a.upper()) # HOBBY

str = "    hi              "
lst = str.lstrip()
rst = str.rstrip()
stst = str.strip()
print(lst) # hi
print(rst) #     hi
print(stst) # hi

a = "Life is : too : short"
rep = a.replace("Life", "Your leg")
print(rep) # Your leg is : too : short

spl = a.split() # 공백을 기준으로 문자열을 나눔
print(spl) # ['Life', 'is', ':', 'too', ':', 'short']

spl2 = a.split(":") # : 를 기준으로 문자열을 나눔
print(spl2) # ['Life is ', ' too ', ' short']