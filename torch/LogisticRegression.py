import torch
import torch.nn.functional as F


# input data : 6x2
x_data = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10],
    [11, 12]
]

# Binary Classification 이므로
# output data : 6x1
y_data = [
    [0],
    [0],
    [0],
    [1],
    [1],
    [1]
]

# list to Tensor for training using Torch
x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)

# 수식을 적어보자
# W, b (requires_grad=True)
# wx+b ==> 입력데이터 multiplication (mxn) ==> 출력데이터
# (6x2) * (2x1) = (6x1)
# w = torch.randn((2, 1), requires_grad=True)
w = torch.zeros((2, 1), requires_grad=True) # 이건 왜 될까?
b = torch.zeros(1, requires_grad=True)

optim = torch.optim.SGD([w, b], lr=1e-5)

# 학습 코드 작성
# +1 : Loss값을 출력할 때 마지막 값까지 보기 위해서
nb_epoch = 10000
for epoch in range(nb_epoch+1):

    # hypothesis 계산
    # 가설함수 시그모이드 직접 작성
    hx = 1 / (1 + torch.exp(-(x_train.matmul(w) + b)))
    # 혹은 torch 내장함수 sigmoid 사용
    # hx = torch.sigmoid(x_train(w)+b)

    # cost 계산 (예측값 hx, 정답값 y_train)
    cost = -((y_train * torch.log(hx)) + \
           (1-y_train) * torch.log(1-hx)).mean()

    # 아래와 같이 적어도 됨
    # cost = F.binary_cross_entropy(hx, y_train)

    # gradient Descent Algorithm
    # zero_grad()는 반드시 해야 한다. 아니면 값이 누적됨
    optim.zero_grad()
    cost.backward()
    optim.step()

    if epoch % 1000 == 0:
        print(f'Epoch: {epoch}/{nb_epoch}, Cost: {cost.item(): .6f}, {cost.data}')

# 학습된 weight 와 bias 값 출력
# print('w : ', w, ', b : ', b)
# w :  tensor([[0.0611],[0.0496]], requires_grad=True) ,
# b :  tensor([-0.0115], requires_grad=True)

hypothesis = torch.sigmoid(x_train.matmul(w) + b) # 6x1

pred = []

# sigmoid(x_train * weight  + b) 의 결과값이 0.5보다 크면 1, 아닐경우 0
for val in list(hypothesis):
    if val >= 0.5: pred.append(1)
    else: pred.append(0)

# print(pred)
# lr=1e-5의 경우 [1, 1, 1, 1, 1, 1]
# lr=1e-2로 올리면 [0, 0, 0, 1, 1, 1]



