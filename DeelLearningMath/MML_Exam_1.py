import random
import numpy as np

np.random.seed(8)

def gen_data(mat, n, m):
    for i in range(n):
        for j in range(m):
            mat[i][j] = np.random.randint(1, 10)


def matmul(mat1, mat2, result):
    n = len(mat1)
    m = len(mat2)
    p = len(mat2[0])

    for i in range(n):
        for j in range(p):
            for k in range(m):
                result[i][j] += mat1[i][k] * mat2[k][j]


if __name__ == "__main__":

    n = np.random.randint(3, 20)
    m = np.random.randint(3, 20)

    print(n, m) # 6 12

    mat1 = np.zeros((n, m))
    mat2 = np.zeros((m, n))
    result = np.zeros((n, n))

    gen_data(mat1, n, m)
    gen_data(mat2, m, n)
    matmul(mat1, mat2, result)

    # print(mat1)
    # print(mat2)
    print(result)
    # print(result.shape) (6, 6)

"""
[365, 251, 310, 326, 346, 360]
[384, 335, 413, 364, 484, 346]
[352, 303, 297, 248, 355, 292]
[371, 389, 422, 366, 478, 336]
[407, 408, 430, 392, 508, 361]
[368, 317, 330, 332, 420, 351]
"""