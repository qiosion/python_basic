# gradient_descent_algorithm
import matplotlib.pyplot as plt
import numpy as np

# 그래프 그리기 Convex
# f(x) = ax + b ==> wx + b (b를 고려하면 3차원이 되므로, b term은 제거)
# H(x) = wx

x = [1, 2, 3]
y = [1, 2, 3]
# H(x)는 예측 값, y는 실제값 (== GT: Ground Truth == 참값 == 정방값)

# -3.0 ~ 5.0 을 100등분 한 것을 weight_data라는 변수에 넣겠다
weight_data = np.linspace(-3.0, 5.0, 100) # w : 가중치 -> 기울기
# (5 - (-3)) / 100 ==> [-3.0, -3.0 + 0.08, ... , 5.0 ] # 간격 0.08

# 리스트변수명.append(값) : 리스트에 값을 추가하는 메서드

weight_data = [] # x축
data = -3.0

for i in range(100):
    weight_data.append(data)
    data = data + 0.08 # (5-(-3))/100

# y축에 해당하는 값을 생성 - x축과 그 크기가 같아야 함
# (wx[0] - y[0])^2 + (wx[1] - y[1])^2 + (wx[2] - y[2]^2)/3
cost = []

for i in range(100):
    val = (weight_data[i] * x[0] - y[0]) ** 2 + \
          (weight_data[i] * x[1] - y[1]) ** 2 + \
          (weight_data[i] * x[2] - y[2]) ** 2
    cost.append(val)

plt.plot(weight_data, cost)
plt.show()