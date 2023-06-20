import torch
import numpy as np
import matplotlib.pyplot as plt

# function name : get_data
# param in : None (or file)
# param out : input x, y(Ground Truth)
# Description
"""
데이터를 가지고 오는 함수
"""
def get_data():
    train_X = np.array([3.3, 4.4, 5.5, 6.71, 6.93, 4.168, 9.779, 6.182, 7.59, 2.167,
                        7.042, 10.791, 5.313, 7.997, 5.654, 9.27, 3.1])
    train_Y = np.array([1.7, 2.76, 2.09, 3.19, 1.694, 1.573, 3.366, 2.596, 2.53, 1.221,
                        2.827, 3.465, 1.65, 2.904, 2.42, 2.94, 1.3])

    x = torch.from_numpy(train_X)
    y = torch.from_numpy(train_Y)

    return x, y

# function name : get_weights
# param in : None
# param out : random weight and bias
# Description
"""
- weight, bias : random normal 한 값으로 셋팅
- randn : 평균이 0이고 표준편차가 1인 가우시안 정규분포
    <-> rand : 0~1 사이의 값을 균등하게 생성해서 반환
    - (w=1.0, b=1.0) 해도 상관없음???
- 중요 : w, b는 항상 미분이 되어야 함(최적값을 찾기 위해)
    => requires_grand=True 셋팅 (반드시!)
"""
def get_weights():
    w = torch.randn(1)
    w.requires_grad = True # 미분 가능하게 셋팅
    b = torch.randn(1)
    b.requires_grad = True # 미분 가능하게 셋팅

    return w, b

# function name : simple_network 뭐.. hypothesis_function 이라 해도 되고
# param in : x(입력값), w(가중치 초기값 => update), b(편향 초기값 => update)
# param out : 리턴값
# Description
"""
H(x) = Wx + b
return h(x)
input : x, w, b
- w : 1D vector
-> w*x 는 (scalar * vector) 라서 문제 없음
-> b는 파이토치에서 broadcasting를 통해 자동 연산
"""
def simple_network(x, w, b):
    y_pred = w * x + b # y예측값. y hat. ^y. H(x)
    return y_pred

# function name : loss_fn
# param in : y, y_predict(GT값, 예측값), w, b
    # w, b 는 loss.backward() 함수 호출 시 미분을 계산했는지 예측하기 위해 사용
# param out : 리턴값
# Description
"""
MSE(Mean Squared Error)를 손실함수 Loss Function으로 정의
Loss function 자체가 w, b 함수로 이루어져 있으며, w, b에 대해 미분해야 함
loss.backward() : MSE의 기울기(gradient, 미분)을 계산
    -> w, b에 대해서 미분해서 기울기 출력
"""
def loss_fn(y, y_pred, w, b):
    loss = torch.mean(((y_pred - y)**2).sum())
    for param in [w, b]:
        if not param.grad is None:
            # 한번이라도 미분을 수행했으면, 초기화하고 다시 미분
            param.grad.data.zero_()
    loss.backward() # MSE의 기울기를 계산
    return loss.data

# function name : update_model_param
# param in : learning_rate, w, b
# Description
"""
- learning rate(lr)를 지정할 수 있도록 파라미터 입력으로 받자
- lr이 커지면 그래프 상에서 이동하는 보폭이 커짐?
"""
def update_model_param(learning_rate, w, b):
    w.data -= learning_rate * w.grad.data
    b.data -= learning_rate * b.grad.data

# function name : plot_variable
# param in : x(x축), y(y축), z(그래프스타일. 생략가능), **kwargs(추가옵션)
# Description
"""
주어진 데이터를 그래프로 시각화하는 함수
- 함수 x와 y 데이터를 가져와 l 리스트에 추가.
- l[0]을 x축, l[1]을 y축으로 설정
"""
def plot_variable(x, y, z='', **kwargs):
    l = []
    for a in [x, y]:
        l.append(a.data)
    plt.plot(l[0], l[1])

if __name__ == "__main__":
    # 데이터 가져오기
    x, y = get_data()
    print(x, y)

    # 초기 가중치 설정 : 랜덤값
    w, b = get_weights()
    print(w, b)

    # 초기 예측값 계산
    y_pred = simple_network(x, w, b)
    print(y_pred)

    # 학습률(lr)과 에포크 수 설정
    learning_rate = 1e-4
    num_epochs = 500

    # 반복 -> 학습 + 모델업데이트
    for epoch in range(num_epochs):
        # 순잔파를 통해 예측값 y_pred
        y_pred = simple_network(x, w, b)

        # 손실 계산
        loss = loss_fn(y, y_pred, w, b)

        # loss.backward() # 역전파 수행
        # update_model_param(learning_rate, w, b) # 모델파라미터 업데이트

        # 50 에포크마다 손실 출력
        if epoch % 50 == 0:
            print("loss : ", loss)
        update_model_param(learning_rate, w, b)

