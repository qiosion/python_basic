# 허프 변환 Hough Transform

"""
1. make data
x = 0 ~ 49
y = 2x + 1

x = [0, 1, 2, ... ,49]
y = [1, 3, 5, ...]
"""
import matplotlib.pyplot as plt

x = list(range(50))

"""
y = []
for i in range(len(x)):
    y.append(2 * i + 1)

위의 식을 람다로 쓰는 방법도 있다
y_axis = lambda x: (x * 2) + 1            -> 이건 어디서 갑자기 왜 나온거고
# 람다를 사용해서 x 를 받음. 출력값은 x * 2 + 1

"""
y = list(map(lambda arg: (arg * 2) + 1, x)) # 이게 이해가 안됨. x는 왜... 나오는거지...
# x 가 리스트고
# 전체 결과값(y)을 리스트로 만들고싶다면 map으로 묶어준 뒤 list로 캐스팅해야함

# print(x, y)


y_noise = []
range_data = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5] # list(range(-5, 6, 1)) 이라고 해도 됨
import random

for data in y:
    y_noise.append(data + random.choice(range_data))

print(y)
print(y_noise)

plt.plot(x, y, color='r')
plt.scatter(x, y_noise)
# plt.show()

import numpy as np
# 2. theta, rho (Ρ, ρ) 범위 지정, lookup table 생성
rows, cols = max(y_noise), max(x) # 최대값으로 지정

d = np.sqrt(rows ** 2 + cols ** 2) # 범위
d = d.astype(int) # 배열 값을 정수화

# 세타와 로 범위 설정
theta_range = list(range(-90, 91, 1)) # theta : 각도. 180도 도는것 ???
rho_range = list(range(-d, d+1, 1)) # rho : 거리

# look up table : 자주 계산 되는 것을 테이블 형태로 만들고, 인덱스로 접근해서 값을 바로 가지고 오도록 만든 테이블
# deg2rad = deg to rad : 각도 deg (degree)를 라디안 rad (radian) 으로 바꿈
cos_thetas = np.cos(np.deg2rad(theta_range)) # 코싸인
sin_thetas = np.sin(np.deg2rad(theta_range)) # 싸인

# accumulator : 축적기 ??
# 0으로 채워진 N x M 행렬 matrix 생성
accumulator = np.zeros((len(rho_range), len(theta_range)))

for col in x:
    for theta_idx in range(len(theta_range)):
        # rho = x * cos(t) + y * sin(t)
        rho = int(d + col * cos_thetas[theta_idx] + y_noise[col] * sin_thetas[theta_idx])
        accumulator[rho, theta_idx] += 1 # 누적

# lines 유추되는 rho, theta 쌍을 추출할 수 있음
# 10개 이상 누적된 경우에만 라인으로 인정
lines = []
for j in range(accumulator.shape[0]): # shape[0] = rho
    rho = rho_range[j]
    for i in range(accumulator.shape[1]): # shape[1] = theta
        if accumulator[j][i] > 10: # j번째 행의 i번째 칼럼에 누적된 값이 10개 이상일 경우
            theta = np.deg2rad(theta_range[i])
            lines.append([rho, theta])

print(lines)

# 추출된 rho, theta 값으로 기울기, 절편 계산
# 기울기 : -cos(t) / sin(t)
# 절편 : rho / sin(t)

gradient = [] # 기울기
intersection = [] # 교집합

for line in lines:
    rho = line[0]
    theta = line[1]

    gradient.append(-(np.cos(theta) / np.sin(theta)))
    intersection.append(rho / np.sin(theta))



