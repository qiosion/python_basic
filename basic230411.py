# 제어문 for문
# 구구단 만들기 : 2중 for문
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print('')

# 리스트 내포 1
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result)

result = [num * 3 for num in a]
print(result)

# 리스트 내포 3 : if조건
result = [num * 3 for num in a if num % 2 == 0] # 짝수일 때
print(result)

