a = True
b = False
print(type(a), type(b))
print(f'1과 1은 같은가? {1==1}, 1과 2는 같은가? {1==2}, 1는 2보다 작나? {1<2}')

print(">>> 문자열에 값이 있는 상태면 True인걸 이용해보자")
str_1 = "Hello"
idx = 1
while str_1: # 문자열에 값이 있는 상태면 True인걸 이용한 것
    print(idx, len(str_1), str_1)
    str_1 = str_1[:len(str_1)-idx] # 슬라이싱. 맨 끝의 글자를 1씩 잘라낸것

print(">>> 위의 것을 조건식으로 작성해보자")
str_2 = "Hello"
idx = 1
while len(str_2)!=0:
    print(idx, len(str_2), str_2)
    str_2 = str_2[:len(str_2) - idx]

print(">>> 1 = True / 0 = False")
if 1:
    print("True")

print(">>> 빈값 -> 거짓")
if []: # if문 조건식이 False가 나왔으므로 else를 출력한다
    print("True")
else:
    print("False")

print(">>> 값이 있다면 -> 참")
if [1,2,3]:
    print("True")
else:
    print("False")

print(f"{bool('Python')}, {bool('')}")

print(">>> copy")
a = [1, 2, 3]
b = a[:]
c = a.copy()

print(">>> 변수를 만드는 여러가지 방법")
a, b = ("coding", "life")
(a, b) = ("coding", "life")
[a, b] = ["coding", "life"]
print(type(a), type(b), a, b)

a = ("coding", "life")
print(type(a))
a = "coding", "life" # 튜플
print(type(a))

print(">>> swap")
a, b = 3, 10
print(a, b)
a, b = b, a
print(a, b)
