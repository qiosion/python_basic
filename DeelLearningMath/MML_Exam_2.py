import numpy as np
from numpy.linalg import norm

def inner_product(vectors, in_vec):
    max_similarity = (0, 0)
    max_similarity = list(max_similarity)
    for i in range(len(vectors)):
        similarity = np.inner(vectors[i], in_vec)
        output = similarity / (norm(vectors[i]) * norm(in_vec))

        if (output > max_similarity[1]):
            max_similarity[1] = round(output, 2)
            max_similarity[0] = i
    return max_similarity


if __name__ == "__main__":
    np.random.seed(1234)
    doc_vec = np.zeros((100, 6))

    # print(doc_vec)

    for i in range(100):
        for j in range(6):
            doc_vec[i][j] = np.round(np.random.random(),2)

    vec_doc_1 = [0.2, 0.4, 0.02, 0.1, 0.9, 0.8]
    print(inner_product(doc_vec, vec_doc_1))
    # 정답 [82, 0.97]