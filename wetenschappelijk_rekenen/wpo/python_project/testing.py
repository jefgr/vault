import numpy as np

A = np.asmatrix([[1, 0, 0],[0, 4, 0],[0, 0, 9]])

B = np.diag(A)
C = np.diag(B)
E = [[1, 2, 3],[0, 4, 0],[0, 0, 9]]
D = list(zip(*E))
print(D)
