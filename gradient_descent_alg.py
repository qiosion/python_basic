# Gradient Descent Algorithm
# D:\KES\Python\python_basic\deepLearning230320.py 과 이어짐

import matplotlib.pyplot as plt
import numpy as np

# y = wx + b : 기울기가 w고 y절편이 b인 직선
w, b = 0.4, 0.6 # 정답을 하나 만들어보기 위해서 지정한 값

# x의 범위
x = np.random.rand(50) # 0~1 사이를 균등분포로 나누고, 랜덤으로 50개 가지고 옴

# x에 따른 y의 값
y = w * x + b

# 노이즈 noise 더하기
noise = np.random.uniform(-0.03, 0.03, 50)
# -0.03에서 0.03까지를 균등하게 50개로 자른 다음, 랜덤하게 가지고 오겠다

y_noise = y + noise

"""
rand 와 uniform 차이는 범위 지정
- rand : 0 ~ 1
- uniform : 지정한 인자 값
"""

plt.plot(x, y, color='r') # 빨간색
plt.scatter(x, y_noise) # 산점도
# plt.show()

# initialize w, b values (w와 b 값 초기화)
w = np.random.uniform(low=-1.0, high=1.0)
b = np.random.uniform(low=-1.0, high=1.0)

lr = 0.05 # learning weight
costs = []

epoch = 1000 # 에포크 : 학습의 횟수
# epochs = 40이라면 전체 데이터를 40번 사용해서 학습을 거치는 것

for i in range(epoch):
    y_hat = w * x + b # y_hat = wx + b
    cost = ((y_hat - y) ** 2).mean() # (y_hat - y)^2의 평균

    w = w - lr * (2 * (y_hat - y) * x).mean() # 뭘.. 미분한 것이 2(y_hat - y)x 였음
    b = b - lr * (2 * (y_hat - y)).mean()

    costs.append(cost)

    if i % 100 == 0:
        print(f'epoch = {i}, w = {w:.6f}, b = {b:.6f}, error = {cost:.6f}') # 터미널 창에 보이는 값

plt.figure(figsize=(10, 7)) # 그림의 사이즈. 단위는 인치
plt.plot(costs) # 아무것도 적지않으면 선 그래프를 보여줌
plt.xlabel("Epochs")
plt.ylabel("Cost")
plt.show()










