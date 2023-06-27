import torch
# nn layer들이 정의되어있는 모듈
import torch.nn as nn
# cost function이 정의되어있는 모듈
import torch.nn.functional as F

from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

# 데이터 불러오기

# x_train : 4x3 matrix
x_train = torch.FloatTensor(
    [
        [70, 82, 75],
        [93, 88, 93],
        [90, 90, 100],
        [96, 98, 100]
    ]
)

# y_train : 4x1 matrix
y_train = torch.FloatTensor(
    [
        [150],
        [185],
        [190],
        [199]
    ]
)


"""
- TensorDataset : Tensor 들을 입력받아 사용할 수 있는 Dataset 형태로 변환
    - dataset = TensorDataset(x, y)
- DataLoader
    - 기본적으로 2개의 옵션을 입력 (batch_size, shuffle 정보)
    - 배치사이즈는 통상적으로 2의 배수를 입력하는 것을 권장
    - 셔플을 사용하는 이유
        - 모델이 데이터셋의 순서에 익숙해지지 않게 함
        - 편향적으로 모델이 만들어질 확률이 낮아짐
        - 오버피팅을 막음
"""
dataset = TensorDataset(x_train, y_train)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# model 정의
model = nn.Linear(3, 1) # 입력과 출력 dimension을 정하면 됨
# input은 4x3 output은 4x1 매트릭스이다.
# Linear에 들어갈 입력 dimension은 feature의 개수. 즉 칼럼 갯수

# 최적화는 무엇으로 할 건지 설정
optim = torch.optim.SGD(model.parameters(), lr=1e-5)
# model.parameters() 는 모델의 파라미터를 초기화한 것
# learning rate는 꼭 1e-5가 아니어도 됨

# 학습 코드 작성
"""
for epoch in range(nb_epoch+1):
- Loss값을 출력(print)할 때 보통은 1000번, 10000번 마다 한번씩 출력하는데,
    이때 제일 마지막을 찍기 위해 +1 해줌
- 지금은 20번밖에 안도니까 +1안함

# 100개의 데이터가 있는데 배치사이즈가 50이면, 한번에 50개의 데이터씩 2번 도는 것
"""

nb_epoch = 20
for epoch in range(nb_epoch):
    for batch_idx, samples in enumerate(dataloader):
        x_train, y_train = samples

        # H(x) 계산
        # 모델에 x_train을 넣어 예측값 만듦
        pred = model(x_train)

        # cost 계산 (예측값, 정답값)
        cost = F.mse_loss(pred, y_train)

        # gradient Descent Algorithm
        # zero_grad()는 반드시 해야 한다. 아니면 값이 누적됨
        optim.zero_grad()
        cost.backward()
        optim.step()

        # 지금 몇번째 에포크인지/전체 에포크 수
        # cost.data = cost.item
        print(f'Epoch: {epoch}/{nb_epoch}, Batch: {batch_idx+1}/{len(dataloader)},'
              f'Cost: {cost.item(): .6f}, {cost.data}')






