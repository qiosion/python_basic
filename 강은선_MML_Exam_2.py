import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 6]

weight_data = np.linspace(-2.0, 6.0, 100)

axisX = [] # x축
cost = []
data = -2.0
for i in range(100):
    axisX.append(data)
    data = data + 0.08  # (6-(-2))/100

    val = (axisX[i] * x[0] - y[0]) ** 2 + \
          (axisX[i] * x[1] - y[1]) ** 2 + \
          (axisX[i] * x[2] - y[2]) ** 2
    cost.append(val)

plt.plot(weight_data, cost)
plt.show()