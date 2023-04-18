class Family:
    lastname = "김" # Family 클래스 안에 클래스 변수 lastname 선언

# Family 클래스로 만든 객체를 통해서도 클래스 변수 사용 가능
a = Family()
b = Family()

print(a.lastname) # 김
print(b.lastname) # 김

# Family 클래스의 lastname 을 변경하면 클래스로 만든 객체의 lastname 값도 모두 변경됨
Family.lastname = "박"

print(a.lastname) # 박
print(b.lastname) # 박

# id 함수를 통한 클래스 변수 확인
# 클래스로 만든 모든 객체의 클래스 변수가 모두 같은 메모리를 가지고 있음
print(id(Family.lastname)) # 1736927797264
print(id(a.lastname)) # 1736927797264
print(id(b.lastname)) # 1736927797264