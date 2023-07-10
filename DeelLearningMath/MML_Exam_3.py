import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

torch.manual_seed(1)

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
    x_train = np.array(house_info)[:-5, 1:-1]
    print("x_train")
    print(x_train.shape) # (23, 11)

    y_train = np.array(house_info)[:-5, -1]
    y_train = y_train.reshape(cnt - 5, 1)
    print("y_train")
    print(y_train.shape) # (23, 1)

    x_test = np.array(house_info)[-5:, 1:-1]
    print("x_test")
    print(x_test.shape) # (5, 11)

    y_test = np.array(house_info)[-5:, -1:]
    print("y_test")
    print(y_test.shape) # (5, 1)

    x_train = torch.FloatTensor(x_train)
    y_train = torch.FloatTensor(y_train)
    print("after FloatTensor")
    print(x_train.shape, y_train.shape)
    # torch.Size([23, 11]) torch.Size([23, 1])

    x_hat = np.matmul(np.matmul(np.linalg.inv(np.matmul(x_train.T, x_train)), x_train.T), y_train)
    print("x_hat")
    print(x_hat.shape)

    model = nn.Linear(11, 1)
    optimizer = optim.SGD(model.parameters(), lr=1e-6)
    nb_epochs = 20000

    for epoch in range(nb_epochs + 1):
        # inputs = torch.FloatTensor(x_train)
        # targets = torch.FloatTensor(y_train)

        pred = model(x_train)
        cost = F.mse_loss(pred, y_train)

        optimizer.zero_grad()
        # pred = model(inputs)
        # cost = F.mse_loss(pred.squeeze(), targets)
        cost.backward()
        optimizer.step()

        if epoch % 100 == 0:
            print(f'Epoch:{epoch}, Cost:{cost.item():.4f}')

    # print(f'w, b{list(model.parameters())}')

    x_test_tensor = torch.FloatTensor(x_test)
    pred_y = model(x_test_tensor)
    print(pred_y)

    # Projection Matrix (Linear Algebra)
    test_A = np.array(house_info)[-5:, 1:-1]

    # test_A = np.concatenate((test_A, np.ones((test_A.shape[0], 1))), axis=1)
    # x = np.linalg.lstsq(x_train, y_train, rcond=None)[0]
    test_result = np.matmul(test_A, x_hat)
    print(test_result)

"""
# Ground Truth
[37.9, 38.9, 36.9, 45.8, 41.0]

# pred_y    :   Linear Regression (Machine Learning)
tensor([[36.3014],
        [46.4926],
        [38.0962],c 
        [44.7135],
        [44.1822]], grad_fn=<AddmmBackward0>)
     

# test_result   :   Projection Matrix (Linear Algebra)
tensor([[40.4278],
        [47.6853],
        [41.5268],
        [44.7408],
        [53.5413]], dtype=torch.float64)

# Linear Regression (Machine Learning)


# Projection Matrtix (Linear Algebra)

"""