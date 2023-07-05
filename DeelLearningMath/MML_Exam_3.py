import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F


def read_file(file_name):
    rtn_list = []
    cnt = 0
    try:
        f = open(file_name, "r")
        while True:
            line = f.readline()
            if not line:
                break
            rtn_list.append(list(map(float, line.rstrip("\n").split("\t"))))
            cnt += 1
        f.close()
        return rtn_list, cnt
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    house_info, cnt = read_file("sell_house.txt")

    # Linear Regression (Machine Learning)
    x_train = np.array(house_info[:-5])[:, :-1]
    y_train = np.array(house_info[:-5])[:, -1]
    x_train = np.concatenate((x_train, np.ones((x_train.shape[0], 1))), axis=1)  # Add a column of ones for the intercept
    x_test = np.array(house_info[-5:])[:, :-1]
    x_test = np.concatenate((x_test, np.ones((x_test.shape[0], 1))), axis=1)  # Add a column of ones for the intercept

    model = nn.Linear(x_train.shape[1], 1)
    optimizer = optim.SGD(model.parameters(), lr=1e-7)
    nb_epochs = 10000

    for epoch in range(nb_epochs + 1):
        inputs = torch.FloatTensor(x_train)
        targets = torch.FloatTensor(y_train)

        optimizer.zero_grad()
        pred = model(inputs)
        cost = F.mse_loss(pred.squeeze(), targets)
        cost.backward()
        optimizer.step()

        if epoch % 1000 == 0:
            print("Epoch {:4d}/{} Cost: {:.6f}".format(epoch, nb_epochs, cost.item()))

    x_test_tensor = torch.FloatTensor(x_test)
    pred_y = model(x_test_tensor)
    print(pred_y)

    # Projection Matrix (Linear Algebra)
    test_A = np.array(house_info[-5:])[:, 1:]
    test_A = np.concatenate((test_A, np.ones((test_A.shape[0], 1))), axis=1)  # Add a column of ones for the intercept
    x = np.linalg.lstsq(x_train, y_train, rcond=None)[0]
    test_result = np.matmul(test_A, x)
    print(test_result)

"""
# Ground Truth
[37.9, 38.9, 36.9, 45.8, 41.0]

# Linear Regression (Machine Learning)
40.3447
45.5422
16.3366
35.0740
33.9402

# Projection Matrtix (Linear Algebra)
352.71429555
402.00186052
330.23014248
394.00541348
341.10433153
"""