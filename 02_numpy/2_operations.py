import sys
import time
import numpy as np

my_array = np.array([1, 2, 3])
second_array = np.array([
    (1, 2, 3, 4, 5, 6),
    (7, 8, 9, 10, 11, 12)
])

# returns the type of array
print(my_array.ndim)

# returns the byte size
print(my_array.itemsize)

# returns datatype
print(my_array.dtype)

# return size of array
print(second_array.size)

# return the shape of array
print(second_array.shape)
