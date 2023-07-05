import random


def gen_data(mat, n, m):
    for i in range(n):
        for j in range(m):
            mat[i][j] = random.randint(1, 9)


def matmul(mat1, mat2, result):
    n = len(mat1)
    m = len(mat2)
    p = len(mat2[0])

    for i in range(n):
        for j in range(p):
            for k in range(m):
                result[i][j] += mat1[i][k] * mat2[k][j]


if __name__ == "__main__":
    random.seed(8)

    n = random.randint(3, 20)
    m = random.randint(3, 20)

    print(n, m) # 10 14

    mat1 = [[0] * m for _ in range(n)]
    mat2 = [[0] * n for _ in range(m)]
    result = [[0] * n for _ in range(n)]

    gen_data(mat1, n, m)
    gen_data(mat2, m, n)
    matmul(mat1, mat2, result)

    for row in result[:6]:
        print(row[:6])

"""
[365, 251, 310, 326, 346, 360]
[384, 335, 413, 364, 484, 346]
[352, 303, 297, 248, 355, 292]
[371, 389, 422, 366, 478, 336]
[407, 408, 430, 392, 508, 361]
[368, 317, 330, 332, 420, 351]
"""