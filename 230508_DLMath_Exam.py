# 1번
# def my_max(input_list):
#     max = 0
#     for var in input_list:
#         if max < var:
#             max = var
#     return max
# def prime_factorization(input_num):
#     n = 2
#     prime_factor = []
#
#     while n <= input_num:
#         if input_num % n == 0:
#             prime_factor.append(n)
#             input_num = input_num // n
#         else:
#             n = n + 1
#
#     rtn_value = set(prime_factor)
#     return my_max(rtn_value)
#
# print("input num : ", end="")
# input_num = int(input())
#
# max_value = prime_factorization(input_num)
# print(f'result: {max_value}')

# 2번
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = [1, 2, 3]
# y = [2, 4, 6]
# weight_data = np.linspace(-2.0, 6.0, 100)
#
# axisX = [] # x축
# cost = []
# data = -2.0
# for i in range(100):
#     axisX.append(data)
#     data = data + 0.08  # (6-(-2))/100
#
#     val = (axisX[i] * x[0] - y[0]) ** 2 + \
#           (axisX[i] * x[1] - y[1]) ** 2 + \
#           (axisX[i] * x[2] - y[2]) ** 2
#     cost.append(val)
#
# plt.plot(weight_data, cost)
# plt.show()

# 3번
import numpy as np

def sigmoid(val):
    return 1 / (1 + np.exp(-val))

lr = 0.5 # Learning Rate

x1, x2 = 0.1, 0.2

w1 = 0.2
w2 = 0.23
w3 = 0.38
w4 = 0.35
w5 = 0.42
w6 = 0.32
w7 = 0.64
w8 = 0.6

z1 = w1 * x1 + w2 * x2
h1 = sigmoid(z1)

z2 = w3 * x1 + w4 * x2
h2 = sigmoid(z2)

z3 = w5 * h1 + w6 * h2
dz3_w5 = h1
dz3_w6 = h2
z4 = w7 * h1 + w8 * h2
dz4_w7 = h1
dz4_w8 = h2

o1 = sigmoid(z3)
o2 = sigmoid(z4)
# print("o1 : ", o1, ", o2 : ", o2)

target_o1 = 0.4
target_o2 = 0.6

Eo1 = 0.5 * (target_o1 - o1) ** 2
Eo2 = 0.5 * (target_o2 - o2) ** 2

Etotal = Eo1 + Eo2

print(z1, z2, h1, h2, z3, z4, o1, o2, Etotal)

def backpropagation_1(weight, d_weight, target, output):
    weight = weight - lr * ( -(target - output) ) * ( (output * (1 - output)) ) * d_weight
    return round(weight, 4)

if __name__ == '__main__':
    print(backpropagation_1(w5, dz3_w5, target_o1, o1))
    print(backpropagation_1(w6, dz3_w6, target_o1, o1))
    print(backpropagation_1(w7, dz4_w7, target_o2, o2))
    print(backpropagation_1(w8, dz4_w8, target_o2, o2))
