import numpy as np

def matrix_transpose(A):
    A = np.array(A)
    M, N = A.shape
    result = np.empty((N, M), dtype=A.dtype)
    for i in range(M):
        result[:, i] = A[i, :]
    return result