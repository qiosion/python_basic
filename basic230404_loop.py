# while문 + break
coffee = 10 # 커피 개수
price = 100 # 커피 가격
money = 300 # 넣은 돈
# 돈이 0원이 되거나(False), 커피가 없으면(break) while 문을 탈출
while money:
    print("돈 받았습니다")
    coffee = coffee - 1
    money = money - price
    print(f"남은 커피 양은 {coffee}개 입니다")
    if coffee == 0:
        print("커피 없음")
        break
# 이때 money가 0이 아니라 애매하게 남으면 True로 인식돼서 계속 돌아감

# vanding machine program 만들어보기
# 돈 넣고 -> 음료 선택 -> 돈이 부족함 / 돈이 충분함 -> 잔돈 + 음료수량 감소
# coffee = 3 # 커피 개수
# coffee_price = 100
# decaf = 3 # 디카페인 커피 개수
# decaf_price = 150
# latte = 3 # 카페라떼 개수
# latte_price = 300
# caramel = 3 # 카라멜라떼 개수
# caramel_price = 300
#
# while True: # 무한루프
#     money = int(input("돈 : "))
#     if money >= 100:
#         drink = input("음료 : ")
#         if drink == 'coffee':
#             print('커피 나옴')
#             coffee -= 1
#             money -= coffee_price
#             print(money, '원 잔돈')
#             break
#     else:


# 나무 찍기
chop_tree = 0 # 나무 찍은 수
while chop_tree < 10:
    chop_tree += 1
    print(f'나무를 {chop_tree}번 찍었습니다')
    if chop_tree == 10:
        print("나무가 넘어갑니다")

# 키보드 입력에 따라서 자료를 추가, 삭제, 보이기 하는 프로그램
# 예외처리 : if []: print("추가/삭제 를 할 수 없습니다")
prompt = """
    1. Add
    2. Del
    3. List
    4. Quit
    Enter number:
"""
number = 0
a = []
while number < 4:
    print(prompt)
    number = int(input())
    if number==1:
        print("추가할 값을 입력하세요")
        input_var = int(input())
        a.append(input_var)
    elif number==2:
        print("삭제할 값을 입력하세요")
        input_var = int(input())
        if input_var in a:
            a.remove(input_var)
        else:
            print("존재하지 않는 값입니다")
    elif number==3:
        print(a)
    else:
        print("프로그램 종료")


