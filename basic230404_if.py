# if문 예시
money = 2000
if money >= 3000:
    print("택시타라")
else:
    print("버스타라")

card = True
if money >= 3000 or card:
    print("택시타라")
else:
    pass # 특별하게 할 건 없지만 else문을 남겨두고 싶을 땐 pass를 작성해야 정상적으로 실행됨


# if문 -> True / False
sum_var = 0
for i in range(10):
    sum_var += i
print(sum_var) # 45

if(not sum_var): # sum_var == True. 즉 not sum_var == False
    print(sum_var) # 출력하지 않는다

# in 연산자
list_var = [1, 2, 3, 4, 5]
if 8 in list_var:
    print("리스트에 있다")
else:
    print("찾을수 없다")