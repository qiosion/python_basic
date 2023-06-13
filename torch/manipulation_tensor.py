import matplotlib.pyplot as plt
import torch
import numpy as np
from glob import glob
from PIL import Image

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
# from sklearn.datasets import load_boston -> 오류남
# 스킷런에서 보스턴 주택 가격을 가져오는 것은 보안문제 때문에 이제 못씀

# 캘리포니아 주택 가격을 사용하자
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()
# print(housing)
print(housing.data.shape) # (20640, 8) : row 가 20640개, 특징(feature)가 8개

# housing.data 는 numpy array type
# numpy의 array(배열)를 torch의 Tensor 타입으로 변경
california_tensor = torch.from_numpy(housing.data)
print(california_tensor.size(), california_tensor.dim()) # torch.Size([20640, 8]) 2

# california_tensor에서 원하는 데이터를 슬라이싱을 통해 가져와보자
print(california_tensor[:2, 1: -1])
# [:2] : 첫 번째부터 두 번째까지의 행을 선택
# 1:-1 : 두 번째 열부터 마지막에서 두 번째 열까지의 열을 선택

# 원하는 데이터를 슬라이싱을 통해 가져오는 연습을 해보자


"""

"""
# 3D Tensor
# - image: size, 3 channel(R,G,B)
#     - 1920 x 1080 x 3 (1920, 1080, 3) :
#         가로 1920, 세로 1080, RGB 색 공간에서 3개의 채널(R,G,B)를 가지는 이미지
# - MNIST : 숫자 손글씨 dataset
#     - image: 28x28
#         - 각 이미지는 가로28 x 세로28. 흑백이므로 채널 정보가 없다
#         - 한 픽셀은 0부터 255까지의 값을 가짐. 값이 높을수록 더 밝은 색
#     - batch_size, img_w, img_h ⇒ (64, 28, 28)
#     - 일반적으로 MNIST 데이터셋은 작은 규모의 데이터셋으로 간주되며,
#         훈련이나 테스트 시에는 배치(batch) 단위로 처리됩니다.
#         예를 들어, 배치 크기가 64라면 한 번에 64개의 이미지를 처리하게 됩니다.
#         따라서, 배치 크기가 (64, 28, 28)인 경우,
#         한 번에 64개의 28x28 크기의 흑백 이미지를 처리하는 것을 의미합니다
# - batch size matrix 를 가지고 올때도 3D tensor 을 이용할 수 있음
#     - 5일 단위로 24시간 동안 처리하길 원하는 이미지가 100개일 때 5 x 24 x 100 라고 표현할 수도 있음

from PIL import Image

dog = np.array(Image.open("../dataset_CatDog/dog.566.jpg").resize((224, 224)))
# np.array() : 이미지(특정한 값을 가지고 있는 object 형태)를 array 형태로 사용하기 위해 형변환

# numpy -> tensor 변환
dog_tensor = torch.from_numpy(dog)
print(f'size, dimension of color image: {dog_tensor.size()},'
      f'{dog_tensor.dim()}')

plt.imshow(dog)
plt.show()

"""

"""
경로 구분
리눅스 linux 계열 : / 
윈도우 windows : \
"""

"""
# 4D tensor

from glob import glob
from PIL import Image

dog_list = glob("../dataset_CatDog/test_set/dogs/*.jpg")
# print(dog_list[:2])
# ['../dataset_CatDog/test_set/dogs\\dog.4001.jpg', '../dataset_CatDog/test_set/dogs\\dog.4002.jpg']

# 3D
img_list = []
# img_list 는 아래의 for 문을 통해 3차원 배열이 됨
# [ [[[]]], #224x224x3, [[[]]] ] 형태
for dog in dog_list[:64]:
    img_list.append(np.array(Image.open("../dataset_CatDog/dog.566.jpg").resize((224, 224))))

# 4D
dogs_imgs = np.array(img_list)
print(dogs_imgs.shape, dogs_imgs.ndim, dogs_imgs.size)
# (64, 224, 224, 3)  4  9633792

dog_tensor = torch.from_numpy(dogs_imgs)
print(dog_tensor.size(), dog_tensor.dim())
# torch.Size([64, 224, 224, 3])  4
"""

"""
# pytorch 에서 자주 사용되고, 기존 코드를 분석할 때 필요한 것들

# 1. Broadcasting
# 브로드캐스팅을 통해 행렬의 크기가 달라도 계산해줌
# 행렬의 덧셈, 뺄셈
# - 행렬 A, B가 있을 때, 두 행렬에 대해 덧셈, 뺄셈 하고자 할 경우 두 행렬의 크기가 같아야 함
# 행렬의 곱셈
# - A 행렬의 열의 갯수와 B 행렬의 행의 갯수가 동일해야 계산 가능

# 1x2 행렬을 만들어보자
m1 = torch.FloatTensor([ [3, 3] ]) # 1 x 2 행렬(매트릭스)
m2 = torch.FloatTensor([ [2, 2] ])
m3 = torch.FloatTensor([2]) # 벡터

# 행렬의 덧셈
print(m1 + m2) # tensor([[5., 5.]])
print(m1 + m3) # tensor([[5., 5.]])
# m3를 브로드 캐스팅해서 [ [2, 2] ] 행렬로 만들어준 뒤 덧셈 계산

# 행렬의 곱셈



# 1x2, 2x1 행렬 생성해서 더하기


"""

"""
# 2. in-place 연산자 inplace
# 변수의 값을 변경하는 연산자. 새로운 변수를 생성하지 않고 기존 변수의 값을 직접 수정

a = torch.FloatTensor([ [1, 2], [3, 4] ])
b = torch.FloatTensor([ [1, 2], [3, 4] ])

print(f'{a + b}\n{torch.add(a, b)}\n{a}') # a + b와 같은 연산을 했지만, 원본 텐서에는 영향이 없음

# 브로드캐스팅 + inplace=True (_ 연산자)
print(f'{a.add_(2)}\n{a}')
"""

"""
# 3. Matrix Multiplication, element_wise 곱셈
# 3-1. Matrix Multiplication (행렬곱) matmul
#     - 두개의 행렬을 곱함
#     - 행렬 A와 B의 곱은 A의 행 벡터와 B의 열 벡터를 선형 결합
#     - 왼쪽 행렬의 열의 수와 오른쪽 행렬의 행 수가 일치해야 함
# 3-2. Element-wise 곱 (원소별 곱셈) element-wise
#     - 두개의 행렬 또는 배열에서 동일한 위치에 있는 원소들 끼리 곱함
#     - 두 행렬의 크기가 같아야 함

m1 = torch.FloatTensor([ [1, 2], [3, 4] ]) # 2x2 행렬
m2 = torch.FloatTensor([ [1], [2] ]) # 2x1 행렬

# 행렬1.matmul(행렬2) : 행렬곱 Matrix Multiplication
# 첫번째 행렬의 열 갯수와 두번째 행렬의 행 갯수만 맞으면 어떤 행렬이든 곱셈 가능
print(m1.shape, m2.shape, m1.matmul(m2)) # 2x2 matmul 2x1 => 2x1 행렬이 나옴

# * 또는 행렬1.mul(행렬2) : 원소곱 Element-wise
print(m1*m2, m1.mul(m2))

"""

"""
# CPU vs GPU
from torch import cuda
import time

# CPU
start = time.time()
a = torch.rand(20000, 20000)
b = torch.rand(20000, 20000)
c = a.matmul(b)
end = time.time()

print(f'cpu: {end-start} seconds') # cpu: 23.631630659103394 seconds

# GPU
use_gpu = cuda.is_available()
print(torch.cuda.get_device_name()) # Quadro RTX 5000

start = time.time()
if use_gpu:
    print("Using CUDA")
    a = a.cuda()
    b = b.cuda()
    a.matmul(b)
end = time.time()

if use_gpu:
    print(f'gpu: {end-start} seconds') # gpu: 3.471745491027832 seconds
"""
# vector : 1D tensor. 선. 리스트. 배열
#     - 2-dimensional vector 2차원 벡터 : 평면에서의 좌표. x축, y축으로 이동한 점
#     - 3-dimensional vector : 3차원 공간에서의 좌표. x축, y축, z축으로 이동한 점

# 4. mean, sum, max, argmax, ..
# dimension 옵션
# m1.mean(dim=0 or 1)
# dim=0 : 첫번째 차원(dimension)을 제거한다는 의미
# 행을 고려하지 않고 열(column 칼럼) 단위로 계산하겠다
# dim=1 : 두번째 차원을 제거. 즉, 행(row) 단위로 계산

# 4-1. mean : 평균
v2 = torch.FloatTensor([1, 2])
v3 = torch.FloatTensor([1, 2, 3])
print(v2.mean()) # (1 + 2) / 2 # tensor(1.5000)
print(v3.mean()) # (1 + 2 + 3) / 3 # tensor(2.)

# matrix : 2D tensor. 행렬
m1 = torch.FloatTensor([ [1, 2], [3, 4]])
print("m1.mean(): ", m1.mean()) # (1 + 2 + 3 + 4) / 4 # tensor(2.5000)

print(m1.mean(dim=0)) # tensor([2., 3.])
print(m1.mean(dim=1)) # tensor([1.5000, 3.5000])

# 4-2. sum : 합
print(m1.sum()) # tensor(10.)
print(m1.sum(dim=0)) # (1+3), (2+4) # tensor([4., 6.])
print(m1.sum(dim=1)) # (1+2), (3+4) # tensor([3., 7.])

# 4-3. max와 argmax
# max : Tensor의 item(element) 중에 가장 큰 값(최댓값)을 반환
# argmax : Tensor의 item(element) 중에 가장 큰 값(최댓값)의 인덱스를 반환

t = torch.FloatTensor([ [1, 4], [5, 4] ]) # argmax : 2
t = torch.FloatTensor([ [1, 4, 5], [6, 7, 7] ]) # argmax : 4
print(f'argmax: {t.argmax()}') # 4 : 최대값이 중복이면 처음 인덱스를 반환

# dim 옵션 가능. max, argmax 값을 둘 다 출력하게 됨
print(t.max(dim=0))
# torch.return_types.max(values=tensor([6., 7., 7.]), indices=tensor([1, 1, 1]))
print(t.max(dim=1))
# torch.return_types.max(values=tensor([5., 7.]), indices=tensor([2, 1]))

