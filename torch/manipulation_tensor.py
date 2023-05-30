import torch
import numpy as np

# print(torch.__version__) # 1.12.1

"""
Vertor --> Matrix --> Tensor

Scalar : 0차원 텐서 0-dimensional Tensor. 점
Vector : 1차원 텐서 1-dimensional Tensor. 선 -> 리스트
Matrix : 2차원 텐서 2-dimensional Tensor. 면 -> 데이터프레임
"""

"""
# Vector : 1D
# 지난주 평균 온도를 벡터로 표현
temp = torch.FloatTensor (
    [15, 29.1, 30.2, 18.9, 15, 18, 19]
)
print(temp.size(), temp.dim()) # torch.Size([7]) 1

# Tensor 이지만 접근 방식은 리스트와 동일하게 접근하면 됨
# 인덱스, 슬라이싱 가능
print(f'월, 화 평균 온도 : {temp[0]}, {temp[1]}') # 월, 화 평균 온도 : 15.0, 29.100000381469727
print(f'화~목 평균 온도 : {temp[1:4]}') # 화~목 평균 온도 : tensor([29.1000, 30.2000, 18.9000])

# Matrix : 2D
# DataFrame 과 동일한 형태
t = torch.FloatTensor([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])
print(t.size(), t.dim()) # torch.Size([4, 3]) 2

# 데이터에 접근하기 위해서는 슬라이싱 사용
# 첫번째 차원(Row)의 모든 것과, 두번째 차원(Col)의 두번째 요소만 가지고 와보자
print(t[:, 1]) # tensor([ 2.,  5.,  8., 11.])

# Row의 세번째 요소값들 모두 가져와라
print(t[2, :]) # tensor([7., 8., 9.])

# t텐서에서 [5, 6], [8, 9] 만 가져오는 법
print(t[1:3, 1:3]) # tensor([[5., 6.], [8., 9.]])

"""
"""
스킷런에서 보스턴 주택 가격을 가져오고자 한다
from sklearn.datasets

from sklearn.datasets import load_boston -> 오류남
내역보면 뭐때문인지, 대안도 알려줌
"""
# 캘리포니아 주택 가격
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()
# print(housing)
print(housing.data.shape) # (20640, 8) : row 가 20640개, 특징(feature)가 8개

# housing.data 는 numpy array type
# numpy array => torch_Tensor 로 변경
california_tensor = torch.from_numpy(housing.data)
print(california_tensor.size(), california_tensor.dim()) # torch.Size([20640, 8]) 2

# california_tensor에서 원하는 데이터를 슬라이싱을 통해 가져와보자
print(california_tensor.data[:2])
