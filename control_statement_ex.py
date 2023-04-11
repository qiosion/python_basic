a = [(1, 3), (2, 4), (3, 5)]

for (f, r) in a: # 리스트 a의 첫번째 값 (f, r) 세트
    print(f + r)

for val in a: # 리스트의 첫번째 값, 즉 (1, 3)이 그대로 들어감
    print(val[0] + val[1])

points = [90, 25, 67, 45, 80]
number = 0 # 몇번째 학생인가
for val in points: # for idx in range(len(points))
    number += 1
    if val < 60: # if points[idx] < 60
        print(f'{number}번째 학생은 불합격입니다')
    else:
        print(f'{number}번째 학생은 합격입니다')

# range(이상, 미만, step)
# 파라미터, 인자 등은 생략 가능

# List 내포
a = [1, 2, 3, 4]
result = []
for val in a:
    result.append(val * 3)
print(result)

result_comp = [val * 3 for val in a]
print(result_comp)

# 리스트 내포를 이용한 구구단
ggd = [x * y for x in range(2, 10)
       for y in range(1, 10)]
print(ggd)

