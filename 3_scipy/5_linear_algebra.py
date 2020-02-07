from scipy import linalg
import numpy as np

# inverse of a matrix
a = np.array([
    [1, 2],
    [4, 5]
])
b = linalg.inv(a)
print(b)
