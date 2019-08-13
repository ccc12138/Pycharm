import numpy as np

def matrix2feature(A):
    a, b = np.linalg.eig(A)
    return a, b
