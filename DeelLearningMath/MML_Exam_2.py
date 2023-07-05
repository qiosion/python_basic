import numpy as np


def inner_product(vectors, in_vec):
    max_similarity = (0, 0)
    for i in range(len(vectors)):
        similarity = np.inner(vectors[i], in_vec)
        if similarity > max_similarity[1]:
            max_similarity = (i, similarity)
    max_similarity = (max_similarity[0], round(max_similarity[1], 3))
    return max_similarity


if __name__ == "__main__":
    np.random.seed(1234)
    doc_vec = np.random.random((100, 6))

    # print(doc_vec)

    vec_doc_1 = [0.2, 0.4, 0.02, 0.1, 0.9, 0.8]
    print(inner_product(doc_vec, vec_doc_1))
    # 정답 (9, 2.1)